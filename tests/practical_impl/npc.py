from typing import ClassVar, Final, override

from textual.app import ComposeResult
from textual.binding import BindingType
from textual.containers import Center, Middle
from textual.screen import ModalScreen
from textual.widgets import Label

# NPC Co-ordinates (Hardcoded for now)
NPC_X: Final[int] = 10
NPC_Y: Final[int] = 5

class DialogScreen(ModalScreen[None]) :
    """A Popup screen that acts as a dialog box"""

    BINDINGS: ClassVar[list[BindingType]] = [
        ("space", "dismiss", "Close Dialog")
    ]

    @override
    def compose(self) -> ComposeResult:
        with Center() :
            with Middle() :
                yield Label(
                    "Hello traveller, it is dangerous to go alone. \n\n[Press SPACE to close]",
                    id="dialog_box"
                )
