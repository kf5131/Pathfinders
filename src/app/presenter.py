from __future__ import annotations

from typing import Protocol

from model import Model

class View(Protocol):
    def init_ui(self, presenter: Presenter) -> None:
        ...

class Presenter():
    def __init__(self, model: Model, view: View):
        self.view = view
        self.model = model

    def update_view(self):
        self.view.print(self.model.get_data())