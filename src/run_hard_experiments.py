"""
Run harder coordination tasks where baseline performance is lower,
allowing room for game-trained agents to show improvement.
"""

import os
import json
import random
import time
from datetime import datetime
from pathlib import Path

import numpy as np
from openai import OpenAI

from coordination_games import ALL_TREATMENTS
from hard_coordination_tasks import HARD_FOCAL_POINT_TASKS, HARD_ROLE_TASKS

SEED = 42
MODEL = "gpt-4.1"
TEMPERATURE = 0.9
N_PAIRS = 50
MAX_RETRIES = 3
RESULTS_DIR = Path("/workspaces/coordination-ai-game-claude/results")

random.seed(SEED)
np.random.seed(SEED)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def call_llm(system_prompt, user_prompt, seed_val=None):
    for attempt in range(MAX_RETRIES):
        try:
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": user_prompt})
            kwargs = {"model": MODEL, "messages": messages, "temperature": TEMPERATURE, "max_tokens": 50}
            if seed_val is not None:
                kwargs["seed"] = seed_val
            response = client.chat.completions.create(**kwargs)
            return response.choices[0].message.content.strip()
        except Exception as e:
            if attempt < MAX_RETRIES - 1:
                time.sleep(2 ** attempt)
            else:
                print(f"  API error: {e}")
                return ""


def make_system_prompt(treatment):
    base = "You are participating in a coordination experiment."
    if treatment["description"] is None:
        return base
    return f"{base}\n\nBackground: {treatment['description']}"


def normalize(resp):
    if not resp:
        return ""
    resp = resp.lower().strip().rstrip(".!").split("\n")[0].strip()
    for prefix in ["i choose ", "i pick ", "my choice is ", "i'd pick ", "i would pick ",
                    "i'll go with ", "my answer is ", "i select ", "i'd choose "]:
        if resp.startswith(prefix):
            resp = resp[len(prefix):]
    resp = resp.strip().strip("'\"")
    # Normalize some common variants
    if resp in ("$5", "$5.00", "5 dollars", "five dollars", "5"):
        resp = "$5"
    if resp in ("50", "fifty"):
        resp = "50"
    return resp


def run_hard_focal_points(treatment, n_pairs):
    system_prompt = make_system_prompt(treatment)
    results = {}
    for task in HARD_FOCAL_POINT_TASKS:
        tid = task["id"]
        matches = 0
        responses_a, responses_b = [], []
        print(f"  {tid}...", end=" ", flush=True)
        for i in range(n_pairs):
            seed_a = hash(f"{tid}_{i}_a") % (2**31)
            seed_b = hash(f"{tid}_{i}_b") % (2**31)
            a = call_llm(system_prompt, task["prompt"], seed_a)
            b = call_llm(system_prompt, task["prompt"], seed_b)
            responses_a.append(a)
            responses_b.append(b)
            na, nb = normalize(a), normalize(b)
            if na and nb and na == nb:
                matches += 1
        rate = matches / n_pairs
        print(f"{rate:.0%} ({matches}/{n_pairs})")
        results[tid] = {
            "match_rate": rate, "matches": matches, "n_pairs": n_pairs,
            "random_chance": task.get("random_chance", 0),
            "responses_a": responses_a, "responses_b": responses_b,
        }
    return results


def run_hard_roles(treatment, n_pairs):
    system_prompt = make_system_prompt(treatment)
    results = {}
    for task in HARD_ROLE_TASKS:
        tid = task["id"]
        complementary = 0
        responses_a, responses_b = [], []
        is_3way = "3way" in task.get("type", "")
        print(f"  {tid}...", end=" ", flush=True)
        for i in range(n_pairs):
            seed_a = hash(f"{tid}_{i}_a") % (2**31)
            seed_b = hash(f"{tid}_{i}_b") % (2**31)
            pa = task["prompt"].replace("{role_id}", "A")
            pb = task["prompt"].replace("{role_id}", "B")
            a = call_llm(system_prompt, pa, seed_a)
            b = call_llm(system_prompt, pb, seed_b)
            responses_a.append(a)
            responses_b.append(b)
            na, nb = normalize(a), normalize(b)
            if na and nb and na != nb:
                complementary += 1
        rate = complementary / n_pairs
        print(f"{rate:.0%} ({complementary}/{n_pairs})")
        results[tid] = {
            "complementarity_rate": rate, "complementary": complementary,
            "n_pairs": n_pairs, "responses_a": responses_a, "responses_b": responses_b,
        }
    return results


def main():
    print("=" * 70)
    print("HARD Coordination Tasks Experiment")
    print(f"Model: {MODEL} | Temp: {TEMPERATURE} | Pairs: {N_PAIRS}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 70)

    all_results = {
        "config": {"model": MODEL, "temperature": TEMPERATURE, "n_pairs": N_PAIRS,
                    "seed": SEED, "timestamp": datetime.now().isoformat()},
        "hard_focal_point": {},
        "hard_role": {},
    }

    for treatment in ALL_TREATMENTS:
        name = treatment["name"]
        print(f"\n{'─' * 55}")
        print(f"Treatment: {name}")
        print(f"{'─' * 55}")

        print("\n[Hard Focal Points]:")
        all_results["hard_focal_point"][name] = run_hard_focal_points(treatment, N_PAIRS)

        print("\n[Hard Roles]:")
        all_results["hard_role"][name] = run_hard_roles(treatment, N_PAIRS)

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out = RESULTS_DIR / "hard_experiment_results.json"

    def conv(o):
        if isinstance(o, (np.integer,)): return int(o)
        if isinstance(o, (np.floating,)): return float(o)
        if isinstance(o, np.ndarray): return o.tolist()
        return o

    with open(out, "w") as f:
        json.dump(all_results, f, indent=2, default=conv)
    print(f"\nResults saved to {out}")


if __name__ == "__main__":
    main()
