import chess
import chess.polyglot

def bestMove(board):
    """Find the best initial move

    Args:
        board (board): bord object from chess

    Returns:
        string: piece movement on the board, like "g2g4"
    """
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
