from __future__ import annotations

from typing import Protocol

from model import Model

class View(Protocol):
    def init_ui(self, presenter: Presenter) -> None:
        ...
        
    def update_view(self) -> None:
        ...

class Presenter():
    def __init__(self, model: Model, view: View):
        self.view = view
        self.model = model

    def update_view(self) -> None:
        data = self.model.get_data()
        self.view.update_view(data)
        
    def run(self) -> None:
        self.view.init_ui(self)
        self.update_view()
        self.view.mainloop()