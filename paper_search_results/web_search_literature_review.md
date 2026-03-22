# Literature Review: Coordination Enhancing Video Game
## Web Search Results - 2026-03-22

**Hypothesis:** A video game can be designed (with AI) so that two strangers who've both played it can coordinate twice as well in unrelated environments.

---

## 1. FOUNDATIONAL THEORY: Schelling Focal Points & Tacit Coordination

### Mehta, Starmer & Sugden (1994)
- **Title:** "The Nature of Salience: An Experimental Investigation of Pure Coordination Games"
- **Authors:** Judith Mehta, Chris Starmer, Robert Sugden
- **Published:** American Economic Review, 1994
- **URL:** https://link.springer.com/article/10.1007/BF01079211
- **PhilPapers:** https://philpapers.org/rec/MEHFPI
- **Relevance:** Foundational experimental work on Schelling focal points. Demonstrated that coordination was far more likely when parties had the explicit goal of matching vs. simply stating preferences. E.g., 35% said "rose" when picking a flower, but 67% said "rose" when trying to match a stranger. Directly relevant to understanding what shared cognitive structures enable coordination.

### Isoni, Poulsen, Sugden & Tsutsui (2014)
- **Title:** "Focal Points in Coordinated Divergence"
- **Authors:** Andrea Isoni, Anders Poulsen, Robert Sugden, Kei Tsutsui
- **Published:** American Economic Review, 2014
- **URL:** https://faculty.wharton.upenn.edu/wp-content/uploads/2012/08/focal_points_3.pdf
- **Relevance:** Tests bargaining games with and without focal points in controlled experiments.

### Bardsley et al. (2010)
- **Title:** "Explaining Focal Points: Cognitive Hierarchy Theory versus Team Reasoning"
- **URL:** https://www.nottingham.ac.uk/cedex/documents/papers/2008-17.pdf
- **Relevance:** Theoretical framework for why focal points work - relevant to game design for coordination.

### Group Behaviour in Tacit Coordination Games (2019)
- **Title:** "Group Behaviour in Tacit Coordination Games with Focal Points"
- **Published:** Games and Economic Behavior, 2019
- **URL:** https://www.sciencedirect.com/science/article/pii/S0899825619301125
- **Relevance:** Groups achieve higher coordination than individuals - groups more often choose salient options.

### Overcoming Coordination Failure (2022)
- **Title:** "Overcoming Coordination Failure in Games with Focal Points"
- **Published:** Games and Economic Behavior, 2022
- **URL:** https://www.sciencedirect.com/science/article/pii/S0899825622001488
- **Relevance:** Tests whether increasing salience of focal points can counteract conflicts of interest.

### Modeling Individual Tacit Coordination Ability (2022)
- **Title:** "Modeling and Predicting Individual Tacit Coordination Ability"
- **Published:** PMC, 2022
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC8817001/
- **Relevance:** Models individual differences in tacit coordination ability - key for measuring game effectiveness.

### The Power of Focal Points Is Limited
- **Title:** "The Power of Focal Points Is Limited: Even Minute Payoff Asymmetry May Yield Large Coordination Failures"
- **Authors:** Uri Gneezy et al.
- **URL:** https://rady.ucsd.edu/_files/faculty-research/uri-gneezy/focal-points.pdf
- **Relevance:** Important constraint - even small payoff asymmetries reduce focal point effectiveness.

---

## 2. ZERO-SHOT COORDINATION (Core Technical Foundation)

### Hu, Lerer, Peysakhovich & Foerster (2020)
- **Title:** "Other-Play for Zero-Shot Coordination"
- **Authors:** Hengyuan Hu, Adam Lerer, Alex Peysakhovich, Jakob N. Foerster
- **arXiv:** 2003.02979
- **URL:** https://arxiv.org/abs/2003.02979
- **Published:** ICML 2020
- **Relevance:** DIRECTLY RELEVANT. Introduces the zero-shot coordination problem - building AI agents that can coordinate with novel partners never seen before. Standard self-play creates specialized conventions that fail with new partners. "Other-Play" algorithm exploits symmetries to find robust strategies. Tested on Hanabi.

### Bard et al. (2020)
- **Title:** "The Hanabi Challenge: A New Frontier for AI Research"
- **arXiv:** 1902.00506
- **URL:** https://arxiv.org/abs/1902.00506
- **Published:** Artificial Intelligence, 2020
- **Relevance:** DIRECTLY RELEVANT. Proposes Hanabi as a benchmark for cooperative AI under imperfect information. Requires reasoning about beliefs and intentions of other agents - a core mechanism for the coordination game.

