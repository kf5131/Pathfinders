import tkinter as tk
from typing import Protocol

## Constants
    # title
TITLE = "Pathfinding Visualizer"
    # window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600



class View():
    def __init__(self, model):
        self.model = model

    def show(self):
        print(self.model.get())