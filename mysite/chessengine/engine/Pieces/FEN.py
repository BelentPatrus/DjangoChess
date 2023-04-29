from .Pieces import Pieces
from ..TeamSideE import TeamSideE


class FEN:
    _FENDATA = {
        TeamSideE.WHITE: {
            Pieces.PAWN: "P",
            Pieces.ROOK: "R",
            Pieces.KNIGHT: "N",
            Pieces.BISHOP: "B",
            Pieces.QUEEN: "Q",
            Pieces.KING: "K",
        },
        TeamSideE.BLACK: {
            Pieces.PAWN: "p",
            Pieces.ROOK: "r",
            Pieces.KNIGHT: "n",
            Pieces.BISHOP: "b",
            Pieces.QUEEN: "q",
            Pieces.KING: "k",
        },
        TeamSideE.EMPTY: {
            Pieces.EMPTY: "1",
        },
    }
    _FENKEY = {
        "P": {"type": Pieces.PAWN, "team": TeamSideE.WHITE},
        "R": {"type": Pieces.ROOK, "team": TeamSideE.WHITE},
        "N": {"type": Pieces.KNIGHT, "team": TeamSideE.WHITE},
        "B": {"type": Pieces.BISHOP, "team": TeamSideE.WHITE},
        "Q": {"type": Pieces.QUEEN, "team": TeamSideE.WHITE},
        "K": {"type": Pieces.KING, "team": TeamSideE.WHITE},
        "p": {"type": Pieces.PAWN, "team": TeamSideE.BLACK},
        "r": {"type": Pieces.ROOK, "team": TeamSideE.BLACK},
        "n": {"type": Pieces.KNIGHT, "team": TeamSideE.BLACK},
        "b": {"type": Pieces.BISHOP, "team": TeamSideE.BLACK},
        "q": {"type": Pieces.QUEEN, "team": TeamSideE.BLACK},
        "k": {"type": Pieces.KING, "team": TeamSideE.BLACK},
        "1": {"type": Pieces.EMPTY, "team": TeamSideE.EMPTY},
    }

    @staticmethod
    def encryptFEN(self,team,type):
        return FEN._FENDATA[team][type]
    

    @staticmethod
    def decryptFEN(self, p):
        try:
            return FEN._FENKEY[p]    
        except KeyError:
            return None

        
    
