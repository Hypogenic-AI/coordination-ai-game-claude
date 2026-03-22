# Literature Review: Coordination Enhancing Video Game

## Research Area Overview

This literature review examines research relevant to the hypothesis: *"There exists a video game such that if two people, who have never met, have both played it, they can on average coordinate in another unrelated environment twice as well; AI can be used to design such a game."*

The hypothesis spans several research areas: (1) Schelling focal points and tacit coordination, (2) zero-shot coordination in cooperative games, (3) emergent communication and convention formation, (4) shared mental models and team coordination, (5) serious games for coordination training, and (6) AI-driven game design. We synthesize findings from 31 downloaded papers and additional references.

---

## Key Papers

### 1. Carroll et al. (2019) - "On the Utility of Learning about Humans for Human-AI Coordination"
- **Authors**: Micah Carroll, Rohin Shah, Mark K. Ho, Thomas L. Griffiths, Sanjit A. Seshia, Pieter Abbeel, Anca Dragan
- **Venue**: NeurIPS 2019
- **Key Contribution**: Introduces the Overcooked-AI benchmark environment for human-AI cooperative task performance. Shows that self-play training fails for human-AI coordination; learning from human data via behavioral cloning (BC) and combining BC with RL improves coordination.
- **Methodology**: Two-player cooperative cooking game (Overcooked). Players must coordinate to cook soups (place ingredients, wait, deliver). 5 layouts with varying coordination difficulty. Trained agents via: self-play (SP), behavioral cloning (BC), and population-based training.
- **Datasets**: Human-human gameplay data (2019 collection, ~62MB). Web-based experiment platform.
- **Results**: Self-play agents develop arbitrary conventions that humans cannot follow. Human-aware agents (BC+RL) achieve significantly better coordination with real humans. Layout design affects coordination difficulty.
- **Code**: https://github.com/HumanCompatibleAI/overcooked_ai
- **Relevance**: Establishes that shared game experience creates coordination conventions. The Overcooked environment is ideal for testing whether game training transfers coordination skills.

### 2. Riedl (2026) - "Emergent Coordination in Multi-Agent Language Models"
- **Authors**: Christoph Riedl
- **Venue**: ICLR 2026
- **Key Contribution**: Introduces information-theoretic framework to measure emergent coordination in multi-agent systems. Shows that prompting (personas + Theory of Mind) steers agents from mere aggregates to higher-order collectives with goal-directed complementarity.
- **Methodology**: Group binary search game (guessing game). N=10 agents guess integers whose sum must match a target. Only group-level "too high/too low" feedback. Three conditions: Plain, Persona, Persona+ToM. 600 experiments with GPT-4.1, replicated across Llama, Gemini, Qwen3.
- **Key Finding**: ToM prompt creates "Schelling point" convergence - agents develop differentiated roles through mutual predictive modeling. Performance requires both redundancy (goal alignment) AND synergy (complementary contributions).
- **Metrics**: Partial information decomposition (PID), time-delayed mutual information (TDMI), emergence capacity, practical criterion, coalition test (I3, G3).
- **Code**: https://github.com/riedlc/AI-GBS
- **Relevance**: **Directly supports our hypothesis.** Demonstrates that game-like tasks can induce emergent coordination, and that this coordination can be steered via design choices (personas, ToM prompting). The information-theoretic framework provides rigorous metrics for measuring coordination quality.

### 3. Hu et al. (2020) - "Other-Play for Zero-Shot Coordination"
- **Authors**: Hengyuan Hu, Adam Lerer, Alex Peysakhovich, Jakob Foerster
- **Venue**: ICML 2020
- **Key Contribution**: Proposes "Other-Play" (OP) algorithm for zero-shot coordination. Key insight: conventions that arise in self-play are arbitrary and prevent coordination with new partners. OP augments self-play by considering equivalent but symmetry-broken versions of the co-player's policy.
- **Methodology**: Leverages game symmetries to break arbitrary conventions during training. Tested on lever coordination game and Hanabi.
- **Results**: OP agents coordinate significantly better with novel partners than self-play agents. Achieves near-optimal ZSC in the lever game and strong Hanabi performance.
- **Relevance**: Shows that breaking arbitrary conventions during training produces more transferable coordination skills. Key insight for game design: games that expose players to diverse conventions may build more transferable coordination abilities.

