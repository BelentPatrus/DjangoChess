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
    
    def testrooktest(self):
        c = cb('White','Black')
        r = c.board[7][7]
        wpm = {
            'curr':[6,7],
            'next':[4,7]
        }
        c.movePiece(wpm)
        print('Done pawn move for rook test')
        wrm = {
            'curr':[7,7],
            'next':[5,7]
        }
        c.movePiece(wrm)
        self.assertTrue(c.board[5][7] == r)
        print('Done moving Rook test 1')
        wrm1 = {
            'curr':[5,7],
            'next':[5,1]
        } 
        c.movePiece(wrm1)
        self.assertTrue(c.board[5][1] == r)
        print('Done moving rook test 2')

        wrm2 = {
            'curr':[5,1],
            'next':[3,1]
        }
        c.movePiece(wrm2)
        self.assertTrue(c.board[3][1] == r)
        print('Done moving rook test 3')

    def testbishop(self):
        c = cb('White','Black')
        b = c.board[7][5]
        pm = {
            'curr':[6,4],
            'next':[4,4]
        }
        
        c.movePiece(pm)
        self.assertTrue(c.board[7][5] == b)
        bm = {
            'curr':[7,5],
            'next':[4,2]
        }
        c.movePiece(bm)
        self.assertTrue(c.board[4][2] == b)

        bm2 = {
            'curr':[4,2],
            'next':[1,5]
        }
        c.movePiece(bm2)
        self.assertTrue(c.board[1][5] == b)
        print('Done take bishop test')

