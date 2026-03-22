"""
Main experiment runner for the Coordination-Enhancing Video Game study.

Uses GPT-4.1 agents as proxies for human players to test whether
game experience improves zero-shot coordination with strangers.
"""

import os
import sys
import json
import random
import time
import hashlib
from datetime import datetime
from pathlib import Path
from collections import defaultdict

import numpy as np
from openai import OpenAI

from coordination_games import (
    ALL_TREATMENTS,
    FOCAL_POINT_TASKS,
    ROLE_ASSIGNMENT_TASKS,
    CONVENTION_TASK,
)

# ── Configuration ─────────────────────────────────────────────────────────

SEED = 42
MODEL = "gpt-4.1"
TEMPERATURE = 0.9  # High enough for variety, low enough for coherence
N_PAIRS = 50  # pairs per condition per task
MAX_RETRIES = 3
RESULTS_DIR = Path("/workspaces/coordination-ai-game-claude/results")

random.seed(SEED)
np.random.seed(SEED)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


# ── API Calling ───────────────────────────────────────────────────────────

def call_llm(system_prompt: str, user_prompt: str, seed_val: int = None) -> str:
    """Call GPT-4.1 with retry logic."""
    for attempt in range(MAX_RETRIES):
        try:
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": user_prompt})

            kwargs = {
                "model": MODEL,
                "messages": messages,
                "temperature": TEMPERATURE,
                "max_tokens": 50,
            }
            if seed_val is not None:
                kwargs["seed"] = seed_val

            response = client.chat.completions.create(**kwargs)
            return response.choices[0].message.content.strip()
        except Exception as e:
            if attempt < MAX_RETRIES - 1:
                time.sleep(2 ** attempt)
            else:
                print(f"  API error after {MAX_RETRIES} retries: {e}")
                return ""


def make_system_prompt(treatment: dict) -> str:
    """Create system prompt for an agent based on treatment condition."""
    base = "You are participating in a coordination experiment."
    if treatment["description"] is None:
        return base
    return f"{base}\n\nBackground: {treatment['description']}"


# ── Experiment 1: Focal Point Tasks ───────────────────────────────────────

def run_focal_point_experiment(treatment: dict, n_pairs: int) -> dict:
    """Run focal point coordination tasks for a single treatment."""
    treatment_name = treatment["name"]
    system_prompt = make_system_prompt(treatment)
    results = {}

    for task in FOCAL_POINT_TASKS:
        task_id = task["id"]
        matches = 0
        responses_a = []
        responses_b = []

        print(f"  Task {task_id}...", end=" ", flush=True)

        for pair_idx in range(n_pairs):
            # Two independent agents, same system prompt, same task
            seed_a = hash(f"{task_id}_{pair_idx}_a") % (2**31)
            seed_b = hash(f"{task_id}_{pair_idx}_b") % (2**31)

            resp_a = call_llm(system_prompt, task["prompt"], seed_val=seed_a)
            resp_b = call_llm(system_prompt, task["prompt"], seed_val=seed_b)

            responses_a.append(resp_a)
            responses_b.append(resp_b)

            # Normalize and compare
            norm_a = normalize_response(resp_a)
            norm_b = normalize_response(resp_b)
            if norm_a and norm_b and norm_a == norm_b:
                matches += 1

        match_rate = matches / n_pairs if n_pairs > 0 else 0
        print(f"{match_rate:.2%} ({matches}/{n_pairs})")

        results[task_id] = {
            "match_rate": match_rate,
            "matches": matches,
            "n_pairs": n_pairs,
            "responses_a": responses_a,
            "responses_b": responses_b,
        }

    return results


