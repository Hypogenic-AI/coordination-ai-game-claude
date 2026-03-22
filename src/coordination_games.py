"""
Coordination game definitions for the Coordination-Enhancing Video Game experiment.

This module defines:
1. Candidate coordination training games (treatments)
2. Evaluation tasks (focal points, role assignment, convention formation)
3. Game experience prompts that simulate "having played" a game
"""

# ── Coordination Training Games (Treatments) ──────────────────────────────

FOCAL_POINT_GAME = {
    "name": "Focal Point Game",
    "description": """You have played a game called 'MindMatch' extensively. In MindMatch:
- You are paired with an anonymous partner you cannot communicate with
- Each round, you both see a set of options and must independently pick the SAME one
- You earn points only when you both choose the same option
- Over many rounds, you learned that the key to success is:
  * Look for the option that STANDS OUT as most natural, obvious, or salient
  * Think about what your partner would consider the "default" or "obvious" choice
  * Cultural conventions and common knowledge are powerful coordination tools
  * When in doubt, go with the most common, typical, or prominent option
  * Numbers: pick round numbers (10, 100). Colors: pick primary/basic ones. Places: pick famous landmarks.
- You became very good at anticipating what a stranger would pick
- Your strategy: "What would MOST people naturally gravitate toward?"
""",
}

CONVENTION_GAME = {
    "name": "Convention Formation Game",
    "description": """You have played a game called 'SignalCraft' extensively. In SignalCraft:
- You are paired with anonymous partners across many rounds
- You develop a shared signaling system from scratch each time
- You learned to form conventions quickly by:
  * Starting with natural/intuitive mappings (e.g., "up" means "go up")
  * Being consistent once you establish a pattern
  * Adapting quickly when your partner signals a different convention
  * Using simple, memorable patterns rather than complex ones
  * Looking for structural/logical mappings between signals and meanings
- You became expert at rapidly forming shared conventions with strangers
- Your strategy: "Start with the most natural mapping, stay consistent, adapt if partner differs"
""",
}

AI_DESIGNED_GAME = {
    "name": "AI-Designed Coordination Game",
    "description": """You have played a game called 'SyncMinds' extensively. SyncMinds was designed by AI specifically to build coordination skills. In SyncMinds:
- Phase 1 (Focal Points): You practiced identifying "obvious" choices among options, learning that the most salient/prominent option is usually the coordination point
- Phase 2 (Perspective-Taking): You practiced predicting what anonymous partners would choose, developing strong Theory of Mind for strangers
- Phase 3 (Role Differentiation): You practiced dividing tasks with partners without communication, learning to identify natural role assignments based on context
- Phase 4 (Convention Speed): You practiced forming shared conventions rapidly with new partners each round
- Key lessons you internalized:
  * Always think from your partner's perspective first
  * Choose the most "obvious" or "natural" option when coordinating
  * When dividing work, take the role that your context/position most naturally suggests
  * Establish patterns quickly and stick with them
  * Simple, intuitive strategies beat clever, complex ones
  * Common knowledge and cultural defaults are coordination tools
- You became exceptionally skilled at coordinating with strangers across many different tasks
""",
}

IRRELEVANT_GAME = {
    "name": "Trivia Game (Control)",
    "description": """You have played a trivia game called 'BrainQuest' extensively. In BrainQuest:
- You answered factual questions across many categories
- You learned many interesting facts about history, science, geography, and pop culture
- You became good at recalling obscure information
- The game was purely individual with no partner interaction
""",
}

NO_GAME = {
    "name": "No Game (Baseline)",
    "description": None,
}

ALL_TREATMENTS = [NO_GAME, IRRELEVANT_GAME, FOCAL_POINT_GAME, CONVENTION_GAME, AI_DESIGNED_GAME]

# ── Evaluation Tasks ──────────────────────────────────────────────────────

