
# Number Mazes Solver

This solver is an implementation of the backtracking algorithm to solve the Number Mazes game. Number Mazes is a puzzle game where players must navigate a grid of numbers with the goal of reaching a specific value through a valid path from the starting point to the endpoint.

## Game Rules

1. **Grid**: The game is played on a square or rectangular grid consisting of cells. Each cell contains a number, which can be positive, zero, or negative.

2. **Starting and Ending Points**: Each game begins from a designated starting cell and must end at a designated ending cell. Players must find a path from the starting point to the ending point.

3. **Path**: Players can move from one cell to another horizontally or vertically, but diagonal movement is not allowed. Each cell can only be visited once during the journey from the starting point to the ending point.

4. **Target Sum**: At each difficulty level, players must ensure that the sum of the numbers along the path from the starting point to the ending point meets a specific target sum:
   - **Easy**: 3x3 grid, the sum of the numbers along the path must be equal to 20.
   - **Moderate**: 4x3 grid, the sum of the numbers along the path must be equal to 50.
   - **Tough**: 4x4 or 5x3 grid, the sum of the numbers along the path must be equal to 100.

5. **Movement**: Players can move horizontally or vertically from one cell to the next, but diagonal movement is not permitted.

6. **Visited Cells**: Each cell in the grid can only be visited once during the journey from the starting point to the ending point.

By following these rules, players must find the correct path to solve the puzzle and reach the endpoint.

## Usage Instructions

1. Ensure you have Python installed on your computer.
2. Clone this repository to your computer.
3. Open a terminal and navigate to the directory where you saved the repository.
4. Run the solver by executing the `NumberMazeBF.py` for BruteForce Algorithm or `NumberMazeBT.py` for Backtracking Algorithm file using the following command:

```python
python NumberMazeBF.py
or 
python NumberMazeBF.py
```

5. Follow the on-screen instructions to input the grid of numbers and the desired difficulty level.
6. The solver will search for a solution and display the path found, if any.

## Author
| No. | Name                           | NIM |
|-----|--------------------------------|------------|
| 1.  | Muhammad Dava Fathurrahman      | 13522114   |


## References
https://www.dr-mikes-math-games-for-kids.com/number-mazes.html