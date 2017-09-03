from random import randrange

def spaces_to_align(num):
    spaces = 0
    while num >= 10 ** spaces:
        spaces += 1
    if spaces == 0:
        spaces += 1
    return spaces - 1
def right_pad_string(to_pad, spaces):
    to_return = to_pad
    for i in range(spaces + 1):
        to_return = to_return + " "
    return to_return

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
        spaces_in_size = spaces_to_align(self.size)
        for i in range(self.size):
            spaces_in_number = spaces_to_align(i + 1)
            to_add = right_pad_string(str(i + 1), spaces_in_size - spaces_in_number)
            output = output + to_add
        print(output)
        for i in range(self.size):
            spaces_in_number = spaces_to_align(i + 1)
            output = right_pad_string(str(i + 1), spaces_in_size - spaces_in_number)
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
for i in range(0,250,5):
    print(i, end=" ")
    print(spaces_to_align(i))