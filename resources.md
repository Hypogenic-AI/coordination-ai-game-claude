# Resources Catalog

## Summary
This document catalogs all resources gathered for the "Coordination Enhancing Video Game" research project. The hypothesis is that a video game can be designed (with AI) such that two strangers who have both played it can coordinate twice as well in unrelated environments.

---

## Papers
Total papers downloaded: 27

| # | Title | Authors | Year | File | Key Info |
|---|-------|---------|------|------|----------|
| 1 | On the Utility of Learning about Humans for Human-AI Coordination | Carroll et al. | 2019 | papers/carroll2019_overcooked_ai.pdf | Overcooked-AI benchmark; conventions in self-play |
| 2 | Emergent Coordination in Multi-Agent Language Models | Riedl | 2026 | papers/riedl2025_emergent_coordination_llm.pdf | Info-theoretic coordination measurement; Schelling points in LLMs |
| 3 | Other-Play for Zero-Shot Coordination | Hu et al. | 2020 | papers/hu2020_other_play_zsc.pdf | Breaking arbitrary conventions for transfer |
| 4 | The Hanabi Challenge | Bard et al. | 2020 | papers/bard2019_hanabi_challenge.pdf | Cooperative game requiring convention formation + ToM |
| 5 | Who Needs to Know? Minimal Knowledge for Coordination | Lauffer et al. | 2023 | papers/lauffer2023_minimal_knowledge_coordination.pdf | Formal coordination complexity framework |
| 6 | Tackling Cooperative Incompatibility for ZSC | Li et al. | 2024 | papers/li2023_cooperative_incompatibility_zsc.pdf | COLE framework; 130-person human study |
| 7 | Cooperative Open-ended Learning for ZSC | Li et al. | 2023 | papers/li2023_cooperative_openended_zsc.pdf | Open-ended ZSC learning |
| 8 | PECAN: Context-Aware ZSC | Lou et al. | 2023 | papers/lou2023_pecan_zsc_human_ai.pdf | Context-aware coordination |
| 9 | MEP for Zero-Shot Coordination | Zhao et al. | 2021 | papers/zhao2021_mep_zsc.pdf | Diverse populations for robust coordination |
| 10 | Efficient RL for ZSC in Evolving Games | Hui et al. | 2025 | papers/hui2025_zsc_evolving_games.pdf | ZSC in complex games |
| 11 | ZSC in Ad Hoc Teams | Nigam et al. | 2025 | papers/nigam2025_zsc_adhoc_teams.pdf | Ad hoc teamwork |
| 12 | Learning to Communicate with Deep MARL | Foerster et al. | 2016 | papers/foerster2016_learning_communicate.pdf | Emergent communication |
| 13 | Emergence of Linguistic Conventions in MARL | Lipowska & Lipowski | 2018 | papers/lipowska2018_linguistic_conventions_marl.pdf | Convention formation dynamics |
| 14 | Zero-Shot Emergent Communication | Bullard et al. | 2020 | papers/bullard2020_zeroshot_emergent_communication.pdf | Communication transfer |
| 15 | Networked MARL with Emergent Communication | Gupta et al. | 2020 | papers/gupta2020_networked_marl_communication.pdf | Communication in networks |
| 16 | DASH: Shared Mental Model | Wan et al. | 2025 | papers/wan2025_dash_shared_mental_model.pdf | Shared mental models |
| 17 | Human-AI Teaming Review | Lou et al. | 2025 | papers/lou2025_human_ai_teaming_review.pdf | Comprehensive HAI review |
| 18 | AI Spatial Collaborators | Fernandez et al. | 2025 | papers/fernandez2025_ai_spatial_collaborators.pdf | AI in collaborative spaces |
| 19 | ProAgent: Proactive Cooperative Agents | Zhang et al. | 2023 | papers/zhang2023_proagent_cooperative.pdf | LLM cooperative agents |
| 20 | LLM Hierarchical Coordination | Liu et al. | 2023 | papers/liu2023_llm_hierarchical_coordination.pdf | Real-time LLM coordination |
| 21 | Cooperating with Humans via Generative Agents | Liang et al. | 2024 | papers/liang2024_cooperate_humans_generative.pdf | Generative partner models |
| 22 | Human-AI Adversarial Training | Chaudhary et al. | 2025 | papers/chaudhary2025_human_ai_adversarial.pdf | Robust human-AI coordination |
| 23 | Few-shot Coordination in Hanabi | Nekoei et al. | 2023 | papers/nekoei2023_fewshot_hanabi.pdf | Few-shot coordination |
| 24 | Ad Hoc Teamwork with Cooperative Game Theory | Wang et al. | 2024 | papers/wang2024_adhoc_teamwork_cooperative.pdf | Cooperative game theory |
| 25 | Emergent Complexity via Multi-Agent Competition | Bansal et al. | 2017 | papers/bansal2017_emergent_complexity.pdf | Emergent complex behavior |
| 26 | Emergent Tool Use from Multi-Agent Autocurricula | Baker et al. | 2019 | papers/baker2019_emergent_tool_use.pdf | Emergent coordination & tools |
| 27 | Theory of Mind for Cooperative Communication | Oguntola et al. | 2021 | papers/oguntola2021_theory_mind_cooperative.pdf | ToM in cooperation |

See papers/README.md for detailed descriptions.

---

## Datasets
Total datasets/environments documented: 6

