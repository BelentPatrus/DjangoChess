
from .piece import Piece
from .empty import Empty


class Rook(Piece):

    def __init__(self, team, type):
        super().__init__(team, type)

    def validMoves(self, board, position):
        moves = []
        row, col = position[0], position[1]
        pieceTeam = board[row][col].team.lower()
        i = 1
        # white: up, black: down
        while row-i >= 0 and board[row-i][col].team.lower() != pieceTeam:
            moves.append([row-i, col])
            if not isinstance(board[row-i][col], Empty):
                break
            i+=1

        # white: down, black: up
        i = 1
        while row+i < 8 and board[row+i][col].team.lower() != pieceTeam:
            moves.append([row+i,col])
            if not isinstance(board[row+i][col], Empty):
                break
            i+=1
        
        i = 1
        # white: right, black: left
        while col+i < 8 and board[row][col+i].team.lower() != pieceTeam:
            moves.append([row, col+i])
            if not isinstance(board[row][col+i], Empty):
                break
            i+=1
        
        i = 1
        # white: left, black: right
        while col-i >= 0 and board[row][col-i].team.lower() != pieceTeam:
            moves.append([row, col-i])
            if not isinstance(board[row][col-i], Empty):
                break
            i+=1

        return moves