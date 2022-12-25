from Pieces import Pawn, Bishop, Empty, King, Queen, Rook, Knight


class Chessboard:
    def __init__(self, colour_white, colour_black):
        board = [
                    [Rook(colour_black), Knight(colour_black), Bishop(colour_black), Queen(colour_black), King(colour_black), Bishop(colour_black),Knight(colour_black), Rook(colour_black)],
                    [Pawn(colour_black) for i in range(8)],
                    [Empty("Empty") for i in range(8)],
                    [Empty("Empty") for i in range(8)],
                    [Empty("Empty") for i in range(8)],
                    [Empty("Empty") for i in range(8)],
                    [Pawn(colour_white) for i in range(8)],
                    [Rook(colour_white), Knight(colour_white), Bishop(colour_white), King(colour_white), Queen(colour_white), Bishop(colour_white),Knight(colour_white), Rook(colour_white)]
                ]



        