def normalize_response(resp: str) -> str:
    """Normalize response for comparison."""
    if not resp:
        return ""
    # Lowercase, strip punctuation, take first word/line
    resp = resp.lower().strip().rstrip(".")
    # Take first line only
    resp = resp.split("\n")[0].strip()
    # Remove common prefixes
    for prefix in ["i choose ", "i pick ", "my choice is ", "i'd pick ", "i would pick ", "i'll go with "]:
        if resp.startswith(prefix):
            resp = resp[len(prefix):]
    resp = resp.strip().strip("'\"")
    # Normalize common variants
    replacements = {
        "twelve": "12", "noon": "12:00 pm", "12 pm": "12:00 pm", "12:00": "12:00 pm",
        "midnight": "12:00 am",
        "red": "red", "blue": "blue",
        "circle": "circle", "square": "square", "triangle": "triangle",
        "monday": "monday", "tuesday": "tuesday", "wednesday": "wednesday",
        "thursday": "thursday", "friday": "friday", "saturday": "saturday", "sunday": "sunday",
        "new york": "new york", "new york city": "new york", "nyc": "new york",
        "paris": "paris", "london": "london", "tokyo": "tokyo",
        "dog": "dog", "cat": "cat",
        "pizza": "pizza", "apple": "apple",
    }
    for k, v in replacements.items():
        if resp == k:
            resp = v
            break
    return resp


# ── Experiment 2: Role Assignment Tasks ───────────────────────────────────

def run_role_assignment_experiment(treatment: dict, n_pairs: int) -> dict:
    """Run role assignment tasks for a single treatment."""
    treatment_name = treatment["name"]
    system_prompt = make_system_prompt(treatment)
    results = {}

    for task in ROLE_ASSIGNMENT_TASKS:
        task_id = task["id"]
        complementary = 0
        responses_a = []
        responses_b = []

        print(f"  Task {task_id}...", end=" ", flush=True)

        for pair_idx in range(n_pairs):
            prompt_a = task["prompt"].replace("{role_id}", "A (you go first)")
            prompt_b = task["prompt"].replace("{role_id}", "B (you go second)")

            seed_a = hash(f"{task_id}_{pair_idx}_a") % (2**31)
            seed_b = hash(f"{task_id}_{pair_idx}_b") % (2**31)

            resp_a = call_llm(system_prompt, prompt_a, seed_val=seed_a)
            resp_b = call_llm(system_prompt, prompt_b, seed_val=seed_b)

            responses_a.append(resp_a)
            responses_b.append(resp_b)

            # Check if they chose different (complementary) roles
            norm_a = normalize_response(resp_a)
            norm_b = normalize_response(resp_b)
            if norm_a and norm_b and norm_a != norm_b:
                complementary += 1

        comp_rate = complementary / n_pairs if n_pairs > 0 else 0
        print(f"{comp_rate:.2%} ({complementary}/{n_pairs})")

        results[task_id] = {
            "complementarity_rate": comp_rate,
            "complementary_count": complementary,
            "n_pairs": n_pairs,
            "responses_a": responses_a,
            "responses_b": responses_b,
        }

    return results


# ── Experiment 3: Convention Formation ────────────────────────────────────

