import tkinter as tk
from typing import Protocol

## Constants
    # title
TITLE = "Pathfinding Visualizer"
    # window size
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
    # canvas size
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

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
        # create & pack frame
        self.frame = tk.Frame(self, padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # establish builder patterns of self.frame
        self.build_canvas()
        self.build_control_panel()

    def build_canvas(self) -> None:
        # create & pack canvas
        self.canvas = tk.Canvas(self.frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack(side=tk.TOP, fill=tk.X)
        self.reset_drawpoint()
        self.canvas.bind("<B1-Motion>", self.draw_line)
        #self.canvas.bind("<ButtonRelease-1>", self.set_drawpoint)
    
    def build_control_panel(self) -> None:
        # create & pack control panel
        self.control_panel = tk.Frame(self.frame)
        self.control_panel.pack(side=tk.TOP, fill=tk.Y)
        
        # create & pack control panel widgets
        self.build_algo_selector()
        self.build_start_button()
        self.build_clear_button()
        
    def build_algo_selector(self) -> None:
        # create & pack algo selector
        self.algo_selector = tk.OptionMenu(self.control_panel, tk.StringVar(), "Dijkstra", "A*", "BFS", "DFS")
        self.algo_selector.pack(side=tk.TOP, fill=tk.X)
        
    def build_start_button(self) -> None:
        # create & pack start button
        self.start_button = tk.Button(self.control_panel, text="Start", command=self.start_solver)
        self.start_button.pack(side=tk.TOP, fill=tk.X)
        
    def build_clear_button(self) -> None:
        # create & pack clear button
        self.clear_button = tk.Button(self.control_panel, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.TOP, fill=tk.X)
    
    
    def draw_line(self, event) -> None:
        self.canvas.create_line(self.last_x, self.last_y, event.x, event.y)
        self.last_x = event.x
        self.last_y = event.y
        
    def clear_canvas(self) -> None:
        self.canvas.delete("all")
        self.reset_drawpoint()
        
    def reset_drawpoint(self) -> None:
        ''' reset drawpoint to (0, 0) '''
        self.last_x = 0
        self.last_y = 0
            
    def start_solver(self) -> None:
        pass
    
    def update_view(self, event=None) -> None:
        ...