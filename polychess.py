#python-chess import
#https://github.com/niklasf/python-chess
import chess
#import polyglot as pg
import chess.polyglot
import polyglot as pg
import random

#SVG render for the board is possible in Jupyter Notebook
#board

#get all the legal moves for the current position

def initBoard():
    return chess.Board()

def displayBoard(board):
    print(board)

def chooseGameType():
    #Display menu
    #Select gameType
    liste = [1,2]
    erreur = False
    print("------------------------------")
    print("Choisir le mode de jeu :")
    print("1- Joueur contre Joueur")
    print("2- Joueur contre IA")
    gameType = input("Saisissez le mode : ")

    try:
        if(not int(gameType) in liste):
            erreur = True
    except: 
        erreur = True
    if(erreur):
        print("------------------------------")
        print("Erreur de saisie")
        chooseGameType()


    return int(gameType)


def startRound(board, playerType):
    #Get the move related with the playerType
    move = None
    print(board.turn)
    if(playerType == 1):
        move = getPlayerMove(board)
    elif(playerType == 2):
        move = getIAMove(board)

    #Make a move
    current_board = makeMove(board, move)
    return current_board

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

    #If no deplacement
    if not deplacement:
        #Déplacement de l'IA de facon aléatoire
        deplacement = random.choice(list(board.legal_moves))

        #Déplacement de l'IA avec l'algorithme de minmax
        #EN COURS

        #val, deplacement = minmax(board,1)



    return(str(deplacement))



def makeMove(board,move):
    #Make a move on the board
    deplacement = chess.Move.from_uci(str(move))
    board.push(deplacement)

    displayBoard(board)

    return board

def chessGame():
    #Create a game
    #Initialization 
    board = initBoard()
    #Choose the game type
    gameType = chooseGameType()
    
    displayBoard(board)

    #If the game is not over
    while not board.is_game_over():
        #Make a round related with the game type
        if gameType == 1:
            board = startRound(board, 1)
            if not board.is_game_over():
                board = startRound(board, 1)
        elif gameType == 2:
            board = startRound(board, 1)
            if not board.is_game_over():
                board = startRound(board, 2)

    print("The game is over")
    print(board.result())


def minmax(board, depth):
    moves = list(board.legal_moves)
    bestMove = None

    if depth == 0 or len(moves) == 0:
        return 0, None

    print(depth)

    if(not board.turn):
        value = -9999
        #print("ia")
        for move in moves:

            deplacement = chess.Move.from_uci(str(move))
            #do the move
            board.push(deplacement)
            
            val,current_move = minmax(board, depth-1)

            #undo the move
            board.pop()
            
            if(val > value):
                value = val
                bestMove = current_move

    else:
        #print("j")
        value = 9999
        for move in moves:
    
            #do the move
            board.push(chess.Move.from_uci(str(move)))
            
            val,current_move = minmax(board, depth-1)

            #undo the move
            board.pop()
            if(val < value):
                value = val
                bestMove = current_move

    return value, bestMove


    """
    function minimax(node, depth, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, minimax(child, depth − 1, FALSE))
        return value
    else (* minimizing player *)
        value := +∞
        for each child of node do
            value := min(value, minimax(child, depth − 1, TRUE))
        return value
    """

chessGame()
"""
moves = board.legal_moves

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
