from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Union


@dataclass
class ProfileConfig:
    """Holds all metadata and resolved paths for a single CGAME profile.

    Paths are resolved by DirectoryManager and injected here, so
    ProfileConfig is a pure data holder — no path logic inside.
    """
    name: str
    sshKey: str
    createdAt: int
    lastModifiedAt: int
    is_active: bool

    # Folder paths
    profile_path: Path          # profiles/<name>/
    backup_path: Path           # profiles/<name>/backup/
    save_path: Path             # profiles/<name>/saves/

    # GameState file paths
    game_state_path: Path       # profiles/<name>/saves/gamestate.json
    backup_game_state_path: Path  # profiles/<name>/backup/gamestate.json

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, int, Path, bool]]) -> ProfileConfig:
        """Construct a ProfileConfig from a plain dictionary (e.g. loaded from JSON)."""
        return cls(
            name=data["name"],
            sshKey=data["sshKey"],
            createdAt=data["createdAt"],
            lastModifiedAt=data["lastModifiedAt"],
            is_active=data["is_active"],
            profile_path=Path(data["profile_path"]),
            backup_path=Path(data["backup_path"]),
            save_path=Path(data["save_path"]),
            game_state_path=Path(data["game_state_path"]),
            backup_game_state_path=Path(data["backup_game_state_path"]),
        )
