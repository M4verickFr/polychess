#!/usr/bin/env pypy -u
# -*- coding: utf-8 -*-

import time
import chess

import evaluation
import tools

import chess.pgn 

def makeAMove(board):
    """get the IA move

    Args:
        board (board): board object from chess

    Returns:
        Array: list containts current bestMove and predicted next move
    """
    bestMove = tools.getBestMove(board)
    bestMoves = [bestMove, "a1a2"]
    print(bestMoves)
    return bestMoves

def main():
    """main function to play with the UCI protocol

    Infinite loop:
        - wait input from GUI
        - make action related to the input
        
    Find the UCI protocol documentation on GOOGLE, because GOOGLE IS YOUR BEST FRIEND
    """
    board = chess.Board()
    game = chess.pgn.Game()

    show_thinking = True
    our_time, opp_time = 1000, 1000 # time in centi-seconds

    while True:
        command = input()

        if command == 'quit':
            break

        elif command == 'debug':
            print(board)

        elif command == 'uci':
            print('id name PolyChess')
            print('id author MACDZ')
            print('uciok')

        elif command == 'isready':
            print('readyok')

        elif command == 'ucinewgame':
            board.reset()
            game = chess.pgn.Game()

        elif command == 'renderSVG':
            tools.renderSVG(board)

        elif command == 'exportPGN':
            print(game, file=open("game.pgn", "w"), end="\n\n")

        elif command == 'readPGN':
            game = chess.pgn.read_game(open("game.pgn"))
            board = game.board() 
            for move in game.mainline_moves():
                board.push(move)

        elif command == 'findBestMove':
            bestMove = tools.getBestMove(board)
            print('the bestmove is ' + str(bestMove))

        elif command.startswith('fen'):
            fen = command[3:]
            board.set_fen(fen)
            return fen

        elif command.startswith('position'):
            params = command.split(' ')
            move = params.pop()
            board.push(chess.Move.from_uci(move))
            node = game.add_variation(chess.Move.from_uci(move))
            
        elif command.startswith('go'):

            params = command.split(' ')[1:]
            for param, val in zip(params[::2], params[1::2]):
                if param == 'depth':
                    depth = int(val)
                if param == 'movetime':
                    movetime = int(val)
                if param == 'wtime':
                    our_time = int(val)
                if param == 'btime':
                    opp_time = int(val)

            start = time.time()
            ponder = None

            moves = makeAMove(board)

            board.push(moves[0])

            if len(moves) > 1:
                print(f'bestmove {moves[0]} ponder {moves[1]}')
            else:
                print('bestmove ' + moves[0])

        elif command.startswith('time'):
            our_time = int(command.split()[1])

        elif command.startswith('otim'):
            opp_time = int(command.split()[1])
            
        else:
            pass

if __name__ == '__main__':
    main()