def run_convention_experiment(treatment: dict, n_pairs: int) -> dict:
    """Run Lewis signaling game for convention formation speed."""
    system_prompt_base = make_system_prompt(treatment)
    n_rounds = CONVENTION_TASK["n_rounds"]
    objects = CONVENTION_TASK["objects"]
    signals = CONVENTION_TASK["signals"]

    all_convergence_rounds = []
    all_accuracy_curves = []

    print(f"  Convention formation ({n_pairs} pairs, {n_rounds} rounds)...", flush=True)

    for pair_idx in range(n_pairs):
        history_sender = []
        history_receiver = []
        correct_per_round = []

        for round_idx in range(n_rounds):
            # Random object
            obj = random.choice(objects)
            # Sender sees object, chooses signal
            sender_history_str = "\n".join(history_sender[-5:]) if history_sender else "No previous rounds."
            sender_prompt = f"""Round {round_idx + 1}: You are the SENDER. The object is '{obj}'.
Choose a signal from {signals} to communicate this object to your partner.
Previous rounds: {sender_history_str}
Respond with just the signal number."""

            signal = call_llm(
                system_prompt_base + "\n" + CONVENTION_TASK["system"],
                sender_prompt,
                seed_val=hash(f"conv_{pair_idx}_{round_idx}_s") % (2**31),
            )
            signal = signal.strip().replace("Signal ", "").replace("signal ", "")[:1]
            if signal not in ["1", "2", "3"]:
                signal = random.choice(signals)

            # Receiver sees signal, guesses object
            receiver_history_str = "\n".join(history_receiver[-5:]) if history_receiver else "No previous rounds."
            receiver_prompt = f"""Round {round_idx + 1}: You are the RECEIVER. The signal is '{signal}'.
Guess which object (A, B, or C) the sender is communicating.
Previous rounds: {receiver_history_str}
Respond with just the letter."""

            guess = call_llm(
                system_prompt_base + "\n" + CONVENTION_TASK["system"],
                receiver_prompt,
                seed_val=hash(f"conv_{pair_idx}_{round_idx}_r") % (2**31),
            )
            guess = guess.strip().upper()[:1]
            if guess not in ["A", "B", "C"]:
                guess = random.choice(objects)

            correct = guess == obj
            correct_per_round.append(correct)

            # Update histories
            feedback = f"Round {round_idx + 1}: Object={obj}, Signal={signal}, Guess={guess}, {'CORRECT' if correct else 'WRONG'}"
            history_sender.append(feedback)
            history_receiver.append(feedback)

        # Find convergence round (3 consecutive correct)
        convergence = None
        for i in range(len(correct_per_round) - 2):
            if all(correct_per_round[i:i+3]):
                convergence = i + 1
                break
        all_convergence_rounds.append(convergence)
        all_accuracy_curves.append(correct_per_round)

    # Compute metrics
    converged = [c for c in all_convergence_rounds if c is not None]
    avg_convergence = np.mean(converged) if converged else float("inf")
    convergence_rate = len(converged) / n_pairs

    # Average accuracy by round
    accuracy_by_round = []
    for r in range(n_rounds):
        round_acc = np.mean([curve[r] for curve in all_accuracy_curves])
        accuracy_by_round.append(round_acc)

    print(f"    Convergence rate: {convergence_rate:.2%}, Avg round: {avg_convergence:.1f}")

    return {
        "convergence_rate": convergence_rate,
        "avg_convergence_round": avg_convergence if converged else None,
        "accuracy_by_round": accuracy_by_round,
        "n_pairs": n_pairs,
        "all_convergence_rounds": all_convergence_rounds,
    }


# ── Main Runner ───────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("Coordination-Enhancing Video Game Experiment")
    print(f"Model: {MODEL} | Temperature: {TEMPERATURE} | Pairs/condition: {N_PAIRS}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 70)

    all_results = {
        "config": {
            "model": MODEL,
            "temperature": TEMPERATURE,
            "n_pairs": N_PAIRS,
            "seed": SEED,
            "timestamp": datetime.now().isoformat(),
        },
        "focal_point": {},
        "role_assignment": {},
        "convention": {},
    }

    for treatment in ALL_TREATMENTS:
        name = treatment["name"]
        print(f"\n{'─' * 60}")
        print(f"Treatment: {name}")
        print(f"{'─' * 60}")

        # Experiment 1: Focal Points
        print(f"\n[Experiment 1] Focal Point Coordination:")
        fp_results = run_focal_point_experiment(treatment, N_PAIRS)
        all_results["focal_point"][name] = fp_results

        # Experiment 2: Role Assignment
        print(f"\n[Experiment 2] Role Assignment:")
        role_results = run_role_assignment_experiment(treatment, N_PAIRS)
        all_results["role_assignment"][name] = role_results

        # Experiment 3: Convention Formation
        print(f"\n[Experiment 3] Convention Formation:")
        conv_results = run_convention_experiment(treatment, N_PAIRS)
        all_results["convention"][name] = conv_results

    # Save results
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    results_file = RESULTS_DIR / "experiment_results.json"

    # Convert numpy types for JSON serialization
    def convert_numpy(obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, (np.bool_,)):
            return bool(obj)
        return obj

    with open(results_file, "w") as f:
        json.dump(all_results, f, indent=2, default=convert_numpy)

    print(f"\n\nResults saved to {results_file}")
    print("Experiment complete!")


if __name__ == "__main__":
    main()
