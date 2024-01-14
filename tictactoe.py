"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # If the board is empty, X goes first
    if board == initial_state():
        return X

    # Else, count the number of X's and O's on the board
    x_count = 0
    o_count = 0
    for row in board:
        for col in row:
            if col == X:
                x_count += 1
            elif col == O:
                o_count += 1

    # If the number of X's is equal to the number of O's, it's X's turn
    if x_count == o_count:
        return X
    # Else, it's O's turn
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Create a set of all possible actions
    possible_actions = set()

    # Iterate through all the rows and columns of the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            # If the space is empty, it is a possible action
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    # Return the set of possible actions
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # If the action is not valid, raise an exception
    if action not in actions(board):
        raise Exception("Invalid action")

    # Create a deep copy of the board
    new_board = []
    for row in board:
        new_row = []
        for col in row:
            new_row.append(col)
        new_board.append(new_row)

    # Update the board with the new action
    new_board[action[0]][action[1]] = player(board)

    # Return the new board
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check for horizontal wins
    for row in board:
        if row[0] == row[1] and row[0] == row[2]:
            return row[0]

    # Check for vertical wins
    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]

    # Check for diagonal wins
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[0][2]

    # If no winner, return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If there is a winner, the game is over
    if winner(board) is not None:
        return True

    # If there are no more actions, the game is over
    if len(actions(board)) == 0:
        return True

    # If the game is not over, return False
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # If X has won, return 1
    if winner(board) == X:
        return 1

    # If O has won, return -1
    if winner(board) == O:
        return -1

    # If the game is a tie, return 0
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        value, move = max_value(board)
    else:
        value, move = min_value(board)

    return move

def max_value(board):
    """
    Calculate the highest value move for player X.
    """
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    best_move = None
    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > v:
            v = min_val
            best_move = action
        if v == 1:
            break

    return v, best_move

def min_value(board):
    """
    Calculate the lowest value move for player O.
    """
    if terminal(board):
        return utility(board), None

    v = float('inf')
    best_move = None
    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < v:
            v = max_val
            best_move = action
        if v == -1:
            break

    return v, best_move
