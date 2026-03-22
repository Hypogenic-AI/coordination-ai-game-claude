# Coordination-Enhancing Video Game Research

Can a video game be designed such that two strangers who have both played it coordinate 2x better in unrelated tasks? Can AI design such a game?

## Key Findings

- **Game training improves coordination up to 2.9x** on specific tasks (e.g., movie coordination: 34% to 100%) and **1.5x on average** across hard coordination tasks
- **AI-Designed multi-skill game achieves 1.98x improvement on role assignment** (50.5% to 100%), nearly meeting the 2x target
- **Single-skill games have tradeoffs**: Focal point training helps convergence but *hurts* role differentiation (0% complementarity on some tasks)
- **Multi-skill training is key**: The game must teach focal point identification, perspective-taking, role differentiation, AND convention formation
- **Convention formation speed improves 24%** with game training (1.6 vs 2.1 rounds to convergence)

## Method

We used GPT-4.1 agents as proxies for human players across 5 conditions (no game, irrelevant game, 3 coordination games) tested on 22 focal point tasks, 9 role assignment tasks, and a Lewis signaling convention game. ~12,000 real API calls total.

## How to Reproduce

```bash
# Setup
cd /workspaces/coordination-ai-game-claude
source .venv/bin/activate

# Run experiments
cd src
python run_experiments.py        # Standard tasks (~5000 API calls)
python run_hard_experiments.py   # Hard tasks (~4000 API calls)

# Analysis
python analyze_results.py        # Standard task analysis + plots
python analyze_hard_results.py   # Hard task analysis + plots
```

Requires: `OPENAI_API_KEY` environment variable.

## File Structure

```
REPORT.md                        # Full research report with results
README.md                        # This file
planning.md                      # Research plan
literature_review.md             # Pre-gathered literature review
resources.md                     # Resource catalog
src/
  coordination_games.py          # Game definitions and task definitions
  hard_coordination_tasks.py     # Harder task battery
  run_experiments.py             # Main experiment runner
  run_hard_experiments.py        # Hard tasks experiment runner
  analyze_results.py             # Standard task analysis
  analyze_hard_results.py        # Hard task analysis
results/
  experiment_results.json        # Raw results (standard tasks)
  hard_experiment_results.json   # Raw results (hard tasks)
  analysis_summary.json          # Statistical summary
  plots/                         # All visualizations
papers/                          # 27 downloaded research papers
code/                            # 5 cloned repositories
datasets/                        # Dataset documentation
```

## Full Report

See [REPORT.md](REPORT.md) for comprehensive results, analysis, and discussion.
