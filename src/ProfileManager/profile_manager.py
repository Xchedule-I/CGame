import shutil
from typing import List

from src.ProfileManager.directory import DirectoryManager
from src.ProfileManager.profile_data import ProfileConfig


class ProfileManager:
    """Manages the lifecycle of CGAME profiles.

    Disk is the single source of truth — no in-memory list is maintained.
    """

    def __init__(self, dir_obj: DirectoryManager) -> None:
        self.dir_obj = dir_obj

    # ------------------------------------------------------------------ #
    # Profile operations                                                 #
    # ------------------------------------------------------------------ #

    def get_profiles_name(self) -> List[str]:
        """Return profile names that actually exist as folders on disk."""
        profiles_dir = self.dir_obj.profiles_dir
        if not profiles_dir.exists():
            return []
        return [p.name for p in profiles_dir.iterdir() if p.is_dir()]

    def profile_exists(self, profile: ProfileConfig) -> bool:
        """Check whether a profile's directory exists on disk."""
        return self.dir_obj.get_profile_path(profile.name).is_dir()

    def profile_size(self) -> int:
        """Number of profiles on disk."""
        return len(self.get_profiles_name())


    def create_profile(self, profile: ProfileConfig) -> None:
        """Create the full directory structure for a new profile on disk.

        Creates:
            profiles/<name>/
            profiles/<name>/saves/       ← gamestate.json will live here
            profiles/<name>/backup/      ← backup copy of gamestate.json
        """
        self.dir_obj.setup_profile_directories(profile.name)

    def activate_profile(self, profile: ProfileConfig) -> None:
        """Activate a profile and load its game state.

        Expected flow:
            1. Verify profile exists on disk via profile_exists().
            2. Read game_state_path (saves/gamestate.json) into a GameState object.
            3. Mark profile as active (profile.is_active = True).
            4. Hand the GameState off to the game engine to begin the session.
        """
        pass

    def exit_profile(self, profile: ProfileConfig) -> None:
        """Save the current game state and exit the active profile cleanly.

        Expected flow:
            1. Serialize current GameState → write to game_state_path (saves/gamestate.json).
            2. Copy saves/gamestate.json → backup/gamestate.json (via create_backup).
            3. Update profile.lastModifiedAt timestamp.
            4. Mark profile as inactive (profile.is_active = False).
        """
        pass


    def remove_profile(self, profile: ProfileConfig) -> None:
        """Permanently delete a profile's directory from disk."""
        profile_path = self.dir_obj.get_profile_path(profile.name)
        if profile_path.is_dir():
            shutil.rmtree(profile_path)

    def create_backup(self, profile: ProfileConfig) -> None:
        """
        Future Based implementation needed for export | Import profiles
        """
        pass

    def load_profile(self) -> None:
        """
        Future Based implementation needed for export | Import profiles
        """
        pass
