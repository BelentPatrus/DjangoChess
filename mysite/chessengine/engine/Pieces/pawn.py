from .piece import Piece
from .empty import Empty
from ..TeamSideE import TeamSideE

class Pawn(Piece):

    def __init__(self, team, type):
        super().__init__(team, type)
        

    def validMoves(self, board, position):
        moves = []
        row, col = position[0], position[1]
        pieceTeam = board[row][col].team.lower()
        if self.team.lower() == TeamSideE.WHITE.lower():
            # moving forward and moving twice on start
            if row-1 >= 0 and board[row-1][col].team.lower() == TeamSideE.EMPTY.lower():
                moves.append((row-1,col))
                if row == 6 and board[row-2][col].team.lower() == TeamSideE.EMPTY.lower():
                    moves.append((row-2, col))
            # Take logic
            if row-1 >=0 and col+1 < 8 and board[row-1][col+1].team.lower() == TeamSideE.BLACK.lower():
                moves.append((row-1, col+1))
            if row-1 >= 0 and col-1 >= 0 and board[row-1][col-1].team.lower() == TeamSideE.BLACK.lower():
                moves.append((row-1, col-1))
        elif self.team.lower() == TeamSideE.BLACK.lower():
            if row+1 < 8 and board[row+1][col].team.lower() == TeamSideE.EMPTY.lower():
                moves.append((row+1, col))
                if row == 1 and board[row+2][col].team.lower() == TeamSideE.EMPTY.lower():
                    moves.append((row+2, col))
            # Take logic
            if row+1 < 8 and col-1 >=0 and board[row+1][col-1].team.lower() == TeamSideE.WHITE.lower():
                moves.append((row+1, col-1))
            if row+1 < 8 and col+1 < 8 and board[row+1][col+1].team.lower() == TeamSideE.WHITE.lower():
                moves.append((row+1, col+1))

        print('Moves available for {} PAWN at [{},{}]: {}'.format(pieceTeam,row,col,moves))
        return moves