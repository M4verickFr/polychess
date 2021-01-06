import chess 

pawn = [
    [0,  0,  0,  0,  0,  0,  0,  0],
    [50, 50, 50, 50, 50, 50, 50, 50],
    [10, 10, 20, 30, 30, 20, 10, 10],
    [5,  5, 10, 25, 25, 10,  5,  5],
    [0,  0,  0, 20, 20,  0,  0,  0],
    [5, -5,-10,  0,  0,-10, -5,  5],
    [5, 10, 10,-20,-20, 10, 10,  5],
    [0,  0,  0,  0,  0,  0,  0,  0]
]

knight = [
    [-50,-40,-30,-30,-30,-30,-40,-50],
    [-40,-20,  0,  0,  0,  0,-20,-40],
    [-30,  0, 10, 15, 15, 10,  0,-30],
    [-30,  5, 15, 20, 20, 15,  5,-30],
    [-30,  0, 15, 20, 20, 15,  0,-30],
    [-30,  5, 10, 15, 15, 10,  5,-30],
    [-40,-20,  0,  5,  5,  0,-20,-40],
    [-50,-40,-30,-30,-30,-30,-40,-50]
]

queen = [
    [-20,-10,-10, -5, -5,-10,-10,-20],
    [-10,  0,  0,  0,  0,  0,  0,-10],
    [-10,  0,  5,  5,  5,  5,  0,-10],
    [-5,  0,  5,  5,  5,  5,  0, -5],
    [0,  0,  5,  5,  5,  5,  0, -5],
    [-10,  5,  5,  5,  5,  5,  0,-10],
    [-10,  0,  5,  0,  0,  0,  0,-10],
    [-20,-10,-10, -5, -5,-10,-10,-20]
]

bishop = [
    [-20,-10,-10,-10,-10,-10,-10,-20],
    [-10,  0,  0,  0,  0,  0,  0,-10],
    [-10,  0,  5, 10, 10,  5,  0,-10],
    [-10,  5,  5, 10, 10,  5,  5,-10],
    [-10,  0, 10, 10, 10, 10,  0,-10],
    [-10, 10, 10, 10, 10, 10, 10,-10],
    [-10,  5,  0,  0,  0,  0,  5,-10],
    [-20,-10,-10,-10,-10,-10,-10,-20]
]

rook = [
    [-50,  -40,  0,  0,  0,  0,  -40,  -50],
    [-5, 10, 10, 10, 10, 10, 10,  5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [0,  0,  0,  5,  5,  0,  0,  0]
]

king = [
    [-30,-40,-40,-50,-50,-40,-40,-30],
    [-30,-40,-40,-50,-50,-40,-40,-30],
    [-30,-40,-40,-50,-50,-40,-40,-30],
    [-30,-40,-40,-50,-50,-40,-40,-30],
    [-20,-30,-30,-40,-40,-30,-30,-20],
    [-10,-20,-20,-20,-20,-20,-20,-10],
    [20, 20,  0,  0,  0,  0, 20, 20],
    [20, 30, 10,  0,  0, 10, 30, 20]
]


def convert_square(square,is_white):
    if(is_white):
        row = 7 - (square // 8)
    else:
        row = square // 8

    column = square % 8
    return [row, column]

def piece_value(piece, square):
    symbol = piece.symbol()
    is_white = not symbol.islower()
    symbol = symbol.islower()

    pos = convert_square(square, is_white)

    score = 0
    if symbol == 'p':
        score = (pawn[pos[0]][pos[1]])
    elif symbol == 'n':
        score = (knight[pos[0]][pos[1]])
    elif symbol == 'b':
        score = (bishop[pos[0]][pos[1]])
    elif symbol == 'r':
        score = (rook[pos[0]][pos[1]])
    elif symbol == 'q':
        score = (queen[pos[0]][pos[1]])
    elif symbol == 'k':
        score = (king[pos[0]][pos[1]])
        
    return score



def getValueBoard(board):
    materialWt = 0

    for i in range(1,6):
        val_w = 0
        val_b = 0

        for square in board.pieces(i, True):
            if(board.piece_at(square) != None):
                val_w += piece_value(board.piece_at(square),square)

        for square in board.pieces(i, False):
            if(board.piece_at(square) != None):
                val_b += piece_value(board.piece_at(square),square)

        if(i == 1):
            materialWt += 100 * (val_w-val_b)
        elif(i == 2):
            materialWt += 280 * (val_w-val_b)
        elif(i == 3):
            materialWt += 320 * (val_w-val_b)
        elif(i == 4):
            materialWt += 489 * (val_w-val_b)
        elif(i == 5):
            materialWt += 929 * (val_w-val_b)
        elif(i == 6):
            materialWt += 60000 * (val_w-val_b)

    mobilityWt = 3 * (len(list(board.legal_moves)))

    w_or_b = -1 if board.turn else 1

    score = (materialWt + mobilityWt) * w_or_b
    return score
