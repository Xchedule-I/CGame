from pathlib import Path

from platformdirs import PlatformDirs


class DirectoryManager:
    """Manages the directory structure for CGAME and user profiles.

    On-disk layout:
        root_dir/
        └── profiles/
            └── <profile_name>/
                ├── saves/
                │   └── gamestate.json
                └── backup/
                    └── gamestate.json
    """

    def __init__(self, app_name: str = "CGAME") -> None:
        self.dirs = PlatformDirs(
            appname=app_name,
            appauthor="BITS-Rohit"
        )

        self.root_dir = Path(self.dirs.user_data_dir)
        self.log_dir = Path(self.dirs.user_log_dir)

        # All profiles live under a single profiles/ folder at root
        self.profiles_dir = self.root_dir / "profiles"

    def setup_base_directories(self) -> None:
        """Ensure the base application directories exist."""
        self.root_dir.mkdir(parents=True, exist_ok=True)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.profiles_dir.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------ #
    # Profile-level paths                                                  #
    # ------------------------------------------------------------------ #

    def get_profile_path(self, profile_name: str) -> Path:
        """Root folder for a given profile."""
        return self.profiles_dir / profile_name

    def get_backup_path(self, profile_name: str) -> Path:
        """backup/ folder inside the given profile's directory."""
        return self.get_profile_path(profile_name) / "backup"

    def get_save_path(self, profile_name: str) -> Path:
        """saves/ folder inside the given profile's directory."""
        return self.get_profile_path(profile_name) / "saves"

    # ------------------------------------------------------------------ #
    # GameState file paths                                                 #
    # ------------------------------------------------------------------ #

    def get_game_state_path(self, profile_name: str) -> Path:
        """Path to the active game state JSON file for a profile.

        Location: saves/gamestate.json
        This is the file that gets loaded when a user activates a profile.
        """
        return self.get_save_path(profile_name) / "gamestate.json"

    def get_backup_game_state_path(self, profile_name: str) -> Path:
        """Path to the backup copy of the game state JSON for a profile.

        Location: backup/gamestate.json
        Written on exit_profile() before the session ends.
        """
        return self.get_backup_path(profile_name) / "gamestate.json"

    # ------------------------------------------------------------------ #
    # Directory bootstrap                                                  #
    # ------------------------------------------------------------------ #

    def setup_profile_directories(self, profile_name: str) -> None:
        """Ensure all required directories exist for a given profile.

        Structure created:
            root_dir/
            └── profiles/
                └── <profile_name>/
                    ├── saves/       ← gamestate.json lives here
                    └── backup/      ← backup copy of gamestate.json lives here
        """
        self.setup_base_directories()

        self.get_profile_path(profile_name).mkdir(parents=True, exist_ok=True)
        self.get_backup_path(profile_name).mkdir(parents=True, exist_ok=True)
        self.get_save_path(profile_name).mkdir(parents=True, exist_ok=True)
