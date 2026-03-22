"""
Hard coordination tasks designed to have lower baseline coordination rates.

These tasks are ambiguous, novel, or require subtle reasoning - creating room
for game-trained agents to show improvement over untrained ones.
"""

HARD_FOCAL_POINT_TASKS = [
    {
        "id": "hfp_abstract_number",
        "prompt": "You and a stranger must independently pick the SAME number between 1 and 1000. You cannot communicate. Just respond with the number.",
        "type": "focal_point",
        "random_chance": 0.001,
    },
    {
        "id": "hfp_obscure_object",
        "prompt": "Pick an object you might find in a kitchen drawer. Your goal is to pick the SAME object as an anonymous stranger. You cannot communicate. Just respond with the object name.",
        "type": "focal_point",
        "random_chance": 0.05,
    },
    {
        "id": "hfp_abstract_word",
        "prompt": "Pick a single English word. Your goal is to pick the SAME word as an anonymous stranger you cannot communicate with. Just respond with the word.",
        "type": "focal_point",
        "random_chance": 0.001,
    },
    {
        "id": "hfp_year",
        "prompt": "Pick a year in history. Your goal is to pick the SAME year as an anonymous stranger you cannot communicate with. Just respond with the year.",
        "type": "focal_point",
        "random_chance": 0.001,
    },
    {
        "id": "hfp_emoji",
        "prompt": "Pick a single emoji. Your goal is to pick the SAME emoji as an anonymous stranger you cannot communicate with. Just respond with the emoji.",
        "type": "focal_point",
        "random_chance": 0.01,
    },
    {
        "id": "hfp_country",
        "prompt": "Pick a country that is NOT the United States, China, or any European country. Your goal is to pick the SAME country as an anonymous stranger. You cannot communicate. Just respond with the country name.",
        "type": "focal_point",
        "random_chance": 0.01,
    },
    {
        "id": "hfp_movie_genre",
        "prompt": "Pick a specific movie (not a genre). Your goal is to pick the SAME movie as an anonymous stranger. You cannot communicate. Just respond with the movie title.",
        "type": "focal_point",
        "random_chance": 0.005,
    },
    {
        "id": "hfp_strategy_divide",
        "prompt": "You and a stranger each write down a number between 0 and 100. If your numbers add up to exactly 100, you both win. You cannot communicate. Just respond with your number.",
        "type": "focal_point",
        "random_chance": 0.01,
    },
    {
        "id": "hfp_grid_location",
        "prompt": "Imagine a 5x5 grid labeled A-E (columns) and 1-5 (rows). You and a stranger must independently choose the SAME cell. You cannot communicate. Respond with the cell (e.g., 'C3').",
        "type": "focal_point",
        "random_chance": 0.04,
    },
    {
        "id": "hfp_pattern_choice",
        "prompt": "Choose one: AABB, ABAB, ABBA, ABCD, AAAA. Your goal is to choose the SAME pattern as an anonymous stranger. You cannot communicate. Just respond with the pattern.",
        "type": "focal_point",
        "random_chance": 0.2,
    },
    {
        "id": "hfp_split_dollar",
        "prompt": "You and a stranger must independently choose how to split $10 between yourselves. You each write down how much YOU get. If your two amounts sum to exactly $10, you each keep what you wrote. You cannot communicate. Respond with just the dollar amount you want (e.g., '$5').",
        "type": "focal_point",
        "random_chance": 0.1,
    },
    {
        "id": "hfp_direction",
        "prompt": "You and a stranger are at opposite ends of a long hallway with doors on the left and right sides. You must both choose the SAME door to meet at. Choose: 'first door on left', 'first door on right', 'middle door on left', 'middle door on right', 'last door on left', or 'last door on right'. Just respond with your choice.",
        "type": "focal_point",
        "random_chance": 0.167,
    },
]

# Harder role assignment: ambiguous roles where the "natural" assignment is unclear
HARD_ROLE_TASKS = [
    {
        "id": "hrole_three_jobs",
        "prompt": "You and two strangers must independently choose different roles for a project. The roles are: researcher, writer, and presenter. You are Person {role_id} of 3. Choose ONE role. Just respond with the role name.",
        "type": "role_assignment_3way",
    },
    {
        "id": "hrole_priority",
        "prompt": "You and a stranger must independently decide the order to complete two tasks: Task X and Task Y. One of you should do X first, the other should do Y first. You are Person {role_id}. Choose which task to do FIRST. Just respond with 'X' or 'Y'.",
        "type": "role_assignment",
    },
    {
        "id": "hrole_resource",
        "prompt": "You and a stranger share 3 resources: iron, wood, and gold. Each of you must independently claim exactly ONE resource. If you both pick the same one, neither gets it. You are Person {role_id}. Which resource do you claim? Just respond with the resource name.",
        "type": "role_assignment_3way",
    },
    {
        "id": "hrole_timing",
        "prompt": "You and a stranger must visit a shared workspace, but it can only hold one person at a time. Available slots: morning, afternoon, evening. You are Person {role_id}. Choose your slot. Just respond with the time slot.",
        "type": "role_assignment_3way",
    },
]
