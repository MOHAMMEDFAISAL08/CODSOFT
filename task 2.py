import math

# Constants for players
PLAYER = 'O'  # Human player
AI = 'X'      # AI player

# Function to print the board
def print_board(board):
    for row in board:
        print(' '.join([cell if cell else '-' for cell in row]))
    print()

# Check if a player has won
def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Row
            return True
        if all(board[j][i] == player for j in range(3)):  # Column
            return True
    if all(board[i][i] == player for i in range(3)):      # Main diagonal
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Anti-diagonal
        return True
    return False

# Check if the board is full (draw)
def is_draw(board):
    return all(all(cell for cell in row) for row in board)

# Minimax function
def minimax(board, is_maximizing):
    if is_winner(board, AI):  # AI wins
        return 10
    if is_winner(board, PLAYER):  # Human wins
        return -10
    if is_draw(board):  # Draw
        return 0

    if is_maximizing:  # AI's turn
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if not board[i][j]:  # Check if the cell is empty
                    board[i][j] = AI
                    score = minimax(board, False)
                    board[i][j] = None  # Undo the move
                    best_score = max(best_score, score)
        return best_score
    else:  # Human's turn
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if not board[i][j]:  # Check if the cell is empty
                    board[i][j] = PLAYER
                    score = minimax(board, True)
                    board[i][j] = None  # Undo the move
                    best_score = min(best_score, score)
        return best_score

# Find the best move for the AI
def find_best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if not board[i][j]:  # Check if the cell is empty
                board[i][j] = AI
                score = minimax(board, False)
                board[i][j] = None  # Undo the move
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Main game loop
def main():
    # Initialize the board (3x3 grid)
    board = [[None for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O', and AI is 'X'")
    print_board(board)

    while True:
        # Human move
        x, y = map(int, input("Enter your move (row and column, 0-2): ").split())
        if board[x][y]:
            print("Invalid move! Try again.")
            continue
        board[x][y] = PLAYER

        # Check for endgame
        if is_winner(board, PLAYER):
            print_board(board)
            print("You win!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI move
        print("AI is making its move...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = AI

        # Check for endgame
        if is_winner(board, AI):
            print_board(board)
            print("AI wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Print the board after each turn
        print_board(board)

if __name__ == "__main__":
    main()
