from .piece import Piece
from .empty import Empty


class Pawn(Piece):

    def __init__(self, team, type):
        super().__init__(team, type)
        

    def validMoves(self, board, position):
        moves = []
        row, col = position[0], position[1]
        if self.team.lower() == 'white':
            # moving forward and moving twice on start
            if isinstance(board[row-1][col], Empty):
                moves.append((row-1,col))
                if row == 6 and isinstance(board[row-2][col], Empty):
                    moves.append((row-2, col))
            # Take logic
            if not isinstance(board[row-1][col+1], Empty):
                moves.append((row-1, col+1))
            if not isinstance(board[row-1][col-1], Empty):
                moves.append((row-1, col-1))
        elif self.team.lower() == 'black':
            if isinstance(board[row+1][col], Empty):
                moves.append((row+1, col))
                if row == 1 and isinstance(board[row+2][col], Empty):
                    moves.append((row+2, col))
            # Take logic
            if not isinstance(board[row+1][col-1], Empty):
                moves.append((row+1, col-1))
            if not isinstance(board[row+1][col+1], Empty):
                moves.append((row-1, col+1))
        print(moves)
        return moves
        
