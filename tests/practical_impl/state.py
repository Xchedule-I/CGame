import json
from pathlib import Path
from typing import Final, cast

# Save directly in the current project directory
STATE_FILE: Final[Path] = Path("../../save.json")

def save_state(x: int, y: int) -> None :
    '''Saves player co-ordinates to local .json file'''
    state_data: dict[str, int] = {"x": x, "y": y}

    try :
        with open(STATE_FILE, "w", encoding="utf-8") as f :
            json.dump(state_data, f, indent=4)
    except Exception:
        # Preventing file lock or permission errors from crashing the game
        pass

def load_state(default_x: int, default_y: int) -> tuple[int, int] :
    '''Loads the player co-ordinates from the .json file'''
    if not STATE_FILE.exists() :
        return default_x, default_y
    try :
        with open(STATE_FILE, "r", encoding="utf-8") as f :
            # Cast overrides the default return value of json.load() which is Any
            data: dict[str, int] = cast(dict[str, int], json.load(f))

        x_val: int = int(data.get("x", default_x))
        y_val: int = int(data.get("y", default_y))

        return x_val, y_val

    except Exception :
        return default_x, default_y