FOCAL_POINT_TASKS = [
    {
        "id": "fp_number",
        "prompt": "Pick a positive integer. Your goal is to pick the SAME number as your anonymous partner, whom you cannot communicate with. Just respond with the number and nothing else.",
        "type": "focal_point",
    },
    {
        "id": "fp_color",
        "prompt": "Pick a color. Your goal is to pick the SAME color as your anonymous partner, whom you cannot communicate with. Just respond with the color name and nothing else.",
        "type": "focal_point",
    },
    {
        "id": "fp_city",
        "prompt": "Pick a city to meet a stranger in. You and an anonymous partner must independently choose the SAME city. You cannot communicate. Just respond with the city name and nothing else.",
        "type": "focal_point",
    },
    {
        "id": "fp_time",
        "prompt": "Pick a time of day (hour) to meet a stranger. You and an anonymous partner must independently choose the SAME time. You cannot communicate. Just respond with the time (e.g., '12:00 PM' or 'noon') and nothing else.",
        "type": "focal_point",
    },
    {
        "id": "fp_shape",
        "prompt": "Pick a geometric shape. Your goal is to pick the SAME shape as your anonymous partner, whom you cannot communicate with. Just respond with the shape name and nothing else.",
        "type": "focal_point",
    },
    {
        "id": "fp_day",
        "prompt": "Pick a day of the week. Your goal is to pick the SAME day as your anonymous partner, whom you cannot communicate with. Just respond with the day name and nothing else.",
        "type": "focal_point",
    },
    {
        "id": "fp_letter",
        "prompt": "Pick a letter of the alphabet. Your goal is to pick the SAME letter as your anonymous partner, whom you cannot communicate with. Just respond with the letter and nothing else.",
        "type": "focal_point",
    },
    {
        "id": "fp_animal",
        "prompt": "Pick an animal. Your goal is to pick the SAME animal as your anonymous partner, whom you cannot communicate with. Just respond with the animal name and nothing else.",
        "type": "focal_point",
    },
    {
        "id": "fp_food",
        "prompt": "Pick a food item. Your goal is to pick the SAME food as your anonymous partner, whom you cannot communicate with. Just respond with the food name and nothing else.",
        "type": "focal_point",
    },
    {
        "id": "fp_number_1to10",
        "prompt": "Pick a number between 1 and 10. Your goal is to pick the SAME number as your anonymous partner, whom you cannot communicate with. Just respond with the number and nothing else.",
        "type": "focal_point",
    },
]

ROLE_ASSIGNMENT_TASKS = [
    {
        "id": "role_cooking",
        "prompt": "You and an anonymous partner must prepare a meal together without communicating. One of you should cook the main dish and the other should prepare the side dish. You are Person {role_id}. Choose ONE role: 'main dish' or 'side dish'. Just respond with your choice and nothing else.",
        "type": "role_assignment",
    },
    {
        "id": "role_moving",
        "prompt": "You and an anonymous partner must move furniture into a new apartment without communicating. One of you should carry items upstairs and the other should unpack boxes. You are Person {role_id}. Choose ONE role: 'carry upstairs' or 'unpack boxes'. Just respond with your choice and nothing else.",
        "type": "role_assignment",
    },
    {
        "id": "role_project",
        "prompt": "You and an anonymous partner must complete a project without communicating. One of you should write the report and the other should create the presentation. You are Person {role_id}. Choose ONE role: 'write report' or 'create presentation'. Just respond with your choice and nothing else.",
        "type": "role_assignment",
    },
    {
        "id": "role_rescue",
        "prompt": "You and an anonymous partner must respond to an emergency without communicating. One of you should call for help and the other should administer first aid. You are Person {role_id}. Choose ONE role: 'call for help' or 'first aid'. Just respond with your choice and nothing else.",
        "type": "role_assignment",
    },
    {
        "id": "role_guard",
        "prompt": "You and an anonymous partner must guard two doors without communicating. One of you should guard the front door and the other should guard the back door. You are Person {role_id}. Choose ONE role: 'front door' or 'back door'. Just respond with your choice and nothing else.",
        "type": "role_assignment",
    },
]

# Convention formation: multi-round Lewis signaling game
CONVENTION_TASK = {
    "id": "convention_signal",
    "system": """You are playing a coordination game. There are 3 objects (A, B, C) and 3 signals (1, 2, 3).
Each round, one player sees an object and sends a signal. The other player sees the signal and guesses the object.
You need to develop a shared mapping between objects and signals.
You will play multiple rounds, alternating roles. After each round you learn if the guess was correct.""",
    "type": "convention",
    "n_rounds": 10,
    "objects": ["A", "B", "C"],
    "signals": ["1", "2", "3"],
}
