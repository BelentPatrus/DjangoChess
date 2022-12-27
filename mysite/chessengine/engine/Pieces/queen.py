
from .piece import Piece
from .empty import Empty


class Queen(Piece):
    def __init__(self, team, type):
        super().__init__(team, type)

    def validMoves(self, board, position):
        moves = []
        row, col = position[0], position[1]
        pieceType = board[row][col].type
        i = 1
        # white: up, black: down
        print('In queen valid move')
        while row-i >= 0 and (isinstance(board[row-i][col], Empty) or isinstance(board[row-i][col].type, Piece)):
            print('valid Move u:{}'.format([row-i,col]))
            moves.append((row-i, col))
            i+=1
        # white: down, black: up
        i = 1
        while row+i < 8 and (isinstance(board[row+i][col], Empty) or isinstance(board[row+i][col], Piece)):
            print('valid Move d :{}'.format([row+i,col]))
            moves.append((row+i,col))
            i+=1
        
        # white: up-right diagonal, black: down-left diagonal
        i = 1
        while row-i >= 0 and col+i < 8 and (isinstance(board[row-i][col+i], Empty) or isinstance(board[row-i][col+i], Piece)):
            print('valid Move up-r {}'.format([row-i,col+i]))
            moves.append((row-i,col+i))
            i+=1
        
        # white: up-left diagonal, black: down-right diagonal
        i = 1
        while row-i >= 0 and col-i >= 0 and (isinstance(board[row-i][col-i], Empty) or isinstance(board[row-i][col-i], Piece)):
            print('valid Move u-l: {}'.format([row-i,col-i]))
            moves.append((row-i,col-i))
            i+=1
        
        # white: down-right diagonal, black: up-left diagonal
        i = 1
        while row+i < 8 and col+i < 8 and (isinstance(board[row+i][col+i], Empty) or isinstance(board[row+i][col+i], Piece)):
            print('valid Move d-r: {}'.format([row+i,col+i]))
            moves.append((row+i,col+i))
            i+=1
        
        # white: down-left diagonal, black: up-right diagonal
        i = 1
        while row+i < 8 and col-i >=0 and (isinstance(board[row+i][col-i], Empty) or isinstance(board[row+i][col-i], Piece)):
            print('valid Move d-l: {}'.format([row+i,col-i]))
            moves.append((row+i, col-i))
            i+=1
        
        return moves
        
