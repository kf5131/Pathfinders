import tkinter as tk

## PARAMS ##
BOARD_HEIGHT = 32
BOARD_WIDTH = 32

## END PARAMS ##


class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pathfinder Algo Shootout")
        
        # Other initialization code can go here
        
        # Create and configure widgets
        self.create_widgets()

    def create_widgets(self):
        # Create and place your widgets here
        label = tk.Label(self.root, text="Hello, Tkinter!")
        label.pack(pady=10)

        button = tk.Button(self.root, text="Click Me", command=self.on_button_click)
        button.pack()
        
    def create_board(self, height, width):
        ...

    def on_button_click(self):
        # Define the behavior when the button is clicked
        print("Button clicked!")

def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
