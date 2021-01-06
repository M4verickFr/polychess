import chess
import chess.polyglot
import random
import math

import polyglot as pg
import evaluation

import chess.svg 


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
    move = str(movesFunction(board))

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

    #If no deplacement
    if not deplacement:
        #Déplacement de l'IA de facon aléatoire
        deplacement = random.choice(list(board.legal_moves))

        #Déplacement de l'IA avec l'algorithme de minmax
        
        #val, deplacement = minmax(board,3)
        val, deplacement = minmaxAlphaBeta(board,5,-math.inf,math.inf)
        print(val)

    return deplacement

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

    if(not board.turn):
        value = -1e8
        for move in moves:
            deplacement = chess.Move.from_uci(str(move))
            #do the move
            board.push(deplacement)
            
            val, current_move = minmax(board, depth-1)

            #undo the move
            board.pop()
            
            if(val > value or not bestMove):
                value = val
                bestMove = move

    else:
        value = 1e8
        for move in moves:

            #do the move
            deplacement = chess.Move.from_uci(str(move))
            #do the move
            board.push(deplacement)
            
            val,current_move = minmax(board, depth-1)

            #undo the move
            board.pop()
            if(val < value or not bestMove):
                value = val
                bestMove = move
    print(bestMove)
    return value, bestMove

"""
def minmaxAlphaBeta(board, depth, alpha, beta):
    moves = list(board.legal_moves)

    bestMove = None

    if depth == 0 or len(moves) == 0:
        return evaluation.getValueBoard(board),bestMove

    if(board.turn):
        value = -1e8
        for move in moves:
            deplacement = chess.Move.from_uci(str(move))
            #do the move
            board.push(deplacement)
            
            val, current_move = minmaxAlphaBeta(board, depth-1, alpha, beta)

            #undo the move
            board.pop()
            
            if(val > value or not bestMove):
                value = val
                bestMove = move

            alpha = max(alpha, value)

            if(beta < alpha and bestMove):
                return value, bestMove

    else:
        value = 1e8
        for move in moves:

            #do the move
            deplacement = chess.Move.from_uci(str(move))
            #do the move
            board.push(deplacement)
            
            val,current_move = minmaxAlphaBeta(board, depth-1, alpha, beta)

            #undo the move
            board.pop()
            if(val < value or not bestMove):
                value = val
                bestMove = move

            beta = min(beta, value)
            if(beta < alpha and bestMove):
                return value, bestMove

    return value, bestMove
"""

def minmaxAlphaBeta(board, depth, alpha, beta):
    moves = list(board.legal_moves)

    bestMove = None

    if depth == 0 or len(moves) == 0:
        return evaluation.getValueBoard(board),bestMove

    if(not board.turn):
        value = 0
        for move in moves:
            deplacement = chess.Move.from_uci(str(move))
            #do the move
            board.push(deplacement)
            print("11a " + str(alpha),"b " + str(beta))
            
            val, current_move = minmaxAlphaBeta(board, depth-1, alpha, beta)
            print("v" + str(val))
            print("21a " + str(alpha),"b " + str(beta))
            #undo the move
            board.pop()

            if(val < value or not bestMove):
                value = val
                bestMove = move

            if(value >= beta):
                return beta, bestMove

            if(value > alpha):
                alpha = value

        return alpha, bestMove
        
    else:
        value = 0
        for move in moves:

            #do the move
            deplacement = chess.Move.from_uci(str(move))
            #do the move
            board.push(deplacement)
            print("12a " + str(alpha),"b " + str(beta))

            val,current_move = minmaxAlphaBeta(board, depth-1, alpha, beta)
            print("v" + str(val))
            print("22a " + str(alpha),"b " + str(beta))
            #undo the move
            board.pop()

            if(val < value or not bestMove):
                value = val
                bestMove = move

            if(value <= alpha):
                return alpha, bestMove

            if(value < beta):
                beta = value
            
        return beta, bestMove

def renderSVG(board):
    svg=open("chessrender.svg", "w") 
    svg.write(chess.svg.board(board))