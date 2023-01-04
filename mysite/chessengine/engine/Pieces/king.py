from .piece import Piece
from .empty import Empty

class King(Piece):
    def __init__(self, team, type):
        super().__init__(team, type)

    def validMoves(self, board, position):
        moves = []
        row, col = position[0], position[1]
        pieceTeam = board[row][col].team.lower()
        
        # white: up, black: down
        if row-1 >= 0 and board[row-1][col].team.lower() != pieceTeam:
            # print('piece team: {}, board piece team: {}'.format(board[row-1][col].team.lower(), pieceTeam))
            # print('valid Move u:{}'.format([row-1,col]))
            moves.append([row-1, col])

        # white: down, black: up
        if row+1 < 8 and board[row+1][col].team.lower() != pieceTeam:
            # print('piece team: {}, board piece team: {}'.format(board[row+1][col].team.lower(), pieceTeam))
            # print('valid Move d :{}'.format([row+1,col]))
            moves.append([row+1,col])
        
        # white: right, black: left
        if col+1 < 8 and board[row][col+1].team.lower() != pieceTeam:
            # print('piece team: {}, board piece team: {}'.format(board[row][col+1].team.lower(), pieceTeam))
            # print('valid Move r :{}'.format([row,col+1]))
            moves.append([row, col+1])

        
        # white: left, black: right
        if col-1 >= 0 and board[row][col-1].team.lower() != pieceTeam:
            # print('piece team: {}, board piece team: {}'.format(board[row][col-1].team.lower(), pieceTeam))
            # print('valid Move r :{}'.format([row,col-1]))
            moves.append([row, col-1])


        # white: up-right diagonal, black: down-left diagonal
        if row-1 >= 0 and col+1 < 8 and board[row-1][col+1].team.lower() != pieceTeam:
            # print('piece team: {}, board piece team: {}'.format(board[row-1][col+1].team.lower(), pieceTeam))
            # print('valid Move up-r {}'.format([row-1,col+1]))
            moves.append([row-1,col+1])   

        # white: up-left diagonal, black: down-right diagonal
        if row-1 >= 0 and col-1 >= 0 and board[row-1][col-1].team.lower() != pieceTeam:
            # print('piece team: {}, board piece team: {}'.format(board[row-1][col-1].team.lower(), pieceTeam))
            # print('valid Move u-l: {}'.format([row-1,col-1]))
            moves.append([row-1,col-1])

        
        # white: down-right diagonal, black: up-left diagonal
        if row+1 < 8 and col+1 < 8 and board[row+1][col+1].team.lower() != pieceTeam:
            # print('board piece team: {}, piece team: {}'.format(board[row+1][col+1].team.lower(), pieceTeam))
            # print('valid Move d-r: {}'.format([row+1,col+1]))
            moves.append([row+1,col+1])

        # white: down-left diagonal, black: up-right diagonal
        if row+1 < 8 and col-1 >=0 and board[row+1][col-1].team.lower() != pieceTeam:
            # print('piece team: {}, board piece team: {}'.format(board[row+1][col-1].team.lower(), pieceTeam))
            # print('valid Move d-l: {}'.format([row+1,col-1]))
            moves.append([row+1, col-1])
        
        print('Moves available for KING at [{},{}]: {}'.format(row,col,moves))
        return moves