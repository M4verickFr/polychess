import chess
import chess.polyglot

import tools

#SVG render for the board is possible in Jupyter Notebook
#board

def main():
    """Main function for playing chess game with the console
    """
    playerType = tools.menu()

    board = tools.initBoard()
    tools.displayBoard(board)

    players = [0, playerType]
    #random.shuffle(players)
    
    #If the game is not over
    while not board.is_game_over():
        board = tools.makeMove(board, players[0])
        if not board.is_game_over():
            board = tools.makeMove(board, players[1])
    
    print("The game is over")
    print(board.result())
    tools.renderSVG(board)

# Calls the main function

if __name__ == "__main__":
    main()

