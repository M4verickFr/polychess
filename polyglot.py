import chess
import chess.polyglot

def bestMove(board):
    weight = 0
    bestMove = None
    with chess.polyglot.open_reader("bookfish.bin") as reader:
        for entry in reader.find_all(board):
            if entry.weight > weight:
                weight=entry.weight
                bestMove=entry.move
    return bestMove

# Testing our code
board = chess.Board()
