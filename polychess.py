import chess
import chess.polyglot
import random

import polyglot as pg
import evaluation

import chess.svg 


#SVG render for the board is possible in Jupyter Notebook
#board

def main():
    """
        -gameType(int): the type of the current player
        -0:Played by the console
        -1:Played with protocol UCI
    """
    gameType = 0
    """
        -playerType(int): the type of the current player
        -0:Played by a human
        -1:Played by Polyglot
    """
    playerTypeUCI = 0
    
    defaultGameType = [choosePlayerType, playerTypeUCI]

    if callable(defaultGameType[gameType]):
        playerType = defaultGameType[gameType]()
    else:
        playerType = defaultGameType[gameType]

    board = initBoard()
    displayBoard(board)

    players = [0, playerType]
    #random.shuffle(players)
    
    #If the game is not over
    while not board.is_game_over():
        board = makeMove(board, players[0])
        if not board.is_game_over():
            board = makeMove(board, players[1])
    
    print("The game is over")
    print(board.result())
    renderSVG(board)
    

def initBoard():
    return chess.Board()

def displayBoard(board):
    print(board)

def choosePlayerType():
    playersType = [0,1]
    print("------------------------------")
    print("Select game type :")
    print("0- Played versus Human")
    print("1- Played versus Polyglot")
    playerType = int(input("Enter selected mode : "))

    if(not playerType in playersType):
        print("------------------------------")
        print("Erreur de saisie")
        choosePlayerType()

    return playerType

def getMove(board, playerType):
    #Get the move related with the playerType
    move = None
    playerTypeMovesFunction = [
        getPlayerMove,
        getIAMove
    ]

    movesFunction = playerTypeMovesFunction[playerType]
    move = movesFunction(board)

    return move

#get all the legal moves for the current position

def getPlayerMove(board):
    #Display player movement selection
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


def getIAMove(board):
    #Get AI Movement
    maxWeight = 0
    deplacement = None

    #Get movement in the polyglot
    deplacement = pg.bestMove(board)
    print(deplacement)
    #If no deplacement
    if not deplacement:
        #Déplacement de l'IA de facon aléatoire
        deplacement = random.choice(list(board.legal_moves))

        #Déplacement de l'IA avec l'algorithme de minmax
        
        #val, deplacement = minmax(board,3)
        val, deplacement = minmaxAlphaBeta(board,3,1e-8,-1e-8)
        

    return(str(deplacement))

def makeMove(board, playerType):
    move = getMove(board, playerType)

    deplacement = chess.Move.from_uci(str(move))
    board.push(deplacement)

    displayBoard(board)

    return board


def minmax(board, depth):
    moves = list(board.legal_moves)
    bestMove = None

    if depth == 0 or len(moves) == 0:
        return evaluation.getValueBoard(board),bestMove

    if(board.turn):
        value = -1e-8
        for move in moves:
            deplacement = chess.Move.from_uci(str(move))
            #do the move
            board.push(deplacement)
            
            val, current_move = minmax(board, depth-1)

            #undo the move
            board.pop()
            
            if(val > value):
                value = val
                bestMove = move

    else:
        value = 1e-8
        for move in moves:

            #do the move
            deplacement = chess.Move.from_uci(str(move))
            #do the move
            board.push(deplacement)
            
            val,current_move = minmax(board, depth-1)

            #undo the move
            board.pop()
            if(val < value):
                value = val
                bestMove = move

    return value, bestMove

def minmaxAlphaBeta(board, depth, alpha, beta):
    moves = list(board.legal_moves)

    bestMove = None

    if depth == 0 or len(moves) == 0:
        return evaluation.getValueBoard(board),bestMove

    if(board.turn):
        value = -1e-8
        for move in moves:
            deplacement = chess.Move.from_uci(str(move))
            #do the move
            board.push(deplacement)
            
            val, current_move = minmaxAlphaBeta(board, depth-1, alpha, beta)

            #undo the move
            board.pop()
            
            if(val > value):
                value = val
                bestMove = move

            alpha = max(alpha, val)

            if(beta < alpha and bestMove):
                return value, bestMove

    else:
        value = 1e-8
        for move in moves:

            #do the move
            deplacement = chess.Move.from_uci(str(move))
            #do the move
            board.push(deplacement)
            
            val,current_move = minmaxAlphaBeta(board, depth-1, alpha, beta)

            #undo the move
            board.pop()
            if(val < value):
                value = val
                bestMove = move

            beta = min(beta, val)
            if(beta < alpha and bestMove):
                return value, bestMove

    return value, bestMove

def renderSVG(board):
    svg=open("chessrender.svg", "w") 
    svg.write(chess.svg.board(board))
    


# Calls the main function

if __name__ == "__main__":
    main()

