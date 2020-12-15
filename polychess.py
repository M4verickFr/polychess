#python-chess import
#https://github.com/niklasf/python-chess
import chess
#import polyglot as pg
import chess.polyglot 

import minMax 

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
    gameType = 2
    return gameType

def startRound(board, playerType):
    #Appeler le type de partie en fonction du type de partie
    move = None

    if(playerType == 1):
        move = getPlayerMove(board)
    elif(playerType == 2):
        move = getIAMove(board)

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


def getIAMove(board): #obtient le meilleur mouvement
    maxWeight = 0
    deplacement = None 
    with chess.polyglot.open_reader("bookfish.bin") as reader:
        for entry in reader.find_all(board):
            if maxWeight < entry.weight :

                deplacement = entry.move
                maxWeight = entry.weight   
    if not deplacement:
        deplacement = minMax.minMaxAlphaBeta(board,4,-3000,3000) #????????????????#

    print(deplacement)
    return(str(deplacement))



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
