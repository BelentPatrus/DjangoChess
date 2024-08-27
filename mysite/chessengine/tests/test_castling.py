from django.test import TestCase
from ..engine.chessboard import Chessboard
from ..engine.TeamSideE import TeamSideE
from ..models import ChessMoveModel, ChessBoardModel, GameStateModel
from ..helper import Helper
from ..engine.Pieces.king import King
from ..engine.Pieces.rook import Rook
import json
# Create your tests here.

class CastlingTestCase(TestCase):

    def setUp(self):
        # these moves for removing pawns and setting queen in the middle of table with bishops protecting king from check
        self.moves = [
            ([6, 4], [4, 4]),  # White pawn
            ([1, 4], [3, 4]),  # Black pawn
            ([7, 3], [3, 7]),  # White queen
            ([0, 3], [4, 7]),  # Black queen
            ([3, 7], [1, 7]),  # White queen move again
            ([4, 7], [6, 7]),  # Black queen move again
            ([1, 7], [1, 6]),  # White queen move again
            ([6, 7], [6, 6]),  # Black queen move again
            ([1, 6], [0, 6]),  # White queen move again
            ([6, 6], [7, 6]),  # Black queen move again
            ([0, 6], [2, 6]),  # White queen move again
            ([7, 6], [5, 6]),  # Black queen move again
            ([2, 6], [2, 1]),  # White queen move again
            ([5, 6], [5, 1]),  # Black queen move again
            ([2, 1], [1, 0]),  # White queen move again
            ([5, 1], [6, 0]),  # Black queen move again
            ([1, 0], [1, 1]),  # White queen move again
            ([6, 0], [6, 1]),  # Black queen move again
            ([1, 1], [1, 2]),  # White queen move again
            ([6, 1], [6, 2]),  # Black queen move again
            ([1, 2], [0, 1]),  # White queen move again
            ([6, 2], [7, 1]),  # Black queen move again
            ([0, 1], [3, 4]),  # White queen move again
            ([0, 5], [1, 4]),  # Black bishop to protect king
            ([7, 5], [6, 4]),  # White bishop to protect king
            ([7, 1], [4, 4]),  # Black queen move again
            ([7, 2], [5, 0]),  # White bishop to left of board
            ([0, 2], [2, 0]),  # Black bishop to left of board
        ]
        # Create a game state
        self.gameStateId = GameStateModel.objects.create()

        # Initialize the chessboard
        self.chess = Chessboard(gameStateId=self.gameStateId)

        # Generate the move dictionary and convert it
        moveDict = self.chess.getAllValidMoves()
        moveDictConverted = Helper.convert_keys_to_strings(moveDict)

        # Create the JSON representation of the chessboard
        jsonChess = json.dumps(self.chess.getJSONDict())

        # Save the chessboard state to the database for movePiece
        self.chessboardData = ChessBoardModel(
            chessboard=jsonChess,
            moveDict=moveDictConverted,
            gameState=self.gameStateId,
            playerTurn=TeamSideE.WHITE,
        )
        self.chessboardData.save()

    def performMoves(self):
        for position, move in self.moves:
            self.chess.movePiece(position, move)

    def test_valid_castling_right(self):
        print("Start of Test Case 01: Valid Castling")
        self.performMoves()
        validMoves = self.chess.getAllValidMoves()
        blackKingMoves = validMoves[self.chess.board[0][4].getTeam().value][(0, 4)]
        whiteKingMoves = validMoves[self.chess.board[7][4].getTeam().value][(7, 4)]
        self.assertIn(
            [0, 6],
            blackKingMoves,
            f"BLACK KING TEST is: {self.chess.board[0][4].getTeam().value} {self.chess.board[0][4].getType().value}. AND doesn't have the RIGHT CASTLING move in its moveset: {blackKingMoves}",
        )
        self.assertIn(
            [0,2],
            blackKingMoves,
            f"BLACK KING test is: {self.chess.board[0][4].getTeam().value} {self.chess.board[0][4].getType().value}. AND doesn't have the LEFT CASTLING move in its moveset: {blackKingMoves}"
        )
        self.assertIn(
            [7, 2],
            whiteKingMoves,
            f"WHITE KING test is: {self.chess.board[7][4].getTeam().value} {self.chess.board[7][4].getType().value}. AND doesn't have the LEFT CASTLING move in its moveset: {whiteKingMoves}",
        )
        self.assertIn(
            [7, 6],
            whiteKingMoves,
            f"WHITE KING test is: {self.chess.board[7][4].getTeam().value} {self.chess.board[7][4].getType().value}. AND doesn't have the RIGHT CASTLING move in its moveset: {whiteKingMoves}",
        )
        print("Regular left and right castling available to white and black kings when no obstacles in the way")

        position = [7, 4]
        move = [7, 6]
        self.chess.movePiece(position, move) # white right side castle
        position = [0, 4]
        move = [0, 6]
        self.chess.movePiece(position, move) # black right side castle
        self.assertTrue(isinstance(self.chess.board[7][6], King), 
                        f"Position [7,6] doesn't hold a KING piece its: {self.chess.board[7][6]}")
        self.assertEquals(self.chess.board[7][6].getTeam(), TeamSideE.WHITE, 
                        f"Position [7,6] doesn't hold a WHITE piece its: {self.chess.board[7][6]}")
        self.assertTrue(isinstance(self.chess.board[7][5], Rook), 
                        f"Position [7,5] doesn't hold a ROOK piece its: {self.chess.board[7][5]}")
        self.assertEquals(self.chess.board[7][5].getTeam(), TeamSideE.WHITE, 
                        f"Position [7,5] doesn't hold a WHITE piece its: {self.chess.board[7][5]}")
        print("White right castle asserted True")
        self.assertTrue(isinstance(self.chess.board[0][6], King),
                        f"Position [0,6] doesn't hold a KING piece its: {self.chess.board[0][6]}")
        self.assertEquals(self.chess.board[0][6].getTeam(), TeamSideE.BLACK,
                        f"Position [0,6] doesn't hold a BLACK piece its: {self.chess.board[0][6]}")
        self.assertTrue(isinstance(self.chess.board[0][5], Rook), 
                        f"Position [0,5] doesn't hold a ROOK piece its: {self.chess.board[0][5]}")
        self.assertEquals(self.chess.board[0][5].getTeam(), TeamSideE.BLACK, 
                        f"Position [0,5] doesn't hold a BLACK piece its: {self.chess.board[0][5]}")
        print("Black right castle asserted True")

    def test_valid_castling_left(self):
        print("Start of Test Case 01: Valid Castling")

        self.performMoves()
        validMoves = self.chess.getAllValidMoves()
        blackKingMoves = validMoves[self.chess.board[0][4].getTeam().value][(0, 4)]
        whiteKingMoves = validMoves[self.chess.board[7][4].getTeam().value][(7, 4)]
        self.assertIn(
            [0, 6],
            blackKingMoves,
            f"BLACK KING TEST is: {self.chess.board[0][4].getTeam().value} {self.chess.board[0][4].getType().value}. AND doesn't have the RIGHT CASTLING move in its moveset: {blackKingMoves}",
        )
        self.assertIn(
            [0,2],
            blackKingMoves,
            f"BLACK KING test is: {self.chess.board[0][4].getTeam().value} {self.chess.board[0][4].getType().value}. AND doesn't have the LEFT CASTLING move in its moveset: {blackKingMoves}"
        )
        self.assertIn(
            [7, 2],
            whiteKingMoves,
            f"WHITE KING test is: {self.chess.board[7][4].getTeam().value} {self.chess.board[7][4].getType().value}. AND doesn't have the LEFT CASTLING move in its moveset: {whiteKingMoves}",
        )
        self.assertIn(
            [7, 6],
            whiteKingMoves,
            f"WHITE KING test is: {self.chess.board[7][4].getTeam().value} {self.chess.board[7][4].getType().value}. AND doesn't have the RIGHT CASTLING move in its moveset: {whiteKingMoves}",
        )
        print("Regular left and right castling available to white and black kings when no obstacles in the way")

        position = [7, 4]
        move = [7, 2]
        self.chess.movePiece(position, move) # white left side castle
        position = [0, 4]
        move = [0, 2]
        self.chess.movePiece(position, move) # black left side castle
        self.assertTrue(isinstance(self.chess.board[7][2], King), 
                        f"Position [7,2] doesn't hold a KING piece its: {self.chess.board[7][2]}")
        self.assertEquals(self.chess.board[7][2].getTeam(), TeamSideE.WHITE, 
                        f"Position [7,2] doesn't hold a WHITE piece its: {self.chess.board[7][2]}")
        self.assertTrue(isinstance(self.chess.board[7][3], Rook), 
                        f"Position [7,3] doesn't hold a ROOK piece its: {self.chess.board[7][3]}")
        self.assertEquals(self.chess.board[7][3].getTeam(), TeamSideE.WHITE, 
                        f"Position [7,3] doesn't hold a WHITE piece its: {self.chess.board[7][3]}")
        print("White LEFT castle asserted True")
        self.assertTrue(isinstance(self.chess.board[0][2], King), 
                        f"Position [0,2] doesn't hold a KING piece its: {self.chess.board[0][2]}")
        self.assertEquals(self.chess.board[0][2].getTeam(), TeamSideE.BLACK, 
                        f"Position [0,6] doesn't hold a BLACK piece its: {self.chess.board[0][2]}")
        self.assertTrue(isinstance(self.chess.board[0][3], Rook), 
                        f"Position [0,3] doesn't hold a ROOK piece its: {self.chess.board[0][3]}")
        self.assertEquals(self.chess.board[0][3].getTeam(), TeamSideE.BLACK, 
                        f"Position [0,3] doesn't hold a BLACK piece its: {self.chess.board[0][3]}")
        print("Black LEFT castle asserted True")
