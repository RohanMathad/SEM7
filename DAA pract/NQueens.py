# Step 1: Print the board
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Step 2: Check if placing queen is safe
def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 'Q':
            return False
    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 'Q':
            return False
    return True

# Step 3: Backtracking to place queens
def solve(board, row, n):
    if row == n:   # all queens placed
        print("\nFinal N-Queen Matrix:")
        print_board(board)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            if solve(board, row + 1, n):  # go to next row
                return True
            board[row][col] = '.'  # backtrack

    return False

# Step 4: Main program
n = int(input("Enter number of Queens: "))
board = [['.' for _ in range(n)] for _ in range(n)]

print("Sample Board (Row & Column numbers):")
print("   0 1 2 3")
print("0  . . . .")
print("1  . . . .")
print("2  . . . .")
print("3  . . . .")
print("\nYou can use these numbers to choose where to place your first Queen.")

# 🟡 You place the first queen
r = int(input("Enter row for first queen (0-indexed): "))
c = int(input("Enter column for first queen (0-indexed): "))
board[r][c] = 'Q'

# 🧩 Start solving from next row
solve(board, r + 1, n)

# Step 5: Complexity
print("Time Complexity: O(N!)")
print("Space Complexity: O(N^2)")


"""
Explanation (super simple terms)
| Step | What Happens                             | Example        |
| ---- | ---------------------------------------- | -------------- |
| 1️⃣  | You place the first queen manually       | Example: (0,1) |
| 2️⃣  | Program starts from next row             | row = 1        |
| 3️⃣  | For each column → check if safe          |                |
| 4️⃣  | If safe → place queen → go to next row   |                |
| 5️⃣  | If stuck → backtrack (remove last queen) |                |
| 6️⃣  | When all queens placed → print matrix    |                |


Summary Table
| Concept                 | Description                    |
| ----------------------- | ------------------------------ |
| **Algorithm Type**      | Backtracking                   |
| **Data Structure Used** | 2D List (Matrix)               |
| **User Role**           | You place first queen manually |
| **Program Role**        | Backtracking fills rest        |
| **Time Complexity**     | O(N!)                          |
| **Space Complexity**    | O(N²)                          |

"""

#--------------------------------------------------------------------------------------

"""
Enter number of Queens: 4
Sample Board (Row & Column numbers):
   0 1 2 3
0  . . . .
1  . . . .
2  . . . .
3  . . . .

You can use these numbers to choose where to place your first Queen.
Enter row for first queen (0-indexed): 0
Enter column for first queen (0-indexed): 1

Final N-Queen Matrix:
. Q . .
. . . Q
Q . . .
. . Q .

Time Complexity: O(N!)
Space Complexity: O(N^2)
"""
