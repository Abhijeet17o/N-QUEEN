# N-Queen Problem Solver

This Python script solves the N-Queen problem using backtracking. The N-Queen problem is a classic puzzle where the objective is to place N chess queens on an N×N chessboard so that no two queens threaten each other. In this implementation, we'll visualize the solution on the console.

## Getting Started

These instructions will help you run the script on your local machine.

### Prerequisites

Before running the script, ensure you have Python installed on your system. You'll also need the `colorama` library to display colored output in the console.

```bash
pip install colorama
```

## Algorithm Overview

The script uses backtracking to find a solution for the N-Queen problem. Here's a brief overview of the algorithm:

1. Start with an empty chessboard.
2. Place queens on the board row by row, starting from the first row.
3. For each queen placement, check if it's safe according to the rules of chess.
4. If a safe position is found, recursively try to place the next queen.
5. If all queens are successfully placed, return True; otherwise, backtrack and try a different position for the current queen.

## Script Structure

- `main.py`: Main Python script containing the implementation of the N-Queen solver algorithm.
- `colorama`: Library used for colorizing the output in the console.
- `README.md`: Markdown file containing information about the script and how to use it.

## Contributing

Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, feel free to open an issue or create a pull request.

## Contact

For any inquiries or support, please contact [abhijeetsapar17@gmail.com].

---
**Note**: The `bPrint(size)` function at the end of the script is for debugging purposes and can be ignored for normal usage.
