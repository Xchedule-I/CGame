from typing import ClassVar, override

from textual.app import App, ComposeResult
from textual.binding import BindingType
from textual.reactive import reactive
from textual.widgets import Static

# Import our custom state handlers
from state import load_state, save_state

MAP_WIDTH: int = 20
MAP_HEIGHT: int = 10

class GameMap(Static):
    # 1. State mgmt : Reactives handle automatic UI updates
    player_x: reactive[int] = reactive(MAP_WIDTH // 2)
    player_y: reactive[int] = reactive(MAP_HEIGHT // 2)

    def on_mount(self) -> None:
        """Called automatically when the widget is added to the screen."""
        saved_x, saved_y = load_state(MAP_WIDTH // 2, MAP_HEIGHT // 2)
        self.player_x = saved_x
        self.player_y = saved_y

    @override
    def render(self) -> str:
        lines: list[str] = []
        for y in range(MAP_HEIGHT) :
            row: str = ""
            for x in range(MAP_WIDTH) :
                if x == self.player_x and y == self.player_y :
                    row += "P"
                else :
                    row += "."
            lines.append(row)

        return "\n".join(lines)

class GameApp(App[None]) :
    BINDINGS: ClassVar[list[BindingType]] = [
        ("q", "quit", "Quit"),
        ("w", "move_up", "Up"),
        ("s", "move_down", "Down"),
        ("a", "move_left", "Left"),
        ("d", "move_right", "Right"),
    ]

    @override
    def compose(self) -> ComposeResult :
        yield GameMap()

    def action_move_up(self) -> None:
        game_map = self.query_one(GameMap)
        if game_map.player_y > 0:
            game_map.player_y -= 1
            save_state(game_map.player_x, game_map.player_y)

    def action_move_down(self) -> None: 
        game_map = self.query_one(GameMap)
        if game_map.player_y < MAP_HEIGHT - 1 :
            game_map.player_y += 1
            save_state(game_map.player_x, game_map.player_y)

    def action_move_left(self) -> None: 
        game_map = self.query_one(GameMap)
        if game_map.player_x > 0 :
            game_map.player_x -= 1
            save_state(game_map.player_x, game_map.player_y)

    def action_move_right(self) -> None: 
        game_map = self.query_one(GameMap)
        if game_map.player_x < MAP_WIDTH - 1 :
            game_map.player_x += 1
            save_state(game_map.player_x, game_map.player_y)


if __name__ == "__main__" :
    app = GameApp()
    _ = app.run()