### 4. Bard et al. (2019) - "The Hanabi Challenge: A New Frontier for AI Research"
- **Authors**: Nolan Bard, Jakob N. Foerster, Sarath Chandar, et al.
- **Venue**: Artificial Intelligence, 2020
- **Key Contribution**: Proposes Hanabi as a challenge problem requiring coordination, communication through action (no explicit communication), Theory of Mind, and convention formation.
- **Game Design**: Cooperative card game. Players see others' cards but not their own. Must give hints and play cards to build ordered stacks. Requires developing shared conventions about what hints mean.
- **Key Insight**: Hanabi inherently teaches coordination because success requires developing shared mental models and conventions. The game structure forces players to think about what others know and intend.
- **Code**: https://github.com/deepmind/hanabi-learning-environment
- **Relevance**: Hanabi is a strong candidate for a "coordination enhancing game" because it naturally develops Theory of Mind, convention formation, and perspective-taking skills.

### 5. Lauffer et al. (2023) - "Who Needs to Know? Minimal Knowledge for Optimal Coordination"
- **Authors**: Niklas Lauffer, Ameesh Shah, Micah Carroll, Michael Dennis, Stuart Russell
- **Key Contribution**: Formalizes what information agents need to optimally coordinate. Introduces "coordination complexity" framework showing that some games require knowing your partner's type while others don't.
- **Methodology**: Information-theoretic analysis of Dec-POMDPs. Defines minimal sufficient statistics for coordination.
- **Key Finding**: In many coordination tasks, knowing a small amount about your partner enables near-optimal coordination. This suggests that games could teach players to efficiently communicate coordination-relevant information.
- **Relevance**: Provides formal framework for what coordination knowledge a game should teach. A well-designed game would help players learn to identify and communicate the minimal information needed for coordination.

### 6. Li et al. (2023) - "Tackling Cooperative Incompatibility for Zero-Shot Human-AI Coordination"
- **Authors**: Yang Li, Shao Zhang, Jichen Sun, Wenhao Zhang, Yali Du, Ying Wen, Xinbing Wang, Wei Pan
- **Venue**: JMLR 2024
- **Key Contribution**: Introduces COLE (Cooperative Open-ended LEarning) framework using graph theory to evaluate cooperative capacity. Addresses "cooperative incompatibility" where agents fail to coordinate with some unseen partners.
- **Methodology**: Graph-form games (GFGs) and preference GFGs. COLE iteratively generates strategies that approximate best responses. Tested in Overcooked with 130 human participants.
- **Results**: COLE outperforms state-of-the-art methods (MEP, FCP, LIPO) for human-AI coordination on subjective preference metrics and objective performance.
- **Code**: https://sites.google.com/view/cole-2023
- **Relevance**: Shows that population diversity in training leads to more robust coordination. A game that exposes players to diverse partners would build more transferable coordination skills.

### 7. Lipowska & Lipowski (2018) - "Emergence of Linguistic Conventions in Multi-Agent Reinforcement Learning"
- **Authors**: Dorota Lipowska, Adam Lipowski
- **Key Contribution**: Studies how signaling conventions emerge in multi-agent RL, connecting to Lewis signaling games and the evolution of language/coordination norms.
- **Methodology**: Multi-agent naming game with RL. Agents develop shared vocabulary through interaction.
- **Key Finding**: Conventions emerge reliably when agents have sufficient interaction and learning capacity. Convention formation follows predictable dynamics with initial exploration, then convergence.
- **Relevance**: Convention formation is the mechanism by which game experience could transfer coordination ability. If a game teaches players to form conventions quickly, this skill transfers.

