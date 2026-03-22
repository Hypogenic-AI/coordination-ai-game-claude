"""
Analysis and visualization for the Coordination-Enhancing Video Game experiment.

Performs statistical tests, generates visualizations, and creates summary tables.
"""

import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

RESULTS_DIR = Path("/workspaces/coordination-ai-game-claude/results")
PLOTS_DIR = RESULTS_DIR / "plots"
PLOTS_DIR.mkdir(parents=True, exist_ok=True)

# Treatment display order and colors
TREATMENT_ORDER = [
    "No Game (Baseline)",
    "Trivia Game (Control)",
    "Focal Point Game",
    "Convention Formation Game",
    "AI-Designed Coordination Game",
]
TREATMENT_SHORT = {
    "No Game (Baseline)": "No Game",
    "Trivia Game (Control)": "Trivia",
    "Focal Point Game": "Focal Pt",
    "Convention Formation Game": "Convention",
    "AI-Designed Coordination Game": "AI-Designed",
}
COLORS = {
    "No Game (Baseline)": "#95a5a6",
    "Trivia Game (Control)": "#bdc3c7",
    "Focal Point Game": "#3498db",
    "Convention Formation Game": "#e67e22",
    "AI-Designed Coordination Game": "#2ecc71",
}


def load_results():
    with open(RESULTS_DIR / "experiment_results.json") as f:
        return json.load(f)


# ── Statistical Analysis ─────────────────────────────────────────────────

def analyze_focal_points(data):
    """Statistical analysis of focal point match rates."""
    results = data["focal_point"]
    print("\n" + "=" * 70)
    print("EXPERIMENT 1: FOCAL POINT COORDINATION")
    print("=" * 70)

    # Aggregate match rates by treatment
    treatment_rates = {}
    for treatment in TREATMENT_ORDER:
        if treatment not in results:
            continue
        task_results = results[treatment]
        rates = [task_results[tid]["match_rate"] for tid in task_results]
        treatment_rates[treatment] = rates

    # Print per-task results
    print(f"\n{'Task':<20}", end="")
    for t in TREATMENT_ORDER:
        if t in results:
            print(f" {TREATMENT_SHORT[t]:>12}", end="")
    print()
    print("-" * 80)

    task_ids = list(results[TREATMENT_ORDER[0]].keys()) if TREATMENT_ORDER[0] in results else []
    for tid in task_ids:
        print(f"{tid:<20}", end="")
        for t in TREATMENT_ORDER:
            if t in results and tid in results[t]:
                rate = results[t][tid]["match_rate"]
                print(f" {rate:>11.1%}", end="")
        print()

    # Print aggregate statistics
    print(f"\n{'MEAN':<20}", end="")
    for t in TREATMENT_ORDER:
        if t in treatment_rates:
            print(f" {np.mean(treatment_rates[t]):>11.1%}", end="")
    print()

    # Statistical tests: each treatment vs baseline
    baseline_name = "No Game (Baseline)"
    if baseline_name in treatment_rates:
        baseline_rates = treatment_rates[baseline_name]
        print(f"\n--- Statistical Tests vs Baseline ---")
        print(f"{'Treatment':<30} {'Mean Rate':>10} {'Ratio':>8} {'t-stat':>8} {'p-value':>10} {'Cohen d':>8} {'Sig':>5}")
        print("-" * 85)

        stat_results = {}
        for t in TREATMENT_ORDER:
            if t == baseline_name or t not in treatment_rates:
                continue
            t_rates = treatment_rates[t]
            b_mean = np.mean(baseline_rates)
            t_mean = np.mean(t_rates)
            ratio = t_mean / b_mean if b_mean > 0 else float("inf")

            # Paired t-test (same tasks)
            t_stat, p_val = stats.ttest_rel(t_rates, baseline_rates)
            # Cohen's d
            diff = np.array(t_rates) - np.array(baseline_rates)
            d = np.mean(diff) / np.std(diff, ddof=1) if np.std(diff, ddof=1) > 0 else 0

            sig = "***" if p_val < 0.001 else "**" if p_val < 0.01 else "*" if p_val < 0.05 else "ns"
            print(f"{TREATMENT_SHORT[t]:<30} {t_mean:>9.1%} {ratio:>7.2f}x {t_stat:>8.2f} {p_val:>10.4f} {d:>8.2f} {sig:>5}")

            stat_results[t] = {
                "mean_rate": t_mean,
                "ratio_vs_baseline": ratio,
                "t_stat": t_stat,
                "p_value": p_val,
                "cohens_d": d,
                "significant": p_val < 0.05,
            }

        return treatment_rates, stat_results
    return treatment_rates, {}


