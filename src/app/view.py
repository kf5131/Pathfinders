import tkinter as tk
from typing import Protocol

## Constants
    # title
TITLE = "Pathfinding Visualizer"
    # window size
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 1000

class Presenter(Protocol):
    def handle_button_press(self, event: tk.Event) -> None:
        ...

class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False, False)
        
    def init_ui(self, presenter: Presenter) -> None:
        
        # create frames
            # upper frame
        self.upper_frame = tk.Frame(self,padx=10, pady=10)
        self.build_canvas()
        self.upper_frame.pack()
            # lower frame
        self.lower_frame = tk.Frame(self, padx=10, pady=10)
        self.build_controls()
        self.lower_frame.pack()
        
    def build_canvas(self) -> None:
        self.canvas = tk.Canvas(self.upper_frame, bg='white' ,width=WINDOW_WIDTH, height=WINDOW_HEIGHT-200)
        self.canvas.pack()
        
    def build_controls(self) -> None:
            # press me button
        self.button = tk.Button(self.lower_frame, text="Press Me!")
        self.button.pack()
            # clear button
        self.clear_button = tk.Button(self.lower_frame, text="Clear")
        self.clear_button.pack()
            # speed slider
        self.speed_slider = tk.Scale(self.lower_frame, from_=0, to=100, orient=tk.HORIZONTAL)
        self.speed_slider.pack()
            # algorithm dropdown
        self.algo = tk.StringVar()
        self.algo.set("A*")
        self.algorithm_dropdown = tk.OptionMenu(self.lower_frame, self.algo, "A*", "Dijkstra", "BFS", "DFS")
        self.algorithm_dropdown.pack()
        
        
        
        
        
        
        
    def draw_point(self, x: int, y: int, color: str) -> None:
        self.canvas.create_oval(x, y, x+10, y+10, fill=color)
        