### 8. Zhao et al. (2021) - "Maximum Entropy Population-Based Training for Zero-Shot Human-AI Coordination"
- **Authors**: Rui Zhao, Jinming Song, et al.
- **Key Contribution**: MEP algorithm: trains agents to coordinate with maximally diverse populations, improving zero-shot coordination.
- **Relevance**: Demonstrates that exposure to diverse coordination strategies during training improves transferability.

### 9. Foerster et al. (2016) - "Learning to Communicate with Deep Multi-Agent Reinforcement Learning"
- **Authors**: Jakob N. Foerster, Yannis M. Assael, Nando de Freitas, Shimon Whiteson
- **Key Contribution**: Pioneering work on emergent communication in deep MARL. Agents develop communication protocols to solve cooperative tasks.
- **Relevance**: Shows that communication protocols can emerge from shared game experience, foundational for understanding how games could teach coordination.

### 10. Bullard et al. (2020) - "Exploring Zero-Shot Emergent Communication in Embodied Multi-Agent Populations"
- **Key Contribution**: Studies whether emergent communication protocols transfer across agents in zero-shot settings.
- **Key Finding**: Communication protocols are often brittle and don't transfer well between agents, highlighting the challenge of creating transferable coordination skills.
- **Relevance**: Identifies a key challenge: coordination skills learned in one context may not transfer. Game design must specifically target transferable coordination primitives.

### 11. Keith et al. (2018, 2021) - "Team Video Gaming for Team Building" / "Team Building Through Team Video Games: RCT"
- **Authors**: Mark J. Keith, Greg Anderson, James E. Gaskin, Douglas L. Dean
- **Key Contribution**: Randomized controlled trial showing that cooperative video game play improves team cohesion, trust, and communication.
- **Key Finding**: Teams that played cooperative video games together showed significantly improved subsequent team performance on non-game tasks compared to control groups.
- **Relevance**: **Directly supports our hypothesis.** Empirical evidence that cooperative gaming transfers to improved coordination in other tasks. However, these studies used co-play (together), not separate play followed by coordination.

### 12. Zhang et al. (2023) - "ProAgent: Building Proactive Cooperative Agents with Large Language Models"
- **Key Contribution**: LLM-based agents that proactively anticipate partner needs in Overcooked, achieving state-of-the-art zero-shot human-AI coordination.
- **Relevance**: Shows LLMs can be used to create cooperative agents, relevant to AI-designed game components.

### 13. Dafoe et al. (2020) - "Open Problems in Cooperative AI"
- **Authors**: Dafoe, Hughes, Bachrach, et al.
- **Venue**: Nature Machine Intelligence
- **Key Contribution**: Defines the Cooperative AI research agenda, including coordination between humans and machines, convention formation, and the role of common knowledge.
- **Relevance**: Frames our hypothesis within a broader research program. Identifies coordination with strangers as a key open problem.

### 14. Mirsky et al. (2022) - "A Survey of Ad Hoc Teamwork Research"
- **Key Contribution**: Comprehensive survey of coordination with new teammates without prior training—the exact "stranger coordination" problem.
- **Relevance**: Provides taxonomy of approaches and evaluation methods for ad hoc teamwork.

### 15. Greitemeyer & Mugge (2014) - Meta-analysis of Prosocial Game Effects
- **Key Contribution**: Meta-analysis of 98 studies (N=36,965) showing prosocial games causally increase cooperation (β=.49 for helping, β=.18 for cooperation).
- **Relevance**: Strong causal evidence that games can change cooperative behavior, supporting the hypothesis that game experience transfers to real-world coordination.