def analyze_role_assignment(data):
    """Statistical analysis of role assignment complementarity."""
    results = data["role_assignment"]
    print("\n" + "=" * 70)
    print("EXPERIMENT 2: ROLE ASSIGNMENT (COMPLEMENTARITY)")
    print("=" * 70)

    treatment_rates = {}
    for treatment in TREATMENT_ORDER:
        if treatment not in results:
            continue
        task_results = results[treatment]
        rates = [task_results[tid]["complementarity_rate"] for tid in task_results]
        treatment_rates[treatment] = rates

    # Print per-task results
    print(f"\n{'Task':<20}", end="")
    for t in TREATMENT_ORDER:
        if t in results:
            print(f" {TREATMENT_SHORT[t]:>12}", end="")
    print()
    print("-" * 80)

    task_ids = list(results[TREATMENT_ORDER[0]].keys()) if TREATMENT_ORDER[0] in results else []
    for tid in task_ids:
        print(f"{tid:<20}", end="")
        for t in TREATMENT_ORDER:
            if t in results and tid in results[t]:
                rate = results[t][tid]["complementarity_rate"]
                print(f" {rate:>11.1%}", end="")
        print()

    print(f"\n{'MEAN':<20}", end="")
    for t in TREATMENT_ORDER:
        if t in treatment_rates:
            print(f" {np.mean(treatment_rates[t]):>11.1%}", end="")
    print()

    baseline_name = "No Game (Baseline)"
    stat_results = {}
    if baseline_name in treatment_rates:
        baseline_rates = treatment_rates[baseline_name]
        print(f"\n--- Statistical Tests vs Baseline ---")
        print(f"{'Treatment':<30} {'Mean Rate':>10} {'Ratio':>8} {'t-stat':>8} {'p-value':>10} {'Sig':>5}")
        print("-" * 75)

        for t in TREATMENT_ORDER:
            if t == baseline_name or t not in treatment_rates:
                continue
            t_rates = treatment_rates[t]
            b_mean = np.mean(baseline_rates)
            t_mean = np.mean(t_rates)
            ratio = t_mean / b_mean if b_mean > 0 else float("inf")
            t_stat, p_val = stats.ttest_rel(t_rates, baseline_rates)
            sig = "***" if p_val < 0.001 else "**" if p_val < 0.01 else "*" if p_val < 0.05 else "ns"
            print(f"{TREATMENT_SHORT[t]:<30} {t_mean:>9.1%} {ratio:>7.2f}x {t_stat:>8.2f} {p_val:>10.4f} {sig:>5}")

            stat_results[t] = {
                "mean_rate": t_mean,
                "ratio_vs_baseline": ratio,
                "t_stat": t_stat,
                "p_value": p_val,
            }

    return treatment_rates, stat_results


