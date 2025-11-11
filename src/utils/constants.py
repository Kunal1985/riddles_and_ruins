import json
import os

COMBAT_PENALTY_POINTS = {
    1: 20,
    2: 40,
    3: 60
}

# Load puzzles from JSON file
def load_puzzles():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, 'puzzles.json')
    with open(json_path, 'r') as f:
        return json.load(f)

PUZZLES_DICTIONARY = load_puzzles()