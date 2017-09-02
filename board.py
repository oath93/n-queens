from random import randrange

class Board(object):
    def __init__(self, size):
        self.size = size
        self.board = []
        self.queen_positions = []
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

    def place_piece(self, x, y):
        self.board[x][y] = 'Q'
        self.queen_positions.append([x,y])

    def check_board(self):
        for queen in self.queen_positions:
            pass


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
            board.place_piece(x,y)
            print("placing piece #" + str(j + 1) +" (" + str(x + 1) + ", " + str(y + 1) + ")")
            board.print_board()

test_board(99, 100, 1)