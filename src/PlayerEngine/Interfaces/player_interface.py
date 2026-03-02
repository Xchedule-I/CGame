from abc import ABC, abstractmethod


class PlayerInterface(ABC):

    @abstractmethod
    def move_to(self, **kwargs): ...

    @abstractmethod
    def get_position(self, **kwargs): ...

    @abstractmethod
    def get_speed(self, **kwargs): ...

    @abstractmethod
    def set_speed(self, **kwargs): ...

    @abstractmethod
    def set_position(self, **kwargs): ...

    @abstractmethod
    def set_map_window_size(self, **kwargs): ...