### Carroll et al. (2019)
- **Title:** "On the Utility of Learning about Humans for Human-AI Coordination"
- **arXiv:** 1910.05789
- **URL:** https://arxiv.org/abs/1910.05789
- **Relevance:** DIRECTLY RELEVANT. Uses Overcooked-AI environment. Shows that self-play agents fail to coordinate with humans because they develop conventions humans don't share. Agents must learn to be understood by and understand humans.

### Equivariant Networks for Zero-Shot Coordination (2022)
- **arXiv:** 2210.12124
- **URL:** https://arxiv.org/abs/2210.12124
- **Relevance:** Equivariant network architecture for leveraging environmental symmetry in zero-shot coordination.

### Tackling Cooperative Incompatibility for Zero-Shot Human-AI Coordination (2023)
- **arXiv:** 2306.03034
- **URL:** https://arxiv.org/abs/2306.03034
- **Relevance:** COLE framework for evaluating cooperative capacity of strategies. Includes 130-participant human experiments on Overcooked platform.

### OvercookedV2 (2025)
- **Title:** "OvercookedV2: Rethinking Overcooked for Zero-Shot Coordination"
- **URL:** https://arxiv.org/html/2503.17821v1
- **Relevance:** Next-generation benchmark for zero-shot coordination algorithms.

### Noisy Zero-Shot Coordination (2024)
- **Title:** "Noisy Zero-Shot Coordination: Breaking The Common Knowledge Assumption"
- **URL:** https://arxiv.org/html/2411.04976v1
- **Relevance:** Extends ZSC by relaxing common knowledge assumptions.

### Diverse Conventions for Human-AI Collaboration (2023)
- **Title:** "Diverse Conventions for Human-AI Collaboration"
- **Authors:** Bidipta Sarkar et al.
- **URL:** https://arxiv.org/pdf/2310.15414
- **Relevance:** Addresses the diversity of conventions humans may use and how AI can adapt.

### Lupu et al. (2021)
- **Title:** "Trajectory Diversity for Zero-Shot Coordination"
- **Published:** ICML 2021
- **URL:** http://proceedings.mlr.press/v139/lupu21a/lupu21a.pdf
- **Relevance:** Diversity in training trajectories for better zero-shot coordination.

---

## 3. AD HOC TEAMWORK

### Mirsky et al. (2022)
- **Title:** "A Survey of Ad Hoc Teamwork Research"
- **arXiv:** 2202.10450
- **URL:** https://arxiv.org/abs/2202.10450
- **Relevance:** DIRECTLY RELEVANT. Comprehensive survey of designing agents that collaborate with new teammates without prior coordination. Core problem statement matches our hypothesis.

### Open Ad Hoc Teamwork with Cooperative Game Theory (2024)
- **arXiv:** 2402.15259
- **URL:** https://arxiv.org/abs/2402.15259
- **Relevance:** Extends ad hoc teamwork to open (changing) teams using cooperative game theory.

### N-Agent Ad Hoc Teamwork (2024)
- **URL:** https://arxiv.org/html/2404.10740v1
- **Relevance:** Scales ad hoc teamwork to N agents.

---

## 4. COOPERATIVE AI (Research Agenda)

### Dafoe et al. (2020)
- **Title:** "Open Problems in Cooperative AI"
- **arXiv:** 2012.08630
- **URL:** https://arxiv.org/abs/2012.08630
- **Relevance:** DIRECTLY RELEVANT. Proposes that AI should explicitly focus on cooperation problems. Defines the Cooperative AI research agenda. Game-theoretic foundations for cooperation between agents.

### Conitzer & Oesterheld (2023)
- **Title:** "Foundations of Cooperative AI"
- **Published:** AAAI 2023
- **URL:** https://www.cs.cmu.edu/~conitzer/FOCALAAAI23.pdf
- **Relevance:** Theoretical foundations for cooperative AI using game theory.

---

## 5. EMERGENT COMMUNICATION & CONVENTION FORMATION

### Lazaridou & Baroni (2020)
- **Title:** "Emergent Multi-Agent Communication in the Deep Learning Era"
- **arXiv:** 2006.02419
- **URL:** https://arxiv.org/abs/2006.02419
- **Relevance:** DIRECTLY RELEVANT. Survey of language emergence in deep agent communities. Reviews conditions under which communication protocols emerge, primarily through Lewis signaling / reference games.

