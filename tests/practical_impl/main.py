from typing import ClassVar, cast, override

from textual.app import App, ComposeResult
from textual.binding import BindingType
from textual.reactive import reactive
from textual.widgets import Static

from state import load_state, save_state
from npc import NPC_X, NPC_Y, DialogScreen

class GameMap(Static):
    player_x: reactive[int] = reactive(0)
    player_y: reactive[int] = reactive(0)

    def on_mount(self) -> None:
        app_instance: App[None] = cast(App[None], self.app)
        term_width: int = app_instance.console.size.width
        term_height: int = app_instance.console.size.height

        saved_x, saved_y = load_state(term_width // 2, term_height // 2)
        self.player_x = saved_x
        self.player_y = saved_y

    @override
    def render(self) -> str:
        width: int = self.size.width
        height: int = self.size.height
        lines: list[str] = []

        for y in range(height) :
            row: str = ""
            for x in range(width) :
                if x == self.player_x and y == self.player_y :
                    row += "P"
                elif x == NPC_X and y == NPC_Y:
                    row += "N"
                else :
                    # Replaced the dot with an empty space!
                    row += " " 
            lines.append(row)

        return "\n".join(lines)

class GameApp(App[None]) :
    CSS: ClassVar[str] = """
    /* Give the whole app a soft, dark-slate background instead of pitch black */
    Screen {
        background: #282a36; 
    }

    GameMap {
        width: 100%;
        height: 100%;
        color: #f8f8f2; /* Light text so P and N are clearly visible */
    }

    /* Dim the map slightly when the dialog pops up */
    DialogScreen {
        align: center middle;
        background: rgba(0, 0, 0, 0.6); 
    }

    /* Style the dialog box to look like a clean RPG popup */
    #dialog_box {
        padding: 2 4;
        background: #44475a;
        color: #f8f8f2;
        border: thick #bd93f9;
        text-align: center;
    }
    """
    
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

    def try_move(self, dx: int, dy: int) -> None:
        """Helper to handle boundaries, collisions, and state saving."""
        game_map = self.query_one(GameMap)
        new_x: int = game_map.player_x + dx
        new_y: int = game_map.player_y + dy

        # Check for NPC collision
        if new_x == NPC_X and new_y == NPC_Y:
            _ = self.push_screen(DialogScreen())
            return 

        # Check map boundaries
        if 0 <= new_x < game_map.size.width and 0 <= new_y < game_map.size.height:
            game_map.player_x = new_x
            game_map.player_y = new_y
            save_state(new_x, new_y)

    def action_move_up(self) -> None:
        self.try_move(0, -1)

    def action_move_down(self) -> None: 
        self.try_move(0, 1)

    def action_move_left(self) -> None: 
        self.try_move(-1, 0)

    def action_move_right(self) -> None: 
        self.try_move(1, 0)


if __name__ == "__main__" :
    app = GameApp()
    _ = app.run()