def analyze_convention(data):
    """Statistical analysis of convention formation speed."""
    results = data["convention"]
    print("\n" + "=" * 70)
    print("EXPERIMENT 3: CONVENTION FORMATION SPEED")
    print("=" * 70)

    print(f"\n{'Treatment':<35} {'Conv. Rate':>10} {'Avg Round':>10} {'Final Acc':>10}")
    print("-" * 70)

    stat_results = {}
    for t in TREATMENT_ORDER:
        if t not in results:
            continue
        r = results[t]
        conv_rate = r["convergence_rate"]
        avg_round = r["avg_convergence_round"]
        final_acc = np.mean(r["accuracy_by_round"][-3:]) if r["accuracy_by_round"] else 0
        avg_str = f"{avg_round:.1f}" if avg_round is not None else "N/A"
        print(f"{TREATMENT_SHORT[t]:<35} {conv_rate:>9.1%} {avg_str:>10} {final_acc:>9.1%}")

        stat_results[t] = {
            "convergence_rate": conv_rate,
            "avg_convergence_round": avg_round,
            "final_accuracy": final_acc,
            "accuracy_by_round": r["accuracy_by_round"],
        }

    return stat_results


# ── Visualizations ────────────────────────────────────────────────────────

def plot_focal_point_comparison(treatment_rates):
    """Bar chart comparing focal point match rates across treatments."""
    fig, ax = plt.subplots(figsize=(10, 6))

    treatments = [t for t in TREATMENT_ORDER if t in treatment_rates]
    means = [np.mean(treatment_rates[t]) for t in treatments]
    stds = [np.std(treatment_rates[t], ddof=1) / np.sqrt(len(treatment_rates[t]))
            for t in treatments]
    labels = [TREATMENT_SHORT[t] for t in treatments]
    colors = [COLORS[t] for t in treatments]

    bars = ax.bar(labels, means, yerr=stds, capsize=5, color=colors, edgecolor="black", linewidth=0.5)

    # Add value labels
    for bar, mean in zip(bars, means):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                f"{mean:.1%}", ha="center", va="bottom", fontsize=10, fontweight="bold")

    # Add 2x baseline line
    if "No Game (Baseline)" in treatment_rates:
        baseline = np.mean(treatment_rates["No Game (Baseline)"])
        ax.axhline(y=baseline * 2, color="red", linestyle="--", linewidth=1.5, label=f"2x Baseline ({baseline*2:.1%})")
        ax.legend(fontsize=10)

    ax.set_ylabel("Match Rate", fontsize=12)
    ax.set_title("Focal Point Coordination: Match Rate by Treatment", fontsize=14, fontweight="bold")
    ax.set_ylim(0, min(1.0, max(means) * 1.5))
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "focal_point_comparison.png", dpi=150)
    plt.close()
    print(f"Saved: {PLOTS_DIR / 'focal_point_comparison.png'}")


def plot_focal_point_by_task(data):
    """Heatmap of match rates by task and treatment."""
    results = data["focal_point"]
    treatments = [t for t in TREATMENT_ORDER if t in results]
    task_ids = list(results[treatments[0]].keys())

    matrix = np.zeros((len(task_ids), len(treatments)))
    for j, t in enumerate(treatments):
        for i, tid in enumerate(task_ids):
            matrix[i, j] = results[t][tid]["match_rate"]

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(
        matrix, annot=True, fmt=".0%", cmap="YlGnBu",
        xticklabels=[TREATMENT_SHORT[t] for t in treatments],
        yticklabels=[tid.replace("fp_", "") for tid in task_ids],
        ax=ax, vmin=0, vmax=1,
    )
    ax.set_title("Focal Point Match Rates by Task and Treatment", fontsize=14, fontweight="bold")
    ax.set_ylabel("Task")
    ax.set_xlabel("Treatment")
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "focal_point_heatmap.png", dpi=150)
    plt.close()
    print(f"Saved: {PLOTS_DIR / 'focal_point_heatmap.png'}")