### 16. Mehta, Starmer & Sugden (1994) - "Focal Points in Pure Coordination Games"
- **Key Contribution**: Foundational experimental evidence on Schelling focal points. Coordination rates approximately double when participants actively try to match vs. random selection.
- **Relevance**: Establishes that focal point identification is a measurable, trainable coordination skill. The "twice as well" target in our hypothesis aligns with observed focal point effects.

---

## Common Methodologies

### Zero-Shot Coordination (ZSC)
The dominant paradigm for studying coordination with unseen partners:
- **Self-Play (SP)**: Train by playing against copies; develops conventions but they're arbitrary
- **Population-Based Training (PBT)**: Train against diverse populations; more robust conventions
- **Other-Play (OP)**: Break symmetries during self-play; reduces convention arbitrariness
- **COLE**: Open-ended learning that iteratively expands coordination capacity
- **MEP**: Maximum entropy populations for diverse training partners

Used in: Carroll et al. 2019, Hu et al. 2020, Li et al. 2023, Zhao et al. 2021, Lou et al. 2023, Nigam et al. 2025

### Emergent Communication
Agents develop communication protocols through interaction:
- Reinforcement learning agents that learn to send/receive messages
- Lewis signaling games as minimal model
- Convention formation dynamics studied through multi-agent interaction

Used in: Foerster et al. 2016, Lipowska & Lipowski 2018, Bullard et al. 2020, Gupta et al. 2020

### Information-Theoretic Coordination Measurement
Quantifying coordination quality:
- Partial Information Decomposition (PID)
- Time-Delayed Mutual Information (TDMI)
- Synergy vs. redundancy decomposition
- Emergence capacity and practical criteria

Used in: Riedl 2026

---

## Standard Baselines

For zero-shot coordination experiments:
1. **Self-Play (SP)**: Baseline showing convention arbitrariness
2. **Behavioral Cloning (BC)**: Learning from human demonstrations
3. **FCP (Fictitious Co-Play)**: Training against diverse past snapshots
4. **MEP**: Maximum entropy population-based training
5. **COLE**: Cooperative open-ended learning (current SOTA)
6. **Random Partner**: Coordination with completely random agents

---

## Evaluation Metrics

1. **Episode Reward**: Joint task completion score (Overcooked soups delivered)
2. **Zero-Shot Coordination Score**: Performance when paired with unseen partners
3. **Human Subjective Preference**: Likert-scale ratings from human experiments
4. **Convention Alignment**: Degree to which partners converge on shared strategies
5. **Synergy Score**: Information-theoretic measure of emergent coordination (Riedl 2026)
6. **Focal Point Accuracy**: Success in pure coordination games (Schelling tasks)
7. **Coordination Coefficient**: Mutual information between agent actions

---

## Datasets in the Literature

| Dataset | Used in | Task |
|---------|---------|------|
| Overcooked layouts | Carroll 2019, Li 2023, Zhao 2021, many others | Cooperative cooking |
| Hanabi | Bard 2019, Hu 2020, Nekoei 2023 | Cooperative card game |
| Lewis signaling game | Lipowska 2018, OpenSpiel | Convention formation |
| Group binary search | Riedl 2026 | Emergent coordination |
| Stag hunt | OpenSpiel, various | Cooperation dilemma |
| Overcooked human data | Carroll 2019 | Human coordination patterns |

---

## Cross-Cutting Synthesis: What Enables Coordination Between Strangers?

From deep reading of the key papers, five principles emerge:

1. **Shared game structure as foundation.** Coordination between strangers is possible when agents exploit shared structural features of the environment. Lauffer et al. show coordination is only needed when multiple incompatible optimal joint plans exist. Hu et al. show coordination should be grounded in symmetry-invariant features, not arbitrary conventions.

2. **Symmetry as both problem and solution.** Self-play creates arbitrary conventions (Hu et al.); these fail catastrophically with new partners (Hanabi ad-hoc scores collapse from ~23 to ~0). Other-Play breaks this by training against symmetry-permuted partners, forcing agents to coordinate on structural features rather than arbitrary labels.

