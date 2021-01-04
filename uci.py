#!/usr/bin/env pypy -u
# -*- coding: utf-8 -*-

import time
import chess
import evaluation

def minmax(board, depth):
    value = 1e-8
    moves = list(board.legal_moves)
    bestMove = None
    bestMoves = []

    if depth == 0 or len(moves) == 0:
        return [None], evaluation.getValueBoard(board)

    for move in moves:
        #do the move
        deplacement = chess.Move.from_uci(str(move))
        #do the move
        board.push(deplacement)
        #get value of the move
        current_move, val = minmax(board, depth-1)
        #undo the move
        board.pop()

        # if the move is more good, replace bestMove
        if(val < value):
            value = val
            bestMove = move

        bestMoves.append(bestMove)

    return bestMoves, value

def main():
    board = chess.Board()
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

        elif command.startswith('position'):
            params = command.split(' ')
            move = params.pop()
            board.push(chess.Move.from_uci(move))

        elif command.startswith('go'):
            #  default options
            depth = 3

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

            moves, value = minmax(board,depth)

            print(moves)
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