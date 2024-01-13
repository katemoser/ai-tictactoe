"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[X, EMPTY, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, X]]


def player(board):
    """
    Returns player who has the next turn on a board. (X or O)
    """

    num_x = 0
    num_o = 0

    for row in board:
        for cell in row:
            if cell == X:
                num_x +=1
            if cell == O:
                num_o += 1
    #  TODO: change to less than or equal to??
    return X if num_x == num_o else O

    # get num x and num o on board
    # if nums are equal, it is X, else O
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    board_width = len(board[0])
    board_height = len(board)

    for row_index in range(board_height):
        for col_index in range(board_width):
            if board[row_index][col_index] == EMPTY:
                possible_actions.add((row_index, col_index))

    return possible_actions
    # return coords of all empty cells
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    curr_player = player(board)
    new_board_state = copy.deepcopy(board)
    (row_index, col_index) = action
    new_board_state[row_index][col_index] = curr_player

    return new_board_state

    # make deep copy of current state, add in action, return
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # TODO: Needs huge refactor

    board_width = len(board[0])
    board_height = len(board)

    found_winner = True
    # check vertical
    for row in board:
        found_winner = all(cell == row[0] for cell in row)
        if found_winner:
            return row[0]

    # check horizontal
    for col_index in range(board_width):
        col = []
        for row_index in range(board_height):
            col.append(board[row_index][col_index])
        found_winner = all(cell == col[0] for cell in col)
        if found_winner:
            return row[0]


    # check diagonals
    diag_lr = [board[0][0], board[1][1], board[2][2]]
    found_winner = all(cell == diag_lr[0] for cell in diag_lr)
    if found_winner:
        return diag_lr[0]
    diag_rl = [board[0][2], board[1][1], board[2][0]]

    found_winner = all(cell == diag_rl[0] for cell in diag_rl)
    if found_winner:
        return diag_rl[0]

    return None
    # checks for 3 in a row of X or O
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    #
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