### Mordatch & Abbeel (2017)
- **Title:** "Emergence of Grounded Compositional Language in Multi-Agent Populations"
- **arXiv:** 1703.04908
- **URL:** https://arxiv.org/abs/1703.04908
- **Published:** AAAI 2017
- **Relevance:** DIRECTLY RELEVANT. Multi-agent environment where compositional language emerges with defined vocabulary and syntax. Also observes emergence of non-verbal communication (pointing, guiding) when language unavailable.

### Lazaridou, Hermann, Tuyls & Clark (2018)
- **Title:** "Emergence of Linguistic Communication from Referential Games with Symbolic and Pixel Input"
- **arXiv:** 1804.03984
- **URL:** https://arxiv.org/abs/1804.03984
- **Published:** ICLR 2018
- **Relevance:** Agents learn communication from raw pixel data in referential games.

### Chaabouni et al. (2022)
- **Title:** "Emergent Communication: Generalization and Overfitting in Lewis Games"
- **arXiv:** 2209.15342
- **URL:** https://arxiv.org/abs/2209.15342
- **Relevance:** Shows RL-trained agents develop languages with undesirable properties; decomposes objective into co-adaptation loss and information loss.

### Kang et al. (2024)
- **Title:** "A Combinatorial Approach to Neural Emergent Communication"
- **arXiv:** 2410.18806
- **URL:** https://arxiv.org/abs/2410.18806
- **Relevance:** Novel combinatorial framework for emergent communication.

### Riedl (2025)
- **Title:** "Emergent Coordination in Multi-Agent Language Models"
- **arXiv:** 2510.05174
- **URL:** https://arxiv.org/abs/2510.05174
- **Relevance:** Information-theoretic framework testing whether multi-agent LLM systems show higher-order structure. Tests GPT-4.1, Llama, Gemini, Qwen agents on group guessing tasks.

### Emergent Social Conventions in LLM Populations (2025)
- **Title:** "Emergent Social Conventions and Collective Bias in LLM Populations"
- **Published:** Science Advances, 2025
- **URL:** https://www.science.gov/doi/10.1126/sciadv.adu9368
- **PMC:** https://pmc.ncbi.nlm.nih.gov/articles/PMC12077490/
- **Relevance:** LLM agent populations spontaneously develop shared social conventions through interaction alone - mimicking human norm formation.

### Lewis's Signaling Game as beta-VAE (2023)
- **arXiv:** 2311.04453
- **URL:** https://arxiv.org/abs/2311.04453
- **Relevance:** Reinterprets Lewis signaling games through variational autoencoder lens.

---

## 6. SHARED MENTAL MODELS & TEAM COGNITION

### Scheutz et al. (2017)
- **Title:** "A Framework for Developing and Using Shared Mental Models in Human-Agent Teams"
- **URL:** https://hrilab.tufts.edu/publications/scheutzetal17smm.pdf
- **Relevance:** Formal and computational foundations for integrating shared mental models into agent architectures for mixed human-agent teams.

### Knowledge and Experience in Video Game Play (2020)
- **Title:** "Knowledge and Experience in Video Game Play: Understanding Individual Differences and Mental Model Transfer Across Game Genres"
- **Published:** Human Factors and Ergonomics Society, 2020
- **URL:** https://journals.sagepub.com/doi/abs/10.1177/1071181320641379
- **Relevance:** Framework for characterizing knowledge differences and mental model transfer across game genres.

### Investigating Effects of Cognitive Styles on Collaborative Gameplay
- **Title:** "Investigating the Effects of Individual Cognitive Styles on Collaborative Gameplay"
- **Published:** ACM TOCHI
- **URL:** https://dl.acm.org/doi/10.1145/3445792
- **Relevance:** How cognitive styles affect team coordination in multiplayer games (Dota 2, LoL, Fortnite). Shared mental models and situation awareness.

---

## 7. COOPERATIVE VIDEO GAMES & PROSOCIAL BEHAVIOR

### Keith et al. (2021)
- **Title:** "Team Building Through Team Video Games: Randomized Controlled Trial"
- **Published:** JMIR Serious Games, 2021
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC8715357/
- **Relevance:** DIRECTLY RELEVANT. RCT showing teams using cooperative video games increased productivity significantly more than controls. Team-building objectives met naturally through cooperative gameplay. Flow mediates the effect.

### Greitemeyer & Mugge (2014)
- **Title:** "Video Games Do Affect Social Outcomes: A Meta-Analytic Review"
- **Authors:** Tobias Greitemeyer, Dirk O. Mugge
- **Published:** Personality and Social Psychology Bulletin, 2014
- **URL:** https://journals.sagepub.com/doi/abs/10.1177/0146167213520459
- **PubMed:** https://pubmed.ncbi.nlm.nih.gov/24458215/
- **Relevance:** Meta-analysis of 98 studies (N=36,965). Prosocial games increase prosocial behavior (helping: beta=.49, cooperation: beta=.18). Demonstrates causal pathway from game exposure to real-world cooperation.

