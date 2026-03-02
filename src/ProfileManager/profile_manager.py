import shutil
from typing import List

from src.ProfileManager.profile_data import ProfileConfig
from src.ProfileManager.directory import DirectoryManager


class ProfileManager:
    """Manages the lifecycle of CGAME profiles.

    Disk is the single source of truth — no in-memory list is maintained.
    """

    def __init__(self, dir: DirectoryManager) -> None:
        self.dir = dir

    # ------------------------------------------------------------------ #
    # Disk-backed queries                                                  #
    # ------------------------------------------------------------------ #

    def get_profile_names_on_disk(self) -> List[str]:
        """Return profile names that actually exist as folders on disk."""
        profiles_dir = self.dir.profiles_dir
        if not profiles_dir.exists():
            return []
        return [p.name for p in profiles_dir.iterdir() if p.is_dir()]

    def get_profiles(self) -> List[str]:
        """Return all profile names currently on disk."""
        return self.get_profile_names_on_disk()

    def profile_exists(self, profile: ProfileConfig) -> bool:
        """Check whether a profile's directory exists on disk."""
        return self.dir.get_profile_path(profile.name).is_dir()

    def profile_size(self) -> int:
        """Number of profiles on disk."""
        return len(self.get_profile_names_on_disk())

    # ------------------------------------------------------------------ #
    # Profile operations                                                   #
    # ------------------------------------------------------------------ #

    def create_profile(self, profile: ProfileConfig) -> None:
        """Create the directory structure for a new profile on disk."""
        self.dir.setup_profile_directories(profile.name)

    def remove_profile(self, profile: ProfileConfig) -> None:
        """Permanently delete a profile's directory from disk."""
        profile_path = self.dir.get_profile_path(profile.name)
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
