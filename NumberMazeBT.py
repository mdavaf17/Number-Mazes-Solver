import timeit

levels = ["Easy", "Moderate", "Hard", "Very Hard"]
totals = [20, 50, 100, 100]
dimensions = [(3, 3), (4, 3), (4, 4), (5, 3)]

class MazeGame:
    def __init__(self, rows, cols, goal_value, grid):
        self.rows = rows
        self.cols = cols
        self.maze = grid
        self.goal_value = goal_value
        self.goal_x = cols - 1
        self.goal_y = rows - 1
        self.visited = set()  # Initialize visited set
        self.explored_nodes = 1  # Initialize explored nodes counter
            
    def neighbors(self, x, y):
        for dx, dy, direction in [(-1, 0, 'Left'), (0, -1, 'Up'), (1, 0, 'Right'), (0, 1, 'Down')]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.cols and 0 <= ny < self.rows:
                yield nx, ny, direction
    
    def print_maze(self):
        for y, row in enumerate(self.maze):
            for x, num in enumerate(row):
                print(num, end="\t")
            print()
        print()
        print('Goal value:', self.goal_value)
    
    def find_path(self, x, y, current_sum, goal_value, path):
        """
        Recursive function to find a path from the starting position to the goal while respecting the given constraints.
        """
        # Base case: if the goal is reached and the sum is equal to the goal value
        if self.is_goal_reached(x, y, current_sum, goal_value):
            return True

        # Base case: if the goal is reached but the sum is not equal to the goal value
        if self.is_goal_unreachable(x, y, current_sum, goal_value):
            return False

        # Mark the current cell as visited
        self.visited.add((x, y))
        self.explored_nodes += 1

        # Iterate through the neighbors
        for nx, ny, direction in self.neighbors(x, y):
            if (nx, ny) not in self.visited:
                next_value = self.maze[ny][nx]
                path.append((nx, ny, direction))
                if self.find_path(nx, ny, current_sum + next_value, goal_value, path):
                    return True
                path.pop()  # Backtrack if the current path doesn't lead to the goal

        # Unmark the current cell as visited before backtracking
        self.visited.remove((x, y))

        # If no path found from this cell, return False
        return False
    
    def is_goal_reached(self, x, y, current_sum, goal_value):
        """
        Check if the current position is the goal and if the sum is equal to the goal value.
        """
        return x == self.goal_x and y == self.goal_y and current_sum == goal_value

    def is_goal_unreachable(self, x, y, current_sum, goal_value):
        """
        Check if the current position is the goal but the sum is not equal to the goal value.
        """
        return x == self.goal_x and y == self.goal_y and current_sum != goal_value

    def run_game(self):
        self.print_maze()
        print(f"Rows: {self.rows}, Columns: {self.cols}, Goal Value: {self.goal_value}")
        
        start_time = timeit.default_timer()
        path = self.solve_maze()
        end_time = timeit.default_timer()
        if path:
            total = 0
            print("Solver found a path:")
            for move in path:
                total += self.maze[move[1]][move[0]]  # Add the value of the current cell to the total
                print(f"{move[2]}({total})", end=" -> ")
            print('End')
            print("Number of explored nodes:", self.explored_nodes)
        else:
            print("No solution found.")
        
        print("Time taken:", end_time - start_time, "seconds")

    def solve_maze(self):
        start_x, start_y = 0, 0
        initial_sum = self.maze[start_y][start_x]
        initial_path = [(start_x, start_y, 'Start')]

        # Call the find_path function with appropriate arguments
        if self.find_path(start_x, start_y, initial_sum, self.goal_value, initial_path):
            return initial_path
        else:
            return None

def choose_level():
    print("Choose a difficulty level:")
    for i, level in enumerate(levels):
        print(f"{i + 1}. {level}")
    
    choice = int(input("Enter the number of your choice: ")) - 1
    if 0 <= choice < len(levels):
        return dimensions[choice][1], dimensions[choice][0], totals[choice]
    # else:
    #     print("Invalid choice. Defaulting to Easy level.")
    #     return totals[0]

if __name__ == "__main__":
    print('Welcome to Number Maze Solver using Backtracking Algorithm!')
    rows, cols, goal_value = choose_level()
    grid = []
    for i in range(rows):
        row = input(f"Enter {cols} numbers for row {i + 1}: ").split()
        grid.append([int(num) for num in row])
    game = MazeGame(rows, cols, goal_value, grid)
    game.run_game()