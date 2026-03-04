from pathlib import Path
from typing import Final

# Save directly in the current project directory
STATE_FILE: Final[Path] = Path("save.kdl")

def save_state(x: int, y: int) -> None:
    """Saves the player coordinates to a local .kdl file."""
    kdl_content: str = f"player x={x} y={y}\n"
    
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            _ = f.write(kdl_content) # Assigned to _ for strict linting
    except Exception:
        # Prevent file lock or permission errors from crashing the game
        pass

def load_state(default_x: int, default_y: int) -> tuple[int, int]:
    """Loads the player coordinates from the local .kdl file."""
    if not STATE_FILE.exists():
        return default_x, default_y
        
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            content: str = f.read().strip()
            
        parts: list[str] = content.split()
        x_val: int = int(parts[1].replace("x=", ""))
        y_val: int = int(parts[2].replace("y=", ""))
        
        return x_val, y_val
        
    except Exception:
        # If the file is manually edited poorly or corrupted, default to center safely
        return default_x, default_y
