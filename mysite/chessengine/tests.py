from django.test import TestCase
from chessengine.engine.chessboard import Chessboard as cb
# Create your tests here.

class testChessMoves(TestCase):
    def testPawnMove(self):
        wpm = {
            'curr':[6,3],
            'next': [4,3]
        }
        c = cb('White','Black')
        wpawn = c.board[6][3]
        c.movePiece(wpm)
        self.assertTrue(c.board[4][3] == wpawn)
        print('Done black pawn test 1')
        wpm1 = {
            'curr': [4,3],
            'next': [3,3]
        }

        c.movePiece(wpm1)
        self.assertTrue(c.board[3][3] == wpawn)
        print('Done white pawn test 2')
        bp = c.board[1][0]
        bpm = {
            'curr': [1,0],
            'next': [2,0]
        }
        c.movePiece(bpm)
        self.assertTrue(c.board[2][0] == bp)
        print('Done black pawn test 1')
        bpm1 = {
            'curr': [2,0],
            'next': [3,0]
        }
        c.movePiece(bpm1)
        self.assertTrue(c.board[3][0] == bp)
        print('Done black pawn test 2')

    def testQueenMoves(self):
        c = cb('White','Black')
        wpm = {
            'curr':[6,3],
            'next': [4,3]
        }
        c.movePiece(wpm)
        print('Finished moving pawn to 4,3')
        q = c.board[7][3]
        wqm = {
            'curr':[7,3],
            'next':[6,3]
        }
        c.movePiece(wqm)
        self.assertTrue(c.board[6][3] == q)
        print('Finished Queen moves test 1')
        wqm1 = {
            'curr':[6,3],
            'next': [3,0]
        }
        c.movePiece(wqm1)
        self.assertTrue(c.board[3][0] == q)
        print('Finished Queen moves test 2')

        # take move  test

        wqm2= {
            'curr':[3,0],
            'next':[1,0]
        }

        c.movePiece(wqm2)
        self.assertTrue(c.board[1][0] == q)
        print('Done queen take test 3')
        wqm3 = {
            'curr':[1,0],
            'next':[0,1]
        }
        c.movePiece(wqm3)
        print('Done queen take test 4')