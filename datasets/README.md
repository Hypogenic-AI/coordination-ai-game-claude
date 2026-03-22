# Datasets for Coordination Enhancing Video Game Research

This directory contains datasets for the research project. Data files are NOT
committed to git due to size. Follow the download instructions below.

## Dataset 1: Overcooked-AI Human Gameplay Data

### Overview
- **Source**: Bundled with [overcooked_ai](https://github.com/HumanCompatibleAI/overcooked_ai) repository
- **Size**: ~160MB total (2019 + 2020 collections)
- **Format**: Python pickle files (requires pandas)
- **Task**: Human-human cooperative coordination in Overcooked game
- **Splits**:
  - 2019: train (48MB), test (15MB), all (62MB)
  - 2020: train (70MB), test (28MB), all (98MB)
- **License**: MIT (same as overcooked_ai)

### Description
Human-human gameplay trajectories collected via web-based Overcooked game interface.
Contains state-action sequences, rewards, and coordination metrics for pairs of
human players cooperating to cook and deliver soups in various kitchen layouts.

### Download Instructions
Data is already available in the cloned repo at:
```
code/overcooked_ai/src/human_aware_rl/static/human_data/cleaned/
```

To install and use:
```python
pip install overcooked-ai pandas
import pandas as pd
import pickle

with open("code/overcooked_ai/src/human_aware_rl/static/human_data/cleaned/2019_hh_trials_all.pickle", "rb") as f:
    data = pickle.load(f)
```

### Why Relevant
- Real human-human coordination data for cooperative game tasks
- Shows how human pairs develop coordination strategies over time
- Can be used to study coordination patterns that emerge during gameplay
- Benchmark for human-AI coordination algorithms

---

## Dataset 2: Overcooked-AI Game Environments

### Overview
- **Source**: [overcooked_ai](https://github.com/HumanCompatibleAI/overcooked_ai) Python package
- **Type**: Programmatic game environment (not static data)
- **Task**: Two-player cooperative cooking game
- **Layouts**: 5+ predefined layouts, supports custom layouts

### Download Instructions
```bash
pip install overcooked-ai
```

```python
from overcooked_ai_py.mdp.overcooked_mdp import OvercookedGridworld
from overcooked_ai_py.mdp.overcooked_env import OvercookedEnv

mdp = OvercookedGridworld.from_layout_name("cramped_room")
env = OvercookedEnv.from_mdp(mdp, horizon=400)
```

### Why Relevant
- Benchmark cooperative game environment requiring real-time coordination
- Multiple layouts with varying coordination difficulty
- Used by 10+ papers on zero-shot coordination
- Supports human-AI experiments via web interface

---

## Dataset 3: Hanabi Learning Environment

### Overview
- **Source**: [hanabi-learning-environment](https://github.com/deepmind/hanabi-learning-environment) by DeepMind
- **Type**: Programmatic game environment
- **Task**: Cooperative card game requiring implicit communication
- **Players**: 2-5 players

### Download Instructions
```bash
pip install hanabi-learning-environment
```

### Why Relevant
- Requires convention formation and Theory of Mind
- "Challenge problem" for cooperative AI (Bard et al. 2019)
- Tests ability to develop shared understanding without explicit communication
- Directly tests coordination skills transferable across partners

---

## Dataset 4: OpenSpiel Coordination Games

### Overview
- **Source**: [OpenSpiel](https://github.com/google-deepmind/open_spiel) by DeepMind
- **Type**: Game theory library with coordination games
- **Games**: Lewis signaling, coordination game, stag hunt, battle of the sexes
- **Format**: C++ with Python bindings

### Download Instructions
```bash
pip install open_spiel
```

```python
import pyspiel

# Lewis signaling game
game = pyspiel.load_game("lewis_signaling")

# Pure coordination game
game = pyspiel.load_game("matrix_coordination")
```

### Why Relevant
- Lewis signaling game: seminal model for convention formation
- Matrix coordination games: focal point selection
- Stag hunt: cooperation vs. safety trade-off
- Formal game-theoretic framework for studying coordination

---

## Dataset 5: PettingZoo Multi-Agent Environments

### Overview
- **Source**: [PettingZoo](https://github.com/Farama-Foundation/PettingZoo) by Farama Foundation
- **Type**: Multi-agent environment library
- **Environments**: 50+ environments across categories (classic, Atari, butterfly, MPE, SISL)
- **Format**: Python API (Gymnasium-compatible)

### Download Instructions
```bash
pip install pettingzoo
```

### Why Relevant
- Standardized multi-agent environment API
- Contains cooperative games (e.g., cooperative Pong, pursuit)
- Can be used to design custom coordination game environments
- Well-maintained with active community

---

## Dataset 6: AI-GBS Group Binary Search Data

### Overview
- **Source**: [AI-GBS](https://github.com/riedlc/AI-GBS) by Riedl (ICLR 2026)
- **Type**: Experimental data from multi-agent LLM coordination
- **Task**: Group guessing game (group binary search)
- **Conditions**: Plain, Persona, Persona+ToM
- **Scale**: 600 experiments (200 per condition), GPT-4.1

### Download Instructions
Data and code available at:
```
code/ai-gbs/
```

### Why Relevant
- Directly demonstrates emergent coordination in multi-agent systems
- Shows how prompting (personas + ToM) steers coordination
- Information-theoretic framework for measuring coordination quality
- Demonstrates "Schelling point" convergence in AI agents

---

## Notes

### Data for Coordination Measurement
For measuring coordination improvement (the "twice as well" claim in our hypothesis),
we need to establish baselines and metrics. Key metrics from the literature include:
- **Episode reward** (Overcooked): joint task completion score
- **Zero-shot coordination score**: performance when paired with unseen partners
- **Coordination coefficient**: mutual information between agent actions
- **Convention alignment**: degree to which partners converge on shared conventions
- **Focal point accuracy**: success rate in pure coordination games (Schelling tasks)
