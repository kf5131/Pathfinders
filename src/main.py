import tkinter as tk

## PARAMS ##
BOARD_HEIGHT = 16
BOARD_WIDTH = 16

## END PARAMS ##


class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pathfinding Visualization")
        
        # Define grid dimensions
        self.rows = BOARD_HEIGHT
        self.columns = BOARD_WIDTH

        # Create a 2D list to store button references
        self.buttons = [[None] * self.columns for _ in range(self.rows)]

        # Create and configure widgets
        self.create_widgets()

    def create_widgets(self):
        # Create and place your widgets here
        label = tk.Label(self.root, text="Pathfinding Visualization")
        label.grid(row=0, column=0, columnspan=self.columns, pady=10)

        # Create the board of buttons
        self.create_board()

        button = tk.Button(self.root, text="Run Pathfinding", command=self.run_pathfinding)
        button.grid(row=1, column=0, columnspan=self.columns)

    def create_board(self):
        # Create a grid of buttons
        for i in range(self.rows):
            for j in range(self.columns):
                button = tk.Button(self.root, width=4, height=2, command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i+2, column=j)  # Adjusted row to avoid overlapping with label and button
                self.buttons[i][j] = button

    def on_button_click(self, i, j):
        # Callback function when a button is clicked
        button = self.buttons[i][j]
        button.config(bg="blue", state=tk.DISABLED)
        print(f"Clicked button at row {i} column {j}")

    def run_pathfinding(self):
        # Placeholder for pathfinding algorithm
        # In a real project, you would implement a proper pathfinding algorithm here
        print("Running pathfinding algorithm")

def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