### Gentile et al. (2009)
- **Title:** "The Effects of Prosocial Video Games on Prosocial Behaviors: International Evidence from Correlational, Longitudinal, and Experimental Studies"
- **Published:** PMC, 2009
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC2678173/
- **Relevance:** International evidence across multiple study designs that prosocial games increase prosocial behavior.

### Farah, Dorneich & Gilbert (2022-2023)
- **Title:** "Evaluating Team Metrics in Cooperative Video Games" (2022)
- **Title:** "Evaluating the Consistency of Cooperative Video Games in Inducing Teamwork Behaviors" (2023)
- **URLs:** https://journals.sagepub.com/doi/abs/10.1177/1071181322661240 / https://journals.sagepub.com/doi/10.1177/21695067231196239
- **Relevance:** Cooperative game designs consistently induce measurable teamwork behaviors including coordination, planning, backup behavior, and mutual monitoring.

### From Gaming to Reality: Skills Transfer (2024)
- **Title:** "From Gaming to Reality: Effectiveness of Skills Transfer from Competitive Sandbox Gaming Environment"
- **URL:** https://educationaltechnologyjournal.springeropen.com/articles/10.1186/s41239-024-00500-2
- **Relevance:** Demonstrates near and far transfer of coordination skills from gaming to real-world contexts.

---

## 8. MULTI-AGENT REINFORCEMENT LEARNING

### Multi-Agent RL Comprehensive Survey (2023)
- **arXiv:** 2312.10256
- **URL:** https://arxiv.org/html/2312.10256v2
- **Relevance:** Comprehensive survey of MARL covering cooperative, competitive, and mixed settings.

### Game Theory and Multi-Agent RL (2024)
- **Title:** "Game Theory and Multi-Agent Reinforcement Learning: From Nash Equilibria to Evolutionary Dynamics"
- **URL:** https://arxiv.org/html/2412.20523v1
- **Relevance:** Integration of evolutionary game theory with MARL for adaptive cooperation.

### Multiagent Cooperation with Deep RL (2015)
- **Title:** "Multiagent Cooperation and Competition with Deep Reinforcement Learning"
- **arXiv:** 1511.08779
- **URL:** https://arxiv.org/abs/1511.08779
- **Relevance:** Early work on deep RL for multi-agent cooperation.

### Game-Theoretic Multi-Agent RL (2020)
- **arXiv:** 2011.00583
- **URL:** https://arxiv.org/html/2011.00583v4
- **Relevance:** Game-theoretic framework for MARL.

### Social Learning through Interactions with Other Agents (2024)
- **arXiv:** 2407.21713
- **URL:** https://arxiv.org/abs/2407.21713
- **Relevance:** Survey on how social learning paradigms have been implemented in machine learning.

---

## 9. PROCEDURAL CONTENT GENERATION & AI GAME DESIGN

### Procedural Content Generation Survey with LLM Integration (2024)
- **arXiv:** 2410.15644
- **URL:** https://arxiv.org/html/2410.15644v1
- **Relevance:** Survey of PCG methods with emerging LLM integration - relevant to AI-designed game content.

### Games for AI Research: Review and Perspectives (2023)
- **arXiv:** 2304.13269
- **URL:** https://arxiv.org/html/2304.13269v4
- **Relevance:** Review of games as platforms for AI research including coordination.

### Player-Driven Emergence in LLM-Driven Game Narrative (2024)
- **arXiv:** 2404.17027
- **URL:** https://arxiv.org/pdf/2404.17027
- **Relevance:** Emergent behavior from player-LLM interaction in games.

### Serious Games: Systematic Literature Review (2023)
- **arXiv:** 2306.03098
- **URL:** https://arxiv.org/pdf/2306.03098
- **Relevance:** Updated systematic review of serious games research.

---

## 10. ADDITIONAL HIGHLY RELEVANT PAPERS

### LLM-Hanabi (2025)
- **Title:** "LLM-Hanabi: Evaluating Multi-Agent Gameplays with Theory-of-Mind"
- **arXiv:** 2510.04980
- **URL:** https://arxiv.org/abs/2510.04980
- **Relevance:** Evaluates LLM Theory of Mind in cooperative game settings.

