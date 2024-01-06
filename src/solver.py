import heapq

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.char = ' '
        
    def __str__(self) -> str:
        return self.char
    def __repr__(self) -> str:
        return self.char
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y 

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
    
    def __lt__(self, other) -> bool:
        return (self.x, self.y) < (other.x, other.y)
    
    def __le__(self, other) -> bool:
        return (self.x, self.y) <= (other.x, other.y)
    
    def __gt__(self, other) -> bool:
        return (self.x, self.y) > (other.x, other.y)
    
    def __ge__(self, other) -> bool:
        return (self.x, self.y) >= (other.x, other.y)
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))     

class Start(Point):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.char = 'S'
        
class End(Point):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.char = 'E'
        
class Obstacle(Point):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.char = '\u2588'


class Node:
    def __init__(self, point: Point, parent) -> None:      
        self.point = point
        self.parent = parent
        
        self.g = 0
        self.h = 0
        self.f = 0


class Board:
    def __init__(self) -> None:
        self.height = 8
        self.width = 8
        self.board = [[Point(x, y) for x in range(self.width)] for y in range(self.height)]
        
    def print_board(self):
        print('+' + '-' * (self.width) + '+')
        for row in self.board:
            row = '|' + ''.join([str(point) for point in row]) + '|'
            print(row)
        print('+' + '-' * (self.width) + '+')
             
    def set_cell(self, x, y, value):
        self.board[y][x] = value
    
    def make_obstacle(self):
        '''Makes an arbirtary obstacle on the board'''
        x = 6
        y = 4
        for i in range(0, 3):
            self.set_cell(x, i, Obstacle(x, i))
        for j in range(3, 5):
            self.set_cell(j, y, Obstacle(j, y))
            
    def make_start(self, x, y):
        '''Makes the starting point on the board'''
        self.set_cell(x, y, Start(x, y))
    
    def get_start(self):
        '''Returns the starting point on the board'''
        for row in self.board:
            for point in row:
                if isinstance(point, Start):
                    return point
    
    def make_end(self, x, y):
        '''Makes the ending point on the board'''
        self.set_cell(x, y, End(x, y))
        
    def get_end(self):
        '''Returns the ending point on the board'''
        for row in self.board:
            for point in row:
                if isinstance(point, End):
                    return point
    
    def get_cell(self, x, y):
        '''Returns the value of the cell at the given coordinates'''
        return self.board[y][x] 
                
    def is_valid(self, x, y):
        '''Checks if the given coordinates are valid'''
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False
        return True
    
    def is_obstacle(self, x, y):
        '''Checks if the given coordinates are an obstacle'''
        return isinstance(self.get_cell(x, y), Obstacle)
    
    
    def get_neighbors(self, x, y):
        '''Returns the neighbors of the given cell as a list of tuples'''
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0:
                    continue
                if self.is_valid(x + i, y + j):
                    neighbors.append((x + i, y + j))
        return neighbors
    
def mainloop(board):
    '''
    Main loop of the program.
    This function is called every frame of the program.
    '''
    # Dijkstra's algorithm
    start = board.get_start()
    end = board.get_end()
    queue = [(0, start)]
    visited = set()
    distances = {start: 0}
    previous = {}

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node == end:
            break
        if current_node in visited:
            continue
        visited.add(current_node)

        x, y = current_node.x, current_node.y  # Extract x and y coordinates
        for neighbor_x, neighbor_y in board.get_neighbors(x, y):  # Add y coordinate
            if board.is_obstacle(neighbor_x, neighbor_y):  # Skip if the neighbor is an obstacle
                continue
            neighbor = Point(neighbor_x, neighbor_y)
            distance = current_distance + 1  # Assuming all edges have weight 1
            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Retrieve the shortest path
    path = []
    current_node = end
    while current_node in previous:
        path.append(current_node)
        current_node = previous[current_node]
    path.append(start)
    path.reverse()

    # Print the shortest path
    for point in path:
        x, y = point.x, point.y
        board.set_cell(x, y, '*')
    board.print_board()
    
def main():
    # Create a board (Builder Pattern)
    board = Board()
    board.print_board()
    board.make_obstacle()
    board.make_start(0, 7)
    board.make_end(7, 0)
    board.print_board()
    
    
    # Main loop
    mainloop(board)
    
    ...
    
if __name__ == '__main__':
    main()