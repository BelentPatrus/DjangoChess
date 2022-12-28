from django.test import TestCase
from chessengine.engine.chessboard import Chessboard as cb
# Create your tests here.

class testChessMoves(TestCase):
    def testPawnMove(self):
        print('STARTING PAWN TESTING FUNCTION *******************************')

        wpm = {
            'curr':[6,3],
            'next': [4,3]
        }
        c = cb('White','Black')
        wpawn = c.board[6][3]
        c.movePiece(wpm)
        self.assertTrue(c.board[4][3] == wpawn)
        print('Done white pawn test 1')
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
        print('STARTING QUEEN TESTING FUNCTION *******************************')
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
        print('STARTING ROOK TESTING FUNCTION *******************************')
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
        print('STARTING BISHOP TESTING FUNCTION *******************************')
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

    def testking(self):
        print('STARTING KING TESTING FUNCTION *******************************')
        c = cb('White','Black')
        k = c.board[7][4]
        pm = {
            'curr':[6,4],
            'next':[4,4]
        } 
        c.movePiece(pm)
        # up 1
        km = {
            'curr':[7,4],
            'next':[6,4]
        }
        # up left 1
        km2 = {
            'curr':[6,4],
            'next': [5,3]
        }
        # up 1
        km3 = {
            'curr':[5,3],
            'next':[4,3]
        }
        # up right
        km4={
            'curr':[4,3],
            'next':[3,4]
        }
        c.movePiece(km)
        c.movePiece(km2)
        c.movePiece(km3)
        c.movePiece(km4)
        self.assertTrue(c.board[3][4] == k)

    def testknight(self):
        print('STARTING KNIGHT TESTING FUNCTION *******************************')
        c = cb('White','Black')
        k = c.board[7][6]
        bk = c.board[0][1]
        km = {
            'curr':[7,6],
            'next':[5,5]
        }
        km1 = {
            'curr':[5,5],
            'next': [4,3]
        }
        bkm = {
            'curr':[0,1],
            'next':[2,2]
        }
        bkm1 = {
            'curr':[2,2],
            'next':[4,3]
        }
        c.movePiece(km)
        self.assertTrue(c.board[5][5] == k)
        c.movePiece(km1)
        self.assertTrue(c.board[4][3] == k)
        c.movePiece(bkm)
        self.assertTrue(c.board[2][2] == bk)
        c.movePiece(bkm1)
        self.assertTrue(c.board[4][3] == bk)
        print(c.board[4])
    

    def testChessGame(self):
        print('***************************STARTING CHESSBOARB SIMULATION ******************************')
        c = cb('White','Black')
        # White pieces
        wp0,wp1,wp2,wp3,wp4,wp5,wp6,wp7,wr0,wn0,wb0,wq,wk,wb1,wn1,wr1 = c.board[6][0], c.board[6][1], c.board[6][2], c.board[6][3], c.board[6][4], c.board[6][5], c.board[6][6], c.board[6][7], c.board[7][0], c.board[7][1], c.board[7][2], c.board[7][3], c.board[7][4], c.board[7][5], c.board[7][6], c.board[7][7]
        # Black pieces
        bp0,bp1,bp2,bp3,bp4,bp5,bp6,bp7,br0,bn0,bb0,bq,bk,bb1,bn1,br1 = c.board[1][0], c.board[1][1], c.board[1][2], c.board[1][3], c.board[1][4], c.board[1][5], c.board[1][6], c.board[1][7], c.board[0][0], c.board[0][1], c.board[0][2], c.board[0][3], c.board[0][4], c.board[0][5], c.board[0][6], c.board[0][7]

        #white moves
        #1
        wp4m = {
            'curr':[6,4],
            'next':[4,4]
        }
        #3
        wn1m = {
            'curr':[7,6],
            'next':[5,5]
        }
        #5
        wb1m = {
            'curr':[7,5],
            'next':[3,1]
        }
        #7
        wb1m1 = {
            'curr':[3,1],
            'next':[2,2]
        }
        #9
        wn1m1 = {
            'curr':[5,5],
            'next':[3,4]
        }
        #11
        wp5m = {
            'curr':[6,5],
            'next':[4,5]
        }
        #13
        wkm = {
            'curr':[7,4],
            'next':[6,5]
        }
        move15 = {
            'curr':[6,3],
            'next':[4,3]
        }
        move17={
            'curr':[7,7],
            'next':[7,4]
        }
        move19={
            'curr':[7,1],
            'next':[5,0]
        }


        #black moves
        #2
        bp4m = {
            'curr':[1,4],
            'next':[3,4]
        }
        #4
        bn0m = {
            'curr':[0,1],
            'next':[2,2]
        }
        #6
        bn1m = {
            'curr':[0,6],
            'next':[2,5]
        }
        #8
        bp3m = {
            'curr':[1,3],
            'next':[2,2]
        }
        #10
        bqm = {
            'curr':[0,3],
            'next':[4,3]
        }
        #12
        bqm1 ={
            'curr':[4,3],
            'next':[4,4]
        }
        #14
        bb1m = {
            'curr':[0,5],
            'next':[3,2]
        }
        move16={
            'curr':[3,2],
            'next':[5,0]
        }
        move18={
            'curr':[4,4],
            'next':[6,2]
        }
        move20={
            'curr':[6,2],
            'next':[7,3]
        }
        
        
        c.movePiece(wp4m)
        self.assertTrue(wp4 == c.board[4][4])
        c.movePiece(bp4m)
        self.assertTrue(bp4 == c.board[3][4])
        c.movePiece(wn1m)
        self.assertTrue(wn1 == c.board[5][5])
        c.movePiece(bn0m)
        self.assertTrue(bn0 == c.board[2][2])
        c.movePiece(wb1m)
        self.assertTrue(wb1 == c.board[3][1])
        c.movePiece(bn1m)
        self.assertTrue(bn1 == c.board[2][5])
        c.movePiece(wb1m1)
        self.assertTrue(wb1 == c.board[2][2])
        c.movePiece(bp3m)
        self.assertTrue(bp3 == c.board[2][2])
        c.movePiece(wn1m1)
        self.assertTrue(wn1 == c.board[3][4])
        c.movePiece(bqm)
        self.assertTrue(bq == c.board[4][3])
        c.movePiece(wp5m)
        self.assertTrue(wp5 == c.board[4][5])
        c.movePiece(bqm1)
        self.assertTrue(bq == c.board[4][4])
        c.movePiece(wkm)
        self.assertTrue(wk == c.board[6][5])
        c.movePiece(bb1m)
        self.assertTrue(bb1 == c.board[3][2])
        c.movePiece(move15)
        c.movePiece(move16)
        c.movePiece(move17)
        c.movePiece(move18)
        c.movePiece(move19)
        c.movePiece(move20)