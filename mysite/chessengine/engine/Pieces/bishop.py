from .piece import Piece
from .empty import Empty

class Bishop(Piece):
    def __init__(self, team, type):
        super().__init__(team, type)

    def validMoves(self, board, position):
        moves = []
        row, col = position[0], position[1]
        pieceTeam = board[row][col].team.lower()

        # white: up-right diagonal, black: down-left diagonal
        i = 1
        while row-i >= 0 and col+i < 8 and board[row-i][col+i].team.lower() != pieceTeam:
            # print('piece team: {}, board piece team: {}'.format(board[row-i][col+i].team.lower(), pieceTeam))
            # print('valid Move up-r {}'.format((row-i,col+i)))
            moves.append((row-i,col+i))
            if not isinstance(board[row-i][col+i], Empty):
                break  
            i+=1

        # white: up-left diagonal, black: down-right diagonal
        i = 1
        while row-i >= 0 and col-i >= 0 and board[row-i][col-i].team.lower() != pieceTeam:
            # print('piece team: {}, board piece team: {}'.format(board[row-i][col-i].team.lower(), pieceTeam))
            # print('valid Move u-l: {}'.format((row-i,col-i)))
            moves.append((row-i,col-i))
            if not isinstance(board[row-i][col-i], Empty):
                break
            i+=1

        # white: down-right diagonal, black: up-left diagonal
        i = 1
        while row+i < 8 and col+i < 8 and board[row+i][col+i].team.lower() != pieceTeam:
            # print('board piece team: {}, piece team: {}'.format(board[row+i][col+i].team.lower(), pieceTeam))
            # print('valid Move d-r: {}'.format((row+i,col+i)))
            moves.append((row+i,col+i))
            if not isinstance(board[row+i][col+i], Empty):
                break
            i+=1

        # white: down-left diagonal, black: up-right diagonal
        i = 1
        while row+i < 8 and col-i >=0 and board[row+i][col-i].team.lower() != pieceTeam:
            # print('piece team: {}, board piece team: {}'.format(board[row+i][col-i].team.lower(), pieceTeam))
            # print('valid Move d-l: {}'.format((row+i,col-i)))
            moves.append((row+i, col-i))
            if not isinstance(board[row+i][col-i], Empty):
                break
            i+=1

        print('Moves available for BISHOP at [{},{}]: {}'.format(row,col,moves))
        return moves