def plot_role_assignment(treatment_rates):
    """Bar chart for role assignment complementarity."""
    fig, ax = plt.subplots(figsize=(10, 6))

    treatments = [t for t in TREATMENT_ORDER if t in treatment_rates]
    means = [np.mean(treatment_rates[t]) for t in treatments]
    stds = [np.std(treatment_rates[t], ddof=1) / np.sqrt(len(treatment_rates[t]))
            for t in treatments]
    labels = [TREATMENT_SHORT[t] for t in treatments]
    colors = [COLORS[t] for t in treatments]

    bars = ax.bar(labels, means, yerr=stds, capsize=5, color=colors, edgecolor="black", linewidth=0.5)

    for bar, mean in zip(bars, means):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                f"{mean:.1%}", ha="center", va="bottom", fontsize=10, fontweight="bold")

    ax.axhline(y=0.5, color="gray", linestyle=":", linewidth=1, label="Random (50%)")
    ax.legend(fontsize=10)
    ax.set_ylabel("Complementarity Rate", fontsize=12)
    ax.set_title("Role Assignment: Complementarity Rate by Treatment", fontsize=14, fontweight="bold")
    ax.set_ylim(0, 1.0)
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "role_assignment_comparison.png", dpi=150)
    plt.close()
    print(f"Saved: {PLOTS_DIR / 'role_assignment_comparison.png'}")


def plot_convention_curves(conv_results):
    """Learning curves for convention formation."""
    fig, ax = plt.subplots(figsize=(10, 6))

    for t in TREATMENT_ORDER:
        if t not in conv_results or not conv_results[t].get("accuracy_by_round"):
            continue
        curve = conv_results[t]["accuracy_by_round"]
        rounds = list(range(1, len(curve) + 1))
        ax.plot(rounds, curve, marker="o", label=TREATMENT_SHORT[t],
                color=COLORS.get(t, "gray"), linewidth=2, markersize=5)

    ax.axhline(y=1/3, color="gray", linestyle=":", linewidth=1, label="Random (33%)")
    ax.set_xlabel("Round", fontsize=12)
    ax.set_ylabel("Accuracy", fontsize=12)
    ax.set_title("Convention Formation: Accuracy by Round", fontsize=14, fontweight="bold")
    ax.legend(fontsize=9, loc="lower right")
    ax.set_ylim(0, 1.0)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "convention_learning_curves.png", dpi=150)
    plt.close()
    print(f"Saved: {PLOTS_DIR / 'convention_learning_curves.png'}")


def plot_coordination_ratios(fp_stats, role_stats, conv_results):
    """Summary plot showing improvement ratios vs baseline."""
    fig, ax = plt.subplots(figsize=(10, 6))

    treatments = [t for t in TREATMENT_ORDER[2:] if t in fp_stats]  # Skip baseline and trivia
    x = np.arange(len(treatments))
    width = 0.25

    fp_ratios = [fp_stats[t]["ratio_vs_baseline"] for t in treatments]
    role_ratios = [role_stats[t]["ratio_vs_baseline"] for t in treatments if t in role_stats]

    bars1 = ax.bar(x - width, fp_ratios, width, label="Focal Point", color="#3498db", edgecolor="black", linewidth=0.5)
    if len(role_ratios) == len(treatments):
        bars2 = ax.bar(x, role_ratios, width, label="Role Assignment", color="#e67e22", edgecolor="black", linewidth=0.5)

    # Convention improvement
    baseline_conv = conv_results.get("No Game (Baseline)", {}).get("final_accuracy", 0)
    if baseline_conv > 0:
        conv_ratios = []
        for t in treatments:
            if t in conv_results:
                conv_ratios.append(conv_results[t]["final_accuracy"] / baseline_conv)
            else:
                conv_ratios.append(1.0)
        bars3 = ax.bar(x + width, conv_ratios, width, label="Convention", color="#2ecc71", edgecolor="black", linewidth=0.5)

    ax.axhline(y=2.0, color="red", linestyle="--", linewidth=2, label="2x Target")
    ax.axhline(y=1.0, color="gray", linestyle=":", linewidth=1, label="Baseline (1x)")

    ax.set_ylabel("Improvement Ratio vs Baseline", fontsize=12)
    ax.set_title("Coordination Improvement Ratios by Treatment", fontsize=14, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels([TREATMENT_SHORT[t] for t in treatments])
    ax.legend(fontsize=10)
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "coordination_ratios.png", dpi=150)
    plt.close()
    print(f"Saved: {PLOTS_DIR / 'coordination_ratios.png'}")