### A Generalist Hanabi Agent (2025)
- **arXiv:** 2503.14555
- **URL:** https://arxiv.org/abs/2503.14555
- **Relevance:** Generalist agent that can play different Hanabi configurations.

### Sparks of Cooperative Reasoning (2025)
- **arXiv:** 2601.18077
- **URL:** https://arxiv.org/abs/2601.18077
- **Relevance:** Benchmarks 17 LLMs in cooperative Hanabi, studies persistent coordination failures.

### Maximum Entropy Population-Based Training for Zero-Shot Human-AI Coordination (2021)
- **URL:** https://arxiv.org/pdf/2112.11701
- **Relevance:** Population-based training method for human-AI coordination.

### Cooperative Open-ended Learning for Zero-Shot Coordination (2023)
- **URL:** https://arxiv.org/html/2302.04831v4
- **Relevance:** Open-ended learning framework for ZSC.

### Multi-Agent Coordination across Diverse Applications: A Survey (2025)
- **arXiv:** 2502.14743
- **URL:** https://arxiv.org/html/2502.14743v2
- **Relevance:** Comprehensive 2025 survey of multi-agent coordination.

---

## SUMMARY OF arXiv PAPERS (for PDF download)

| arXiv ID | Short Title | Year |
|-----------|-------------|------|
| 2003.02979 | Other-Play for Zero-Shot Coordination | 2020 |
| 1902.00506 | The Hanabi Challenge | 2020 |
| 1910.05789 | Learning about Humans for Human-AI Coordination | 2019 |
| 2012.08630 | Open Problems in Cooperative AI | 2020 |
| 2006.02419 | Emergent Multi-Agent Communication Survey | 2020 |
| 1703.04908 | Emergence of Grounded Compositional Language | 2017 |
| 1804.03984 | Emergence of Linguistic Communication | 2018 |
| 2202.10450 | Survey of Ad Hoc Teamwork | 2022 |
| 2209.15342 | Emergent Communication in Lewis Games | 2022 |
| 2510.05174 | Emergent Coordination in Multi-Agent LMs | 2025 |
| 2210.12124 | Equivariant Networks for ZSC | 2022 |
| 2306.03034 | Tackling Cooperative Incompatibility for ZSC | 2023 |
| 2402.15259 | Open Ad Hoc Teamwork | 2024 |
| 2312.10256 | Multi-Agent RL Comprehensive Survey | 2023 |
| 1511.08779 | Multiagent Cooperation with Deep RL | 2015 |
| 2011.00583 | Game-Theoretic Multi-Agent RL | 2020 |
| 2407.21713 | Social Learning through Interactions | 2024 |
| 2410.15644 | PCG Survey with LLM Integration | 2024 |
| 2304.13269 | Games for AI Research | 2023 |
| 2404.17027 | Player-Driven Emergence in LLM Games | 2024 |
| 2306.03098 | Serious Games Systematic Review | 2023 |
| 2510.04980 | LLM-Hanabi Theory of Mind | 2025 |
| 2503.14555 | Generalist Hanabi Agent | 2025 |
| 2601.18077 | Sparks of Cooperative Reasoning | 2025 |
| 2112.11701 | MaxEnt Population-Based Training ZSC | 2021 |
| 2302.04831 | Cooperative Open-ended Learning ZSC | 2023 |
| 2502.14743 | Multi-Agent Coordination Survey | 2025 |
| 2310.15414 | Diverse Conventions Human-AI | 2023 |
| 2410.18806 | Combinatorial Neural Emergent Communication | 2024 |
| 2311.04453 | Lewis Signaling Game as beta-VAE | 2023 |
| 2412.20523 | Game Theory and MARL | 2024 |
| 2601.08129 | Emergent Coordination via Pressure Fields | 2026 |
| 2602.00966 | Symphony-Coord Decentralized Coordination | 2026 |
| 2411.04976 | Noisy Zero-Shot Coordination | 2024 |

---

## KEY THEMES FOR THE HYPOTHESIS

1. **Zero-shot coordination** is the exact technical framing of our problem: can agents (humans) coordinate with strangers?
2. **Focal points / Schelling points** provide the cognitive mechanism: shared salience enables tacit coordination
3. **Shared mental models** explain the transfer mechanism: games build common cognitive frameworks
4. **Emergent communication** shows how conventions arise without explicit agreement
5. **Ad hoc teamwork** is the AI formalization of coordinating with unknown partners
6. **Prosocial game effects** have causal empirical evidence (meta-analyses) for behavioral transfer
7. **The convention problem** (self-play agents fail with strangers) mirrors our core challenge
8. **Cultural common knowledge** determines focal point effectiveness - games could build this
