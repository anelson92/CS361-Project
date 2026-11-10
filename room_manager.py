## room manager is responsible for loading room data by room id 

import json
from pathlib import Path

ROOMS_DIR = Path(__file__).parent / "data" / "rooms"

def load_room(room_id):
    room_path = ROOMS_DIR / f"{room_id}.json"

    with open(room_path, "r", encoding="utf-8") as file:
        return json.load(file)
