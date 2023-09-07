import colorama


def main() -> list:
    BOARD_SIZE = 5
    
    board = createBoard(BOARD_SIZE)

    colorama.init()
    
    if nQueen(board, row_idx=0, queen=(colorama.Fore.BLUE + str(1) + colorama.Fore.RESET)):
        print("Here is the solution:")
        printBoard(board)
        
    colorama.deinit()


def nQueen(board: list, row_idx: int, queen) -> bool:
    
    N = len(board)
    
    # Base condition
    if row_idx >= N:
        return True
    
    # MAIN BACKTRACKING SECTION
    # Conditions to check
    for i in range(N):
        if isSafe(board, row_idx, i, queen):
            board[row_idx][i] = queen 

            # Backtracking Part
            if nQueen(board, row_idx + 1, queen):
                return True
            
            # Modify earlier decision
            board[row_idx][i] = 0
            
    return False


def createBoard(n: int) -> list:
    """Returns a nxn board in form of a list"""
    board = [[0] * n for _ in range(n)]
    return board


def printBoard(board):
    for row in board:
        for item in row:
            print(str(item), end=" ")
        print()


def isSafe(board: list, row: int, col: int, queen) -> bool:
    """Checks if the position provided is safe to place a queen"""
    
    # For Row
    if queen in board[row]:
        return False
            
    # For Column
    if queen in [r[col] for r in board]:
        return False
    
    # For Quad 1
    def isSafeinQuad1(board: list , row: int, col: int) -> bool:
        while col < len(board) and row >= 0:
            if board[row][col] == queen:
                return False
            row -=1
            col +=1
        return True 
    
    # For Quad 2
    def isSafeinQuad2(board: list , row: int, col: int) -> bool:
        while col >= 0 and row >= 0:
            if board[row][col] == queen:
                return False
            row -=1
            col -=1 
        return True
    
    # For Quad 3
    def isSafeinQuad3(board: list , row: int, col: int) -> bool:
        while col >= 0 and row < len(board):
            if board[row][col] == queen:
                return False
            row +=1
            col -=1 
        return True
    
    # For Quad 4
    def isSafeinQuad4(board: list , row: int, col: int) -> bool:
        while col < len(board) and row < len(board):
            if board[row][col] == queen:
                return False
            row +=1
            col +=1 
        return True
    
    # For all Quads
    if not (isSafeinQuad1(board, row, col) and isSafeinQuad2(board, row, col) and isSafeinQuad3(board, row, col) and isSafeinQuad4(board, row, col)):
        return False
    
    return True


#======================RUN=======================#

main()

#==============================#
# Normal Board
def bPrint(size):
    print()
    for r in createBoard(size):
        for c in r:
            print(c, end=" ")
        print()
        
# bPrint(10)
