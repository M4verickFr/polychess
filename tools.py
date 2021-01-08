import chess
import chess.polyglot
import random
import math

import polyglot as pg
import evaluation

import chess.svg 


def initBoard():
    """board initialisation

    Returns:
        board: default chess board
    """
    return chess.Board()

def displayBoard(board):
    print(board)

def menu():
    """select game type 

    Returns:
        string: gametype
    """
    playersType = [0,1]
    print("------------------------------")
    print("Select game type :")
    print("0- Play against Human")
    print("1- Play against Program")
    playerType = int(input("Enter selected mode : "))

    if(not playerType in playersType):
        print("------------------------------")
        print("Typing error")
        menu()

    return playerType

def getMove(board, playerType):
    """Get the move related with playerType

    Args:
        board (board): board object from chess
        playerType (string): selected player type

    Returns:
        string: piece movement on the board, i.e. "g2g4"
    """
    #Get the move related with the playerType
    move = None
    playerTypeMovesFunction = [
        getPlayerMove,
        getBestMove
    ]

    movesFunction = playerTypeMovesFunction[playerType]
    move = str(movesFunction(board))

    if playerType == 1:
        print("----------------------------------------")
        print("IA - Movement :" + move)

    return move

#get all the legal moves for the current position

def getPlayerMove(board):
    """Select player move

    Args:
        board (board): board object from chess

    Returns:
        string: selected player move
    """
    #Display player movement selection
    moves = board.legal_moves

    print("----------------------------------------")
    if(board.turn):
    	inputMove = input("Player 1 - Enter your mouvement : \n")
    else:
    	inputMove = input("Player 2 - Enter your mouvement : \n")

    for move in list(moves):
        if(inputMove == chess.Move.uci(move)):
            return inputMove
    
    print("Typing error : no possible movement corresponds to your entry")      
    return getPlayerMove(board)

def getBestMove(board):
    """find the best move

    Args:
        board (board): board object from chess

    Returns:
        UCI.move: piece movement on the board, i.e. "g2g4"
    """
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
        
        val, deplacement = minmax(board,3)
        #val, deplacement = minmaxAlphaBeta(board,5,-math.inf,math.inf)
    
    return deplacement

def makeMove(board, playerType):
    """make move and display board

    Args:
        board (board): board object from chess
        playerType (string): selected player type

    Returns:
        board: updated board
    """
    move = getMove(board, playerType)

    deplacement = chess.Move.from_uci(str(move))
    board.push(deplacement)

    displayBoard(board)

    return board


def minmax(board, depth):
    """get the best move and it weight

    Args:
        board (board): board object from chess
        depth (int): depth of the search

    Returns:
        int: move weight
        UCI.move: piece movement on the board, i.e. "g2g4"
    """
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

    return value, bestMove


# def minmaxAlphaBeta(board, depth, alpha, beta):
#     moves = list(board.legal_moves)

#     bestMove = None

#     if depth == 0 or len(moves) == 0:
#         return evaluation.getValueBoard(board),bestMove

#     if(board.turn):
#         value = -1e8
#         for move in moves:
#             deplacement = chess.Move.from_uci(str(move))
#             #do the move
#             board.push(deplacement)
            
#             val, current_move = minmaxAlphaBeta(board, depth-1, alpha, beta)

#             #undo the move
#             board.pop()
            
#             if(val > value or not bestMove):
#                 value = val
#                 bestMove = move

#             alpha = max(alpha, value)

#             if(beta < alpha and bestMove):
#                 return value, bestMove

#     else:
#         value = 1e8
#         for move in moves:

#             #do the move
#             deplacement = chess.Move.from_uci(str(move))
#             #do the move
#             board.push(deplacement)
            
#             val,current_move = minmaxAlphaBeta(board, depth-1, alpha, beta)

#             #undo the move
#             board.pop()
#             if(val < value or not bestMove):
#                 value = val
#                 bestMove = move

#             beta = min(beta, value)
#             if(beta < alpha and bestMove):
#                 return value, bestMove

#     return value, bestMove


def minmaxAlphaBeta(board, depth, alpha, beta):
    """minmax upgrade: it doesn't run through all the branches

    Args:
        board (board): board object from ches
        depth (int): depth of the search
        alpha (int): lightest movement
        beta (int): weightest movement

    Returns:
        int: move weight
        UCI.move: piece movement on the board, i.e. "g2g4"
    """
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
    """render board in a SVG file

    Args:
        board (board): board object from chess
    """
    svg=open("chessrender.svg", "w") 
    svg.write(chess.svg.board(board))