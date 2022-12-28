
from .piece import Piece


class Knight(Piece):
    def __init__(self, team, type):
        super().__init__(team, type)
    
    def validMoves(self, board, position):
        moves = []
        row, col = position[0], position[1]
        pieceTeam = board[row][col].team.lower()
        # White: up up left Black: down down right
        if row-2 >= 0 and col-1 >= 0 and board[row-2][col-1].team.lower() != pieceTeam:
            moves.append((row-2,col-1))
        # white: up up right, black: down down left
        if row-2 >= 0 and col+1 < 8 and board[row-2][col+1].team.lower() != pieceTeam:
            moves.append((row-2,col+1))
        # white: up left left, black: down right right
        if row-1 >=0 and col-2 >= 0 and board[row-1][col-2].team.lower() != pieceTeam:
            moves.append((row-1, col-2))
        # white: up right right, black down left left
        if row-1 >= 0 and col+2 < 8 and board[row-1][col+2].team.lower() != pieceTeam:
            moves.append((row-1, col+2))
        # white: down left left, black: up right right
        if row+1 < 8 and col-2 >= 0 and board[row+1][col-2].team.lower() != pieceTeam:
            moves.append((row+1, col-2))
        # white: down down left, black: up up right
        if row+2 < 8 and col-1 >= 0 and board[row+2][col-1].team.lower() != pieceTeam:
            moves.append((row+2, col-1)) 
        # white: down down right, black: up up left          
        if row+2 < 8 and col+1 < 8 and board[row+2][col+1].team.lower() != pieceTeam:
            moves.append((row+2, col+1))
        # white: down right right, black: up left left 
        if row+1 < 8 and col+2 < 8 and board[row+1][col+2].team.lower() != pieceTeam:
            moves.append((row+1, col+2))
        
        print('MOVESET GOTTEN AT POSITION [{},{}] : {}'.format(row,col,moves))
        return moves