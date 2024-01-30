import tkinter as tk
from typing import Protocol

## Constants
    # title
TITLE = "Pathfinding Visualizer"
    # window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

class Presenter(Protocol):
    def update_view(self, event=None) -> None:
        ...

class View(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title(TITLE)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False, False)
        
    def init_ui(self, presenter: Presenter) -> None:
        self.frame = tk.Frame(self, padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
    def update_view(self, event=None) -> None:
        ...