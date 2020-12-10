#python-chess import
#https://github.com/niklasf/python-chess
import chess
#import polyglot as pg


#SVG render for the board is possible in Jupyter Notebook
#board

#get all the legal moves for the current position

def initBoard():
    return chess.Board()

def displayBoard(board):
    print(board)

def chooseGameType():
    #Display different type de partie
    #JvsJ
    #JvsIA
    #...
    gameType = 1
    return gameType

def startRound(board, gameType):
    #Appeler le type de partie en fonction du type de partie
    move = None

    if(gameType == 1):
        move = getPlayerMove(board)

    current_board = makeMove(board, move)
    return current_board

def getPlayerMove(board):

    validDeplacement = False
    moves = board.legal_moves

    print("----------------------------------------")
    deplacement = input("De quelle case voulez vous partir et quelle tache voulez vous aller ?\n")

    for move in list(moves):
        if(deplacement == chess.Move.uci(move)):
            validDeplacement = True
    
    if(not validDeplacement):
        print("Erreur de saisie : aucun mouvement possible ne correspond a votre saisie")      
        return getPlayerMove(board)

    
    

    return deplacement

    

def makeMove(board,move):
    deplacement = chess.Move.from_uci(move)
    board.push(deplacement)

    displayBoard(board)

    return board

def chessGame():
    board = initBoard()
    gameType = chooseGameType()
    
    displayBoard(board)

    while not board.is_game_over():
        board = startRound(board, gameType)



    print("The game is over")
    print(board.result())

chessGame()
"""
#iterate over all the moves
for move in moves: 
    
    #display the move
    print(move)

    #save the current position
    current_board = board
    
    #do the move
    board.push(move)
    
    #display the board
    print(board)
    
    #number of black moves
    print("Black moves:" + str(board.legal_moves.count()))
    
    #undo the move
    board.pop()
    


    #do we have a winner?
    if (board.is_game_over()):
        print("The game is over")
        print(board.result())
"""  
