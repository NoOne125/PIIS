import chess
from eval import getEval

def negascout(depth, board, alpha, beta):
    best_score = -99999
    b = beta
    if depth == 0:
        finalEval = getEval(board)
        if finalEval == None:
            return 0
        return -finalEval

    for move in board.legal_moves:
        board.push(move)
        score = -negascout(depth - 1, board, -b, -alpha)
        if score > best_score:
            if alpha < score < beta:
                best_score = max(score, best_score)
            else:
                best_score = -negascout(depth - 1, board, -beta, -score)

        board.pop()
        alpha = max(score, alpha)
        if alpha > beta:
            return alpha
        b = alpha + 1
    return best_score