| Name | Source | Type | Task | Location | Notes |
|------|--------|------|------|----------|-------|
| Overcooked Human Data | HumanCompatibleAI | Gameplay trajectories | Cooperative cooking | code/overcooked_ai/src/human_aware_rl/static/human_data/ | ~160MB, 2019+2020 collections |
| Overcooked-AI Env | HumanCompatibleAI | Game environment | Cooperative cooking | `pip install overcooked-ai` | 5+ layouts, standard ZSC benchmark |
| Hanabi Env | DeepMind | Game environment | Cooperative cards | code/hanabi/ | Convention formation + ToM |
| OpenSpiel Games | DeepMind | Game library | Coordination games | code/open_spiel/ | Lewis signaling, coordination, stag hunt |
| PettingZoo | Farama Foundation | Multi-agent envs | Various cooperative | code/pettingzoo/ | 50+ environments |
| AI-GBS Data | Riedl (ICLR 2026) | Experiment data | Group guessing | code/ai-gbs/ | 600 LLM coordination experiments |

See datasets/README.md for detailed descriptions and download instructions.

---

## Code Repositories
Total repositories cloned: 5

| Name | URL | Purpose | Location | Notes |
|------|-----|---------|----------|-------|
| Overcooked-AI | github.com/HumanCompatibleAI/overcooked_ai | Cooperative game benchmark | code/overcooked_ai/ | Primary testbed; has human data |
| AI-GBS | github.com/riedlc/AI-GBS | Emergent coordination measurement | code/ai-gbs/ | Info-theoretic framework |
| Hanabi | github.com/deepmind/hanabi-learning-environment | Convention formation game | code/hanabi/ | DeepMind challenge problem |
| OpenSpiel | github.com/google-deepmind/open_spiel | Game theory library | code/open_spiel/ | Lewis signaling, coordination |
| PettingZoo | github.com/Farama-Foundation/PettingZoo | Multi-agent environments | code/pettingzoo/ | Standardized API |

See code/README.md for detailed descriptions.

---

## Resource Gathering Notes

### Search Strategy
1. **arXiv API**: Searched 7 query combinations covering coordination games, cooperative games, emergent communication, shared mental models, and convention formation. Found 38 unique papers.
2. **Semantic Scholar API**: Searched 8 query combinations for focal points, cooperative games, convention formation, and tacit coordination.
3. **Web search**: Searched for Schelling focal points, cooperative game training, AI game design, shared mental models, prosocial gaming, and reinforcement learning for cooperation.
4. **Paper-finder**: Searched with diligent mode across multiple query formulations.
5. **GitHub**: Searched for cooperative game environments, multi-agent coordination, signaling games, and procedural generation.

### Selection Criteria
Papers were selected based on:
- Direct relevance to coordination between strangers (zero-shot coordination)
- Empirical evidence of coordination skill transfer
- Game environments that teach coordination
- AI methods for game design or coordination training
- Formal frameworks for measuring coordination quality

### Key Findings
1. **Zero-shot coordination** is a well-studied problem with strong benchmarks (Overcooked, Hanabi)
2. **Convention formation** is the key mechanism by which game experience could transfer coordination ability
3. **Theory of Mind** and **focal points** are trainable coordination skills
4. **Information-theoretic measures** (PID, TDMI) provide rigorous metrics for coordination quality
5. **Cooperative gaming does improve team performance** (Keith et al. 2018, 2021 RCT)
6. **Gap**: No existing work studies whether individual game training transfers coordination to unrelated tasks with new partners

### Challenges Encountered
- Limited research specifically on games designed to enhance general coordination ability
- Most ZSC research evaluates within-game transfer only
- Schelling focal point research is primarily pre-digital (1960s-1990s), with limited modern computational work
- Keith et al. studies used co-play, not separate individual training

---

## Recommendations for Experiment Design

### 1. Primary Dataset(s)
- **Overcooked-AI environment** for cooperative game experiments
- **OpenSpiel coordination/signaling games** for focal point evaluation tasks
- **Overcooked human data** as baseline for human coordination patterns

### 2. Baseline Methods
- Self-play trained agents (convention arbitrariness baseline)
- FCP/MEP trained agents (population diversity baselines)
- Untrained human control group
- Human group trained on unrelated games

### 3. Evaluation Metrics
- Coordination improvement ratio (primary metric)
- Convention formation speed
- Focal point accuracy (Schelling-type tasks)
- Information-theoretic synergy (Riedl's PID framework)
- Subjective coordination quality

### 4. Code to Adapt/Reuse
- **Overcooked-AI**: Game environment and human experiment platform
- **AI-GBS**: Information-theoretic coordination measurement framework
- **OpenSpiel**: Lewis signaling and coordination games for evaluation
- **PettingZoo**: Custom environment design framework

### 5. Experimental Design Suggestion
```
Phase 1: AI Game Design
├── Use LLMs to generate candidate coordination game variants
├── Evaluate games on coordination-enhancing properties
└── Select top games via automated metrics

Phase 2: Individual Training
├── Treatment group: Play designed coordination game (alone/with AI)
├── Control 1: No game training
├── Control 2: Play non-coordination game
└── Each participant trains independently

Phase 3: Evaluation
├── Pair trained participants with strangers (both trained)
├── Pair control participants with strangers
├── Test on multiple unrelated coordination tasks:
│   ├── Schelling focal point selection
│   ├── Cooperative task (simplified Overcooked)
│   ├── Tacit coordination (no communication)
│   └── Lewis signaling game
└── Measure: coordination ratio, convention speed, synergy

Phase 4: Analysis
├── Compare trained vs. control coordination scores
├── Test "twice as well" hypothesis (2x improvement)
├── Information-theoretic decomposition (PID/TDMI)
└── Identify which coordination skills transferred
```
