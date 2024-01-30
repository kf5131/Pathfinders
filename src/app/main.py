from model import Model
from presenter import Presenter
from view import View



def main():
    model = Model()
    view = View()
    presenter = Presenter(model, view)
    presenter.run()


if __name__ == '__main__':
    main()