# Research Plan: Coordination-Enhancing Video Game

## Motivation & Novelty Assessment

### Why This Research Matters
Coordination between strangers is a fundamental challenge in teamwork, emergency response, online collaboration, and multi-agent systems. If a game could reliably improve strangers' ability to coordinate—even without direct practice together—it would have transformative applications in team formation, distributed work, and human-AI cooperation. The "2x improvement" target, while ambitious, aligns with observed focal point effects in the literature (Mehta et al. 1994).

### Gap in Existing Work
Based on the literature review, three critical gaps exist:
1. **Transfer across domains**: ZSC research tests coordination within the same game, not transfer to unrelated environments
2. **Individual training → pair coordination**: No work studies whether individual game experience transfers to improved coordination with a stranger who had the same experience
3. **AI-designed coordination games**: No work uses AI to specifically design games that maximize coordination skill transfer

### Our Novel Contribution
We test whether **in-context game experience** (playing a coordination-focused game) improves **zero-shot coordination with strangers on novel tasks**. We use LLM agents as proxies for human players (validated by Riedl 2026), enabling large-scale controlled experiments. We also use AI (GPT-4.1) to design candidate coordination games and measure which game properties maximize transfer.

### Experiment Justification
- **Experiment 1 (Focal Point Coordination)**: Tests the most fundamental coordination skill—choosing the same "obvious" answer without communication. Directly measures Schelling focal point identification.
- **Experiment 2 (Tacit Role Assignment)**: Tests complementary behavior—can trained agents divide labor without communication? Tests a higher-order coordination skill.
- **Experiment 3 (Convention Formation Speed)**: Tests whether game experience accelerates learning shared conventions in a new domain. Measures adaptation speed, not just static coordination.
- **Experiment 4 (AI Game Design)**: Tests whether AI can design games that maximize coordination transfer, by varying game properties and measuring downstream coordination.

## Research Question
Can a video game be designed such that two people who have never met, but have both played it, coordinate on average 2x better in unrelated tasks? Can AI be used to design such a game?

## Background and Motivation
The hypothesis bridges several established research areas:
- **Schelling focal points** (Mehta et al. 1994): Coordination rates double when players try to match vs. random
- **Zero-shot coordination** (Hu et al. 2020): Breaking arbitrary conventions improves novel-partner coordination
- **Cooperative gaming transfer** (Keith et al. 2018, 2021): RCT evidence that cooperative games improve team performance
- **Emergent LLM coordination** (Riedl 2026): LLM agents exhibit emergent coordination, validating them as proxies

Key insight from literature: Teaching *convention-formation skills* (perspective-taking, focal point identification, role differentiation) transfers better than teaching *specific conventions*.

## Hypothesis Decomposition
1. **H1**: LLM agents given coordination game experience will match on Schelling focal point tasks at significantly higher rates than untrained agents
2. **H2**: Game-trained agents will adopt complementary roles in tacit coordination tasks more often than untrained agents
3. **H3**: Game-trained agents will form conventions faster in novel signaling games
4. **H4**: Games designed to emphasize Theory of Mind and focal point salience will produce greater coordination transfer than games emphasizing other skills
5. **H_main**: The best game design will produce ≥2x coordination improvement

## Proposed Methodology

### Approach
Use LLM agents (GPT-4.1) as proxies for human players in a controlled experiment with 4 conditions:
- **Control**: No game context (baseline coordination)
- **Treatment A**: "Focal Point Game" experience (game emphasizing Schelling-type choices)
- **Treatment B**: "Convention Game" experience (game emphasizing convention formation)
- **Treatment C**: "AI-Designed Game" (game designed by GPT-4.1 to maximize coordination transfer)

Each condition tested on 3 evaluation tasks with N=100 independent pairs per condition.

### Experimental Steps
1. Design 3 candidate coordination games with different emphases
2. Create evaluation suite: focal point tasks, role assignment tasks, convention tasks
3. Run control condition (no game experience) as baseline
4. Run each treatment condition (game experience in context)
5. Compare coordination rates across conditions
6. Analyze which game properties maximize transfer

### Baselines
- **Random**: Expected coordination by chance (1/k for k options)
- **No-game control**: LLM agents with no coordination training
- **Irrelevant-game control**: Agents given experience with a non-coordination game (e.g., trivia)

### Evaluation Metrics
- **Match rate**: % of pairs choosing the same answer (focal point tasks)
- **Complementarity score**: % of pairs adopting non-overlapping roles (role tasks)
- **Convention speed**: Rounds to reach 90% agreement (signaling tasks)
- **Coordination improvement ratio**: Treatment match rate / Control match rate (target: ≥2.0)

### Statistical Analysis Plan
- Chi-squared tests for match rate comparisons
- Bootstrap confidence intervals for coordination ratios
- Bonferroni correction for multiple comparisons (4 conditions × 3 tasks)
- Effect sizes (Cohen's h for proportions)
- Significance level: α = 0.05

## Expected Outcomes
- H1 supported if focal-point match rate > control at p < 0.05
- H_main supported if best treatment achieves ≥2x control match rate
- Expect AI-designed game to outperform hand-designed games

## Timeline and Milestones
- Planning: 20 min ✓
- Environment setup & game design: 20 min
- Implementation: 60 min
- Experiments (API calls): 40 min
- Analysis & visualization: 30 min
- Documentation: 20 min

## Potential Challenges
- API rate limits → batch with delays, use caching
- LLM agents may not be perfect proxies for humans → acknowledge as limitation
- "2x improvement" may be too ambitious → report actual improvement ratios honestly
- Temperature sensitivity → test at multiple temperatures

## Success Criteria
1. Statistically significant coordination improvement in at least one treatment vs. control
2. Clear identification of which game properties drive coordination transfer
3. AI-designed game performs competitively with or better than hand-designed games
4. Honest assessment of whether 2x improvement is achievable