3. **Convention-formation skills vs. specific conventions.** The key insight for our hypothesis: teaching *specific conventions* is fragile (they don't transfer), but teaching *convention-formation skills* (perspective-taking, intent recognition, pragmatic reasoning) could transfer. Hanabi naturally exercises these meta-coordination skills.

4. **Observability reduces coordination burden.** Lauffer et al. show that full observability dramatically reduces coordination requirements (1 strategic equivalence class vs. 6 under partial observability). Game designs that maximize observability may reduce the need for pre-agreed conventions.

5. **Population dynamics matter.** Lipowska & Lipowski show that frozen conventions prevent adaptation, while population renewal enables convention evolution. This parallels the self-play vs. Other-Play distinction: mechanisms that prevent convention lock-in produce more transferable coordination.

---

## Gaps and Opportunities

### Gap 1: Transfer of Coordination Skills Across Domains
Most ZSC research tests coordination within the SAME game environment. Our hypothesis requires measuring transfer to UNRELATED environments. Keith et al. (2018, 2021) show some evidence of transfer from cooperative gaming to team tasks, but did not study the case where players train separately.

### Gap 2: Individual Training → Pair Coordination
Current research focuses on either: (a) pairs training together, or (b) AI agents trained on populations. No existing work studies whether INDIVIDUAL game experience (playing alone or with AI partners) transfers to improved coordination with a new human who had the SAME game experience.

### Gap 3: AI-Designed Coordination Games
While there is extensive work on AI game design (procedural content generation, mixed-initiative design), none specifically targets designing games to maximize coordination skill transfer. This is a novel application of AI game design.

### Gap 4: Quantifying "Twice as Well"
No standard benchmark exists for measuring general coordination ability across domains. We need to design evaluation tasks that test coordination in "unrelated environments."

---

## Recommendations for Our Experiment

### Recommended Approach
Based on the literature, the most promising experimental design is:

1. **Game Design Phase**: Use AI (LLMs or RL) to design a coordination game that teaches:
   - Focal point identification (Schelling-type tasks)
   - Convention formation speed
   - Theory of Mind (perspective-taking)
   - Complementary role adoption

2. **Training Phase**: Have individuals play the designed game independently (with AI partners or alone).

3. **Evaluation Phase**: Test coordination between pairs of trained individuals in unrelated coordination tasks:
   - Schelling focal point games (choosing matching answers)
   - Cooperative task completion (e.g., simplified Overcooked)
   - Tacit coordination games (no explicit communication)
   - Compare against untrained control group

### Recommended Datasets/Environments
1. **Overcooked-AI**: Primary testbed for cooperative coordination (well-established, has human data)
2. **OpenSpiel coordination games**: For pure coordination / focal point evaluation
3. **Hanabi**: For convention formation and ToM evaluation
4. **Group binary search (AI-GBS)**: For emergent coordination measurement

### Recommended Baselines
1. Untrained control group (no game experience)
2. Players trained with unrelated games (e.g., solo puzzle games)
3. Players trained with cooperative games together (Keith et al. baseline)
4. Standard ZSC baselines (SP, FCP, MEP) for AI agent comparison

### Recommended Metrics
1. Coordination improvement ratio (trained vs. control performance)
2. Focal point accuracy across multiple Schelling-type tasks
3. Convention formation speed (rounds to converge)
4. Information-theoretic synergy (Riedl's PID framework)
5. Subjective coordination quality ratings

### Methodological Considerations
- **Sample size**: Based on Keith et al. (2021), ~50-100 participants per condition needed for sufficient power
- **Transfer distance**: Must use truly unrelated evaluation tasks to demonstrate transfer
- **Individual vs. joint training**: Our hypothesis specifies individual training (both played independently)
- **Game complexity**: Simpler games may teach more transferable skills (Lauffer's minimal knowledge principle)
- **AI game design**: LLMs could generate game variants, with RL selecting for coordination-enhancing properties
