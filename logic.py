import math

def print_board_console(board):
    """Funzione di debug per stampare la board in console"""
    for i in range(3):
        row = board[3*i : 3*i+3]
        print(" | ".join(row))
        if i < 2:
            print("---------")

def check_winner(board):

    winning_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for (a,b,c) in winning_positions:
        if board[a] != '-' and board[a] == board[b] == board[c]:
            return board[a]
    if '-' not in board:
        return 'Draw'
    return None

def minimax(board, is_maximizing):

    result = check_winner(board)
    if result == 'X':
        return +1
    elif result == 'O':
        return -1
    elif result == 'Draw':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == '-':
                board[i] = 'X'
                score = minimax(board, False)
                board[i] = '-'
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == '-':
                board[i] = 'O'
                score = minimax(board, True)
                board[i] = '-'
                best_score = min(best_score, score)
        return best_score

def find_best_move(board, player):

    best_move = None
    
    if player == 'X':
        best_score = -math.inf
        for i in range(9):
            if board[i] == '-':
                board[i] = 'X'
                score = minimax(board, False)
                board[i] = '-'
                if score > best_score:
                    best_score = score
                    best_move = i
    else:  # 'O'
        best_score = math.inf
        for i in range(9):
            if board[i] == '-':
                board[i] = 'O'
                score = minimax(board, True)
                board[i] = '-'
                if score < best_score:
                    best_score = score
                    best_move = i
    return best_move