from random import randrange

class Board(object):
    def __init__(self, size):
        self.size = size
        self.board = []
        self.pieces = []
        for i in range(size):
            self.board.append([])
            for j in range(size):
                self.board[i].append('x')

    #work on output for double-digit boards
    def print_board(self):
        output = "  "
        for i in range(self.size):
            output = output + str(i + 1) + " "
        print(output)
        for i in range(self.size):
            output = str(i + 1) + " "
            for j in range(self.size):
                output = output + self.board[j][i] + " "
            print(output)

    def place_piece(self, x, y, piece):
        if x < self.size and y < self.size:
            self.board[x][y] = piece
            self.pieces.append([x,y, piece])
        else:
            print("Invalid placement (out of bounds). x=" + str(x+1) + " y=" + str(y+1) + ". Boardsize: " + str(self.size))

def test_board(min, max, steps = 1):
    for i in range(min,max, steps):
        print("Test of n=" + str(i))
        board = Board(i)
        board.print_board()
        pieces_to_place = randrange(0,i)
        print("testing piece placing. placing " + str(pieces_to_place) + " test pieces.")
        for j in range(pieces_to_place):
            x = randrange(0,i)
            y = randrange(0,i)
            board.place_piece(x,y, "Q")
            print("placing piece #" + str(j + 1) +" (" + str(x + 1) + ", " + str(y + 1) + ")")
            board.print_board()
        print("Placing out-of-bounds piece:")
        print("Board before attempted place...")
        board.print_board()
        board.place_piece(i-1,i,"Q")
        print("Board after attempted place...")
        board.print_board()
        board.place_piece(i,i-1,"Q")
        print("Attempting placement at edge.")
        board.place_piece(i-1,i-1,"Q")
        board.print_board()


test_board(10,11, 1)