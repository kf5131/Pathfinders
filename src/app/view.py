import tkinter as tk
from typing import Protocol

## Constants
    # title
TITLE = "Pathfinding Visualizer"
    # window size
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
    # canvas size
CANVAS_WIDTH = WINDOW_WIDTH - 10
CANVAS_HEIGHT = WINDOW_HEIGHT - 10

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
        
        self.canvas = tk.Canvas(self.frame, bg='white',width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()
        
    def update_view(self, event=None) -> None:
        ...