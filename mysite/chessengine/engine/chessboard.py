import json

from .Pieces.FEN import FEN
from .Pieces.rook import Rook
from .Pieces.bishop import Bishop
from .Pieces.queen import Queen
from .Pieces.king import King
from .Pieces.knight import Knight
from .Pieces.pawn import Pawn
from .Pieces.empty import Empty
from .Pieces.Pieces import Pieces
from .TeamSideE import TeamSideE
from ..models import ChessBoardModel
from ..models import ChessMoveModel
from .Pieces.piece import Piece

from django.db.models import Q

from copy import deepcopy


class Chessboard:

    def __convert2D__(self, board):
        result = []
        row = 8
        index = 0
        while index < len(board):
            result.append(board[index:index+row])
            index = index + row
        return result

    def __init__(self, chessBoardModel=None, playerTurn=TeamSideE.WHITE):
        if chessBoardModel == None:

            self.board = [

                [Rook(TeamSideE.BLACK, Pieces.ROOK), Knight(TeamSideE.BLACK,  Pieces.KNIGHT), Bishop(TeamSideE.BLACK, Pieces.BISHOP), Queen(TeamSideE.BLACK, Pieces.QUEEN), King(
                    TeamSideE.BLACK, Pieces.KING), Bishop(TeamSideE.BLACK, Pieces.BISHOP), Knight(TeamSideE.BLACK, Pieces.KNIGHT), Rook(TeamSideE.BLACK, Pieces.ROOK)],
                [Pawn(TeamSideE.BLACK, Pieces.PAWN) for i in range(8)],
                [Empty(TeamSideE.EMPTY, Pieces.EMPTY) for i in range(8)],
                [Empty(TeamSideE.EMPTY, Pieces.EMPTY) for i in range(8)],
                [Empty(TeamSideE.EMPTY, Pieces.EMPTY) for i in range(8)],
                [Empty(TeamSideE.EMPTY, Pieces.EMPTY) for i in range(8)],
                [Pawn(TeamSideE.WHITE, Pieces.PAWN) for i in range(8)],
                [Rook(TeamSideE.WHITE, Pieces.ROOK), Knight(TeamSideE.WHITE, Pieces.KNIGHT), Bishop(TeamSideE.WHITE, Pieces.BISHOP), Queen(TeamSideE.WHITE, Pieces.QUEEN), King(
                    TeamSideE.WHITE, Pieces.KING), Bishop(TeamSideE.WHITE, Pieces.BISHOP), Knight(TeamSideE.WHITE, Pieces.KNIGHT), Rook(TeamSideE.WHITE, Pieces.ROOK)]
            ]
            self.moveData = {}
            self.playerTurn = playerTurn
            self.gameStateId = None
        else:
            self.board = []
            for p in chessBoardModel:
                p = FEN.decryptFEN(self, p)
                if p == None:
                    continue
                elif p['type'] == Pieces.BISHOP:
                    tmp = Bishop(p['team'], Pieces.BISHOP)
                elif p['type'] == Pieces.PAWN:
                    tmp = Pawn(p['team'], Pieces.PAWN)
                elif p['type'] == Pieces.QUEEN:
                    tmp = Queen(p['team'], Pieces.QUEEN)
                elif p['type'] == Pieces.KNIGHT:
                    tmp = Knight(p['team'], Pieces.KNIGHT)
                elif p['type'] == Pieces.KING:
                    tmp = King(p['team'], Pieces.KING)
                elif p['type'] == Pieces.EMPTY:
                    tmp = Empty(p['team'], Pieces.EMPTY)
                elif p['type'] == Pieces.ROOK:
                    tmp = Rook(p['team'], Pieces.ROOK)
                else:
                    return
                self.board.append(tmp)
            self.board = self.__convert2D__(self.board)
            self.moveData = []  # come back and fix this must query db
            self.captureLog = []  # come back and fix this must query db
            self.playerTurn = playerTurn

    def movePiece(self, position, move):
        """
            args: move dict with the current and next move location in two lists accessible with key's 'curr' and 'next'
            returns: True or False based on if the move is in the moveset calculated to be in the piece's move list.

        """
        # To test comment and make moveInfo = move
        # moveInfo = json.loads(move)
        # moveInfo = move
        # row, col = moveInfo['curr'][0], moveInfo['curr'][1]
        row, col = position[0], position[1]
        selectedP = self.board[row][col]
        print(self.board[row][col])
        if selectedP.team != self.playerTurn:
            print("NOT YOUR TURN")
            return False

        moveSet = self.board[row][col].validMoves(self.board, position)
        print(self.board[row][col].getTeam().value)
        print(self.board[row][col].getType().value)
        posTuple = tuple(position)

        # isValid = False if moveSet is None else tuple(next) in moveSet
        validMoves = self.getAllValidMoves()
        isValid = tuple(move) in validMoves[selectedP.getTeam().value][posTuple]
        if isValid:

            nextRow, nextCol = move[0], move[1]
            pieceTaken = self.board[nextRow][nextCol]

            moveData = {}
            moveData['piece'] = {'team': selectedP.getTeam().value, 'type': selectedP.getType().value}
            moveData['position'] = position
            moveData['pieceTaken'] = {'team': pieceTaken.getTeam().value, 'type': pieceTaken.getType().value}
            moveData['move'] = move

            # left or right castle moves from King
            if isinstance(selectedP, King) and row == nextRow and (col+2 == nextCol or col-2 == nextCol):
                moveData['result'] = 'CASTLE'
                moveData['rookPosition'] = [row,0] if col - 2 == nextCol else [row,7]
                moveData['rookMove'] = [row,3] if col - 2 == nextCol else [row,5]

                moveData['rookPiece'] = {
                                        'team': self.board[moveData['rookPosition'][0]][moveData['rookPosition'][1]].getTeam().value, 
                                        'type': self.board[moveData['rookPosition'][0]][moveData['rookPosition'][1]].getType().value
                                        }
                moveData['rookPieceTaken'] = {
                                            'team': self.board[moveData['rookMove'][0]][moveData['rookMove'][1]].getTeam().value, 
                                            'type': self.board[moveData['rookMove'][0]][moveData['rookMove'][1]].getType().value
                                            }
                self.castle(position, move, moveData['rookPosition'], moveData['rookMove'])
            elif pieceTaken.getTeam() == TeamSideE.EMPTY:
                moveData['result'] = 'MOVE'
                self.moveOrTake(position, move)
            else:
                moveData['result'] = 'TAKE'
                self.moveOrTake(position,move)

            self.setMoveData(moveData)

            self.toggleTurn()

        print("PLAYER TURN IS NOW " + self.playerTurn)
        return isValid

    def moveOrTake(self, position, move):
        self.board[move[0]][move[1]] = self.board[position[0]][position[1]]
        self.board[position[0]][position[1]] = Empty(TeamSideE.EMPTY, Pieces.EMPTY)

    def castle(self, position1, move1, position2, move2):
        self.board[move1[0]][move1[1]] = self.board[position1[0]][position1[1]]
        self.board[position1[0]][position1[1]] = Empty(TeamSideE.EMPTY, Pieces.EMPTY)

        self.board[move2[0]][move2[1]] = self.board[position2[0]][position2[1]]
        self.board[position2[0]][position2[1]] = Empty(TeamSideE.EMPTY, Pieces.EMPTY)

    def getAllMovesForPosition(self, team, position):
        return self.getAllValidMoves()[team][tuple(position)]

    def getAllValidMoves(self):
        valid_moves = {}
        valid_moves[TeamSideE.WHITE.value] = {}
        valid_moves[TeamSideE.BLACK.value] = {}
        for row, rowArray in enumerate(self.board):
            for col, piece in enumerate(rowArray):
                if piece.team != TeamSideE.EMPTY:
                    print(f'Valid Moves: Piece - {piece} position ({row}, {col})')
                    position = (row,col)
                    valid_moves[piece.team.value][position] = self.getMovesFilter(piece, position)
                    print(f'Valid Moves generated for {piece} - {valid_moves[piece.team][position]}')
        print(f'End of Valid Moves result: \n{valid_moves}')

        return valid_moves

    def getMovesFilter(self, piece, position):
        moves = self.generateAllMovesOfASinglePiece(piece, position)
        if len(moves) != 0:
            moves = self.handleSpecialMoves(piece, moves, position)
            moves = self.filterInvalidMoves(piece, moves, position)
        return moves

    def generateAllMovesOfASinglePiece(self, piece, position):
        return piece.validMoves(self.board, position)

    def filterInvalidMoves(self, piece, moves, position):
        validMoves = []
        for move in moves:
            newBoard = self.simulateMove(move, position)
            if not self.isKingInCheck(newBoard, piece.getTeam()):
                validMoves.append(move)

        return validMoves

    def handleSpecialMoves(self, piece, moves, position):
        if isinstance(piece, King):
            moves = self.handleCastling(piece, moves, position)
        if isinstance(piece, Pawn):
            moves = self.handleEnPassant(piece, moves, position)
        return moves

    def handleCastling(self, piece, moves, position):
        hasKingMoved = self.getKingsFirstMoveQuery(piece.getTeam())
        hasLeftRookMoved, hasRightRookMoved = self.getRooksFirstMoveQuery(piece.getTeam())
        leftCastle = False
        rightCastle = False
        # Need to test out the moveset filter.
        if not hasKingMoved and not self.isKingInCheck(self.board, piece.getTeam()):

            isUnderAttackLeft, isUnderAttackRight = self.isUnderAttackRightAndLeft(piece.getTeam())
        
            if not hasLeftRookMoved and not isUnderAttackLeft:

                leftCol = 1
                leftCastle = True
                while leftCol < 4 and leftCastle:
                    if (self.board[position[0]][leftCol].getTeam() != TeamSideE.EMPTY):
                        leftCastle = False
                    leftCol += 1
            if not hasRightRookMoved and not isUnderAttackRight:
                rightCol = 5
                rightCastle = True
                while rightCol < 7 and rightCastle:
                    if (self.board[position[0]][rightCol].getTeam() != TeamSideE.EMPTY):
                        rightCastle = False
                    rightCol += 1

        if leftCastle:
            if piece.getTeam() == TeamSideE.WHITE:
                if isinstance(piece, King):
                    moves.append((7,2))
            elif piece.getTeam() == TeamSideE.BLACK:
                if isinstance(piece, King):
                    moves.append((0,2))
        if rightCastle:
            if piece.getTeam() == TeamSideE.WHITE:
                if isinstance(piece, King):
                    moves.append((7,6))
            if piece.getTeam() == TeamSideE.BLACK:
                if isinstance(piece, King):
                    moves.append((0,6))

        return moves

    def isUnderAttackRightAndLeft(self,player):
        isUnderAttackRight = False
        isUnderAttackLeft = False

        positionsRight = [(0,6),(0,5)]
        positionsLeft = [(0,3),(0,2)]
        if player == TeamSideE.WHITE:
            positionsRight = [(7, 6), (7, 5)] 
            positionsLeft = [(7, 3), (7, 2)]

        for row, rowArray in enumerate(self.board):
            for col, piece in enumerate(rowArray):
                if self.board[row][col].getTeam() != player:
                    enemyPosition = [row, col]
                    for position in positionsRight:
                        if position in self.board[row][col].validMoves(self.board, enemyPosition):
                            isUnderAttackRight = True
                            break
                    for position in positionsLeft:
                        if position in self.board[row][col].validMoves(self.board, enemyPosition):
                            isUnderAttackLeft = True
                            break

        return isUnderAttackLeft, isUnderAttackRight

    def getKingsFirstMoveQuery(self, team):

        position = [0,4]
        if team == TeamSideE.WHITE:
            position = [7,4]
        try:
            kingMoves = ChessMoveModel.objects.filter(
                gameState=self.gameStateId,
                piece__type=Pieces.KING.value,
                piece__team=team,
                position=position
            ).order_by("date")
        except ChessMoveModel.DoesNotExist:
            kingMoves = None

        return kingMoves

    def getRooksFirstMoveQuery(self, team):
        position1 = [7,0]
        position2 = [7,7]
        if team == TeamSideE.WHITE:
            position1 = [0,0]
            position2 = [0,7]
        try:
            firstMovePos1 = ChessMoveModel.objects.filter(
                Q(gameState=self.gameStateId) &
                Q(piece__type=Pieces.ROOK.value) &
                Q(piece__team=team) &
                Q(position=position1)
            ).earliest("date")
        except ChessMoveModel.DoesNotExist:
            firstMovePos1 = None

        try:
            firstMovePos2 = ChessMoveModel.objects.filter(
                Q(gameState=self.gameStateId) &
                Q(piece__type=Pieces.ROOK.value) &
                Q(piece__team=team) &
                Q(position=position2)
            ).earliest("date")
        except ChessMoveModel.DoesNotExist:
            firstMovePos2 = None

        return firstMovePos1, firstMovePos2

    def handleEnPassant(self, piece, moves, position):
        # TODO
        return moves

    def simulateMove(self, move, position):

        newBoard = deepcopy(self.board)
        newBoard[move[0]][move[1]] = newBoard[position[0]][position[1]]
        newBoard[position[0]][position[1]] = Empty(TeamSideE.EMPTY, Pieces.EMPTY)
        return newBoard

    def isKingInCheck(self, board, player):
        moves = []
        for row, rowArray in enumerate(board):
            for col, piece in enumerate(rowArray):
                if board[row][col].getTeam() != player:
                    position = [row,col]
                    moves.extend(board[row][col].validMoves(board, position))
                if isinstance(piece, King) and piece.team == player:
                    kingPos = (row, col)

        return True if kingPos in moves else False

    def isCheckMate(self, movesDict, player):
        for moves in movesDict[player]:
            if len(moves) != 0:
                return False
        return True

    def getPieceMoves(self, position):
        return self.board[position[0]][position[1]].validMoves(self.board, position)

    def getJSONDict(self):
        # need to serialize the board
        chessboardSerialized = []

        for row in self.board:
            for p in row:
                chessboardSerialized.append(p.getJSONDict())
            chessboardSerialized.append("/")

        return ('').join(chessboardSerialized)

    def toggleTurn(self):
        self.playerTurn = TeamSideE.BLACK if self.playerTurn == TeamSideE.WHITE else TeamSideE.WHITE
        return

    def setMoveData(self, moveData):
        self.moveData = moveData

    def getMoveData(self):
        return self.moveData

    def setGameStateId(self, gameStateId):
        self.gameStateId = gameStateId

    def getGameStateId(self):
        return self.gameStateId
