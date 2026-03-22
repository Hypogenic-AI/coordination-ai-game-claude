# Cloned Repositories

## Repo 1: Overcooked-AI
- **URL**: https://github.com/HumanCompatibleAI/overcooked_ai
- **Purpose**: Primary benchmark environment for cooperative human-AI coordination
- **Location**: code/overcooked_ai/
- **Key files**:
  - `src/overcooked_ai_py/mdp/overcooked_mdp.py` - Core game MDP
  - `src/overcooked_ai_py/mdp/overcooked_env.py` - Gymnasium environment wrapper
  - `src/human_aware_rl/static/human_data/` - Human gameplay data (2019 + 2020)
  - `Overcooked Tutorial.ipynb` - Getting started notebook
- **Install**: `pip install overcooked-ai`
- **Notes**: 5+ predefined layouts with varying coordination difficulty. Supports human-AI experiments via web interface. Used by 10+ papers on zero-shot coordination. Contains real human-human gameplay data.

## Repo 2: AI-GBS (Group Binary Search)
- **URL**: https://github.com/riedlc/AI-GBS
- **Purpose**: Emergent coordination experiments with multi-agent LLMs (ICLR 2026)
- **Location**: code/ai-gbs/
- **Key files**: Check README for experiment scripts and data
- **Notes**: Implements the group guessing game from Riedl (2026). Provides information-theoretic framework (PID, TDMI) for measuring emergent coordination. Includes persona generation and ToM prompting code. Results with GPT-4.1, Llama, Gemini, Qwen3.

## Repo 3: Hanabi Learning Environment
- **URL**: https://github.com/deepmind/hanabi-learning-environment
- **Purpose**: Cooperative card game requiring convention formation and Theory of Mind
- **Location**: code/hanabi/
- **Install**: `pip install hanabi-learning-environment`
- **Notes**: DeepMind's implementation of Hanabi. C++ core with Python bindings. 2-5 player cooperative game. Inherently requires developing shared conventions and perspective-taking.

## Repo 4: OpenSpiel
- **URL**: https://github.com/google-deepmind/open_spiel
- **Purpose**: Game theory library with coordination games
- **Location**: code/open_spiel/
- **Key files**:
  - `open_spiel/games/lewis_signaling/` - Lewis signaling game (convention formation)
  - `open_spiel/games/matrix_games/` - Coordination game, stag hunt, battle of sexes
- **Install**: `pip install open_spiel`
- **Notes**: Comprehensive game theory library. Lewis signaling game is directly relevant to convention formation. Matrix coordination game models pure focal point selection. Stag hunt models cooperation vs. safety trade-offs.

## Repo 5: PettingZoo
- **URL**: https://github.com/Farama-Foundation/PettingZoo
- **Purpose**: Standardized multi-agent environment library
- **Location**: code/pettingzoo/
- **Install**: `pip install pettingzoo`
- **Notes**: 50+ environments across categories. Includes cooperative games. Standardized API compatible with Gymnasium. Can be used to design custom coordination game environments for experiments.

## Additional Notable Repositories (not cloned)

- **google-deepmind/concordia** (1,289 stars) - LLM-based generative social simulation; used in NeurIPS 2024 Cooperative AI contest. URL: https://github.com/google-deepmind/concordia
- **google-deepmind/meltingpot** (805 stars) - Suite of multi-agent cooperation/social dilemma test scenarios. URL: https://github.com/google-deepmind/meltingpot
- **oTree-org/oTree** (516 stars) - Python framework for multiplayer decision games and behavioral experiments (web-based). URL: https://github.com/oTree-org/oTree
- **Stanford-ILIAD/PantheonRL** (158 stars) - Multi-agent RL with cross-play and ad-hoc coordination support. URL: https://github.com/Stanford-ILIAD/PantheonRL
- **liyang619/COLE-Platform** (39 stars) - Overcooked human-AI experiment platform from Li et al. (2023). URL: https://github.com/liyang619/COLE-Platform
- **ZSC-Eval** (ICLR 2025) - First evaluation toolkit for zero-shot coordination. Paper: https://arxiv.org/abs/2310.05208
