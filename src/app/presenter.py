from __future__ import annotations

from typing import Protocol

from model import Model

class View(Protocol):
    def init_ui(self, presenter: Presenter) -> None: 
        ...
        
    def mainloop(self) -> None: 
        ...

class Presenter():
    def __init__(self, model: Model, view: View):
        self.view = view
        self.model = model
        
    def update_something(self):
        print(self.model.get_data())
        
    def run(self):
        self.view.init_ui(self) # from Protocol
        self.update_something() # child class method
        self.view.mainloop() # from Protocol