def plot_response_distribution(data):
    """Show most common responses for key focal point tasks."""
    results = data["focal_point"]
    key_tasks = ["fp_number", "fp_color", "fp_city"]

    fig, axes = plt.subplots(1, len(key_tasks), figsize=(15, 5))

    for ax, tid in zip(axes, key_tasks):
        # Combine responses from AI-Designed treatment
        treatment = "AI-Designed Coordination Game"
        if treatment not in results or tid not in results[treatment]:
            continue
        all_responses = (results[treatment][tid]["responses_a"] +
                        results[treatment][tid]["responses_b"])
        # Normalize and count
        from collections import Counter
        normalized = [normalize_response(r) for r in all_responses]
        counts = Counter(normalized).most_common(8)
        if counts:
            labels, values = zip(*counts)
            ax.barh(range(len(labels)), values, color="#2ecc71")
            ax.set_yticks(range(len(labels)))
            ax.set_yticklabels(labels, fontsize=9)
            ax.invert_yaxis()
            ax.set_xlabel("Count")
            ax.set_title(tid.replace("fp_", "").replace("_", " ").title(), fontsize=12, fontweight="bold")

    plt.suptitle("Response Distribution (AI-Designed Game Treatment)", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "response_distributions.png", dpi=150)
    plt.close()
    print(f"Saved: {PLOTS_DIR / 'response_distributions.png'}")


def normalize_response(resp):
    """Same normalization as in run_experiments.py."""
    if not resp:
        return ""
    resp = resp.lower().strip().rstrip(".")
    resp = resp.split("\n")[0].strip()
    for prefix in ["i choose ", "i pick ", "my choice is ", "i'd pick ", "i would pick ", "i'll go with "]:
        if resp.startswith(prefix):
            resp = resp[len(prefix):]
    resp = resp.strip().strip("'\"")
    replacements = {
        "twelve": "12", "noon": "12:00 pm", "12 pm": "12:00 pm", "12:00": "12:00 pm",
        "new york city": "new york", "nyc": "new york",
    }
    for k, v in replacements.items():
        if resp == k:
            resp = v
            break
    return resp


# ── Main ──────────────────────────────────────────────────────────────────

def main():
    data = load_results()
    print(f"Loaded results: {data['config']['model']}, {data['config']['n_pairs']} pairs")

    # Analysis
    fp_rates, fp_stats = analyze_focal_points(data)
    role_rates, role_stats = analyze_role_assignment(data)
    conv_results = analyze_convention(data)

    # Visualizations
    print("\n--- Generating Visualizations ---")
    plot_focal_point_comparison(fp_rates)
    plot_focal_point_by_task(data)
    plot_role_assignment(role_rates)
    plot_convention_curves(conv_results)
    plot_coordination_ratios(fp_stats, role_stats, conv_results)
    plot_response_distribution(data)

    # Save analysis summary
    def make_serializable(obj):
        if isinstance(obj, (np.integer,)): return int(obj)
        if isinstance(obj, (np.floating, np.float64)): return float(obj)
        if isinstance(obj, np.ndarray): return obj.tolist()
        if isinstance(obj, (np.bool_,)): return bool(obj)
        if isinstance(obj, dict): return {k: make_serializable(v) for k, v in obj.items()}
        if isinstance(obj, (list, tuple)): return [make_serializable(v) for v in obj]
        return obj

    summary = make_serializable({
        "focal_point_stats": fp_stats,
        "role_assignment_stats": role_stats,
        "convention_stats": {k: {kk: vv for kk, vv in v.items() if kk != "accuracy_by_round"}
                           for k, v in conv_results.items()},
    })
    with open(RESULTS_DIR / "analysis_summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\nAnalysis saved to {RESULTS_DIR / 'analysis_summary.json'}")


if __name__ == "__main__":
    main()
