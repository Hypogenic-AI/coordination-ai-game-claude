"""
Analysis of hard coordination tasks experiment.
"""

import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

RESULTS_DIR = Path("/workspaces/coordination-ai-game-claude/results")
PLOTS_DIR = RESULTS_DIR / "plots"

TREATMENT_ORDER = [
    "No Game (Baseline)", "Trivia Game (Control)",
    "Focal Point Game", "Convention Formation Game",
    "AI-Designed Coordination Game",
]
SHORT = {
    "No Game (Baseline)": "No Game", "Trivia Game (Control)": "Trivia",
    "Focal Point Game": "Focal Pt", "Convention Formation Game": "Convention",
    "AI-Designed Coordination Game": "AI-Designed",
}
COLORS = {
    "No Game (Baseline)": "#95a5a6", "Trivia Game (Control)": "#bdc3c7",
    "Focal Point Game": "#3498db", "Convention Formation Game": "#e67e22",
    "AI-Designed Coordination Game": "#2ecc71",
}


def main():
    with open(RESULTS_DIR / "hard_experiment_results.json") as f:
        data = json.load(f)

    hfp = data["hard_focal_point"]
    hrole = data["hard_role"]

    # ── Hard Focal Point Analysis ─────────────────────────────────────
    print("=" * 75)
    print("HARD FOCAL POINT TASKS")
    print("=" * 75)

    task_ids = list(hfp[TREATMENT_ORDER[0]].keys())

    # Print table
    print(f"\n{'Task':<22}", end="")
    for t in TREATMENT_ORDER:
        print(f" {SHORT[t]:>11}", end="")
    print()
    print("-" * 80)

    for tid in task_ids:
        print(f"{tid.replace('hfp_',''):<22}", end="")
        for t in TREATMENT_ORDER:
            rate = hfp[t][tid]["match_rate"]
            print(f" {rate:>10.0%}", end="")
        print()

    # Means
    treatment_means = {}
    for t in TREATMENT_ORDER:
        rates = [hfp[t][tid]["match_rate"] for tid in task_ids]
        treatment_means[t] = np.mean(rates)

    print(f"\n{'MEAN':<22}", end="")
    for t in TREATMENT_ORDER:
        print(f" {treatment_means[t]:>10.1%}", end="")
    print()

    # Only analyze tasks where baseline < 100% (room for improvement)
    hard_tasks = [tid for tid in task_ids if hfp[TREATMENT_ORDER[0]][tid]["match_rate"] < 1.0]
    print(f"\n--- Tasks with baseline < 100% (room for improvement): {len(hard_tasks)} ---")

    hard_means = {}
    for t in TREATMENT_ORDER:
        rates = [hfp[t][tid]["match_rate"] for tid in hard_tasks]
        hard_means[t] = np.mean(rates)

    baseline_hard = hard_means[TREATMENT_ORDER[0]]
    print(f"\n{'Treatment':<30} {'Hard Mean':>10} {'Ratio':>8} {'Improvement':>12}")
    print("-" * 65)
    for t in TREATMENT_ORDER:
        ratio = hard_means[t] / baseline_hard if baseline_hard > 0 else 0
        imp = hard_means[t] - baseline_hard
        print(f"{SHORT[t]:<30} {hard_means[t]:>9.1%} {ratio:>7.2f}x {imp:>+11.1%}")

    # Per-task improvement ratios for tasks with baseline < 100%
    print(f"\n--- Per-task improvement ratios (treatment/baseline) ---")
    print(f"{'Task':<22}", end="")
    for t in TREATMENT_ORDER[2:]:  # Skip baseline and trivia
        print(f" {SHORT[t]:>11}", end="")
    print()
    print("-" * 60)

    for tid in hard_tasks:
        base = hfp[TREATMENT_ORDER[0]][tid]["match_rate"]
        print(f"{tid.replace('hfp_',''):<22}", end="")
        for t in TREATMENT_ORDER[2:]:
            rate = hfp[t][tid]["match_rate"]
            ratio = rate / base if base > 0 else float("inf")
            marker = " *" if ratio >= 2.0 else ""
            print(f" {ratio:>9.2f}x{marker}", end="")
        print()

    # ── Hard Role Analysis ────────────────────────────────────────────
    print("\n" + "=" * 75)
    print("HARD ROLE ASSIGNMENT TASKS")
    print("=" * 75)

    role_ids = list(hrole[TREATMENT_ORDER[0]].keys())
    print(f"\n{'Task':<22}", end="")
    for t in TREATMENT_ORDER:
        print(f" {SHORT[t]:>11}", end="")
    print()
    print("-" * 80)

    for rid in role_ids:
        print(f"{rid.replace('hrole_',''):<22}", end="")
        for t in TREATMENT_ORDER:
            rate = hrole[t][rid]["complementarity_rate"]
            print(f" {rate:>10.0%}", end="")
        print()

    # AI-Designed game role performance
    print(f"\n--- AI-Designed Game: Role Assignment Improvement ---")
    for rid in role_ids:
        base = hrole[TREATMENT_ORDER[0]][rid]["complementarity_rate"]
        ai = hrole["AI-Designed Coordination Game"][rid]["complementarity_rate"]
        if base == 0:
            ratio_str = f"0%→{ai:.0%}"
        elif base < 1.0:
            ratio = ai / base
            ratio_str = f"{base:.0%}→{ai:.0%} ({ratio:.1f}x)"
        else:
            ratio_str = f"{base:.0%}→{ai:.0%}"
        print(f"  {rid}: {ratio_str}")

    # ── Visualizations ────────────────────────────────────────────────

    # 1. Hard focal point heatmap
    fig, ax = plt.subplots(figsize=(12, 8))
    matrix = np.zeros((len(task_ids), len(TREATMENT_ORDER)))
    for j, t in enumerate(TREATMENT_ORDER):
        for i, tid in enumerate(task_ids):
            matrix[i, j] = hfp[t][tid]["match_rate"]

    sns.heatmap(
        matrix, annot=True, fmt=".0%", cmap="RdYlGn",
        xticklabels=[SHORT[t] for t in TREATMENT_ORDER],
        yticklabels=[tid.replace("hfp_", "") for tid in task_ids],
        ax=ax, vmin=0, vmax=1,
    )
    ax.set_title("Hard Focal Point Match Rates by Task and Treatment", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "hard_focal_point_heatmap.png", dpi=150)
    plt.close()

    # 2. Improvement on hard tasks
    fig, ax = plt.subplots(figsize=(10, 6))
    treatments = TREATMENT_ORDER[2:]  # Treatment conditions only
    x = np.arange(len(hard_tasks))
    width = 0.25

    for i, t in enumerate(treatments):
        improvements = []
        for tid in hard_tasks:
            base = hfp[TREATMENT_ORDER[0]][tid]["match_rate"]
            rate = hfp[t][tid]["match_rate"]
            improvements.append(rate - base)
        bars = ax.bar(x + i * width, improvements, width, label=SHORT[t],
                     color=COLORS[t], edgecolor="black", linewidth=0.5)

    ax.axhline(y=0, color="black", linewidth=0.5)
    ax.set_ylabel("Improvement vs Baseline (pp)", fontsize=12)
    ax.set_title("Coordination Improvement on Hard Tasks\n(only tasks with baseline < 100%)", fontsize=14, fontweight="bold")
    ax.set_xticks(x + width)
    ax.set_xticklabels([tid.replace("hfp_", "") for tid in hard_tasks], rotation=45, ha="right")
    ax.legend(fontsize=10)
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "hard_task_improvements.png", dpi=150)
    plt.close()

    # 3. Role assignment comparison
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(role_ids))
    width = 0.15
    for i, t in enumerate(TREATMENT_ORDER):
        rates = [hrole[t][rid]["complementarity_rate"] for rid in role_ids]
        ax.bar(x + i * width, rates, width, label=SHORT[t],
               color=COLORS[t], edgecolor="black", linewidth=0.5)

    ax.set_ylabel("Complementarity Rate", fontsize=12)
    ax.set_title("Hard Role Assignment: Complementarity by Task and Treatment", fontsize=14, fontweight="bold")
    ax.set_xticks(x + 2 * width)
    ax.set_xticklabels([rid.replace("hrole_", "") for rid in role_ids])
    ax.legend(fontsize=9)
    ax.grid(axis="y", alpha=0.3)
    ax.set_ylim(0, 1.1)
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "hard_role_assignment.png", dpi=150)
    plt.close()

    # 4. Overall summary: best improvement ratios
    fig, ax = plt.subplots(figsize=(10, 6))
    # For each treatment, compute max improvement ratio on any hard task
    for t in TREATMENT_ORDER[2:]:
        ratios = []
        for tid in hard_tasks:
            base = hfp[TREATMENT_ORDER[0]][tid]["match_rate"]
            rate = hfp[t][tid]["match_rate"]
            if base > 0:
                ratios.append(rate / base)
        best = max(ratios) if ratios else 1.0
        mean_r = np.mean(ratios) if ratios else 1.0
        ax.barh(SHORT[t], mean_r, color=COLORS[t], edgecolor="black", linewidth=0.5)
        ax.text(mean_r + 0.02, SHORT[t], f"{mean_r:.2f}x (max: {best:.1f}x)", va="center", fontsize=10)

    ax.axvline(x=2.0, color="red", linestyle="--", linewidth=2, label="2x Target")
    ax.axvline(x=1.0, color="gray", linestyle=":", linewidth=1)
    ax.set_xlabel("Mean Improvement Ratio on Hard Tasks", fontsize=12)
    ax.set_title("Mean Coordination Improvement vs Baseline\n(Hard tasks only, baseline < 100%)", fontsize=14, fontweight="bold")
    ax.legend(fontsize=10)
    ax.set_xlim(0, 3.0)
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "overall_improvement_ratios.png", dpi=150)
    plt.close()

    print(f"\nPlots saved to {PLOTS_DIR}")

    # ── Summary statistics ────────────────────────────────────────────
    print("\n" + "=" * 75)
    print("KEY FINDINGS SUMMARY")
    print("=" * 75)

    # Count tasks where 2x improvement was achieved
    print(f"\nTasks where ≥2x improvement achieved (game-trained vs baseline):")
    for t in TREATMENT_ORDER[2:]:
        two_x_tasks = []
        for tid in hard_tasks:
            base = hfp[TREATMENT_ORDER[0]][tid]["match_rate"]
            rate = hfp[t][tid]["match_rate"]
            if base > 0 and rate / base >= 2.0:
                two_x_tasks.append((tid, base, rate, rate/base))
        print(f"\n  {SHORT[t]}:")
        if two_x_tasks:
            for tid, base, rate, ratio in two_x_tasks:
                print(f"    {tid}: {base:.0%} → {rate:.0%} ({ratio:.1f}x)")
        else:
            print(f"    None")

    # Best overall treatment
    print(f"\n--- Overall Best Treatment (mean ratio on hard tasks) ---")
    best_t = None
    best_ratio = 0
    for t in TREATMENT_ORDER[2:]:
        ratios = []
        for tid in hard_tasks:
            base = hfp[TREATMENT_ORDER[0]][tid]["match_rate"]
            if base > 0:
                ratios.append(hfp[t][tid]["match_rate"] / base)
        mean_r = np.mean(ratios)
        if mean_r > best_ratio:
            best_ratio = mean_r
            best_t = t
        print(f"  {SHORT[t]}: {mean_r:.2f}x mean improvement")
    print(f"\n  BEST: {SHORT[best_t]} at {best_ratio:.2f}x mean improvement")

    # AI-Designed role assignment
    print(f"\n--- AI-Designed Game: Role Assignment ---")
    ai_role_mean = np.mean([hrole["AI-Designed Coordination Game"][rid]["complementarity_rate"]
                            for rid in role_ids])
    base_role_mean = np.mean([hrole[TREATMENT_ORDER[0]][rid]["complementarity_rate"]
                              for rid in role_ids])
    print(f"  Baseline mean: {base_role_mean:.1%}")
    print(f"  AI-Designed mean: {ai_role_mean:.1%}")
    if base_role_mean > 0:
        print(f"  Ratio: {ai_role_mean/base_role_mean:.2f}x")


if __name__ == "__main__":
    main()
