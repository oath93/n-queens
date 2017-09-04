from random import randrange
from time import time

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

    def print_board(self):
        spaces_in_size = spaces_to_align(self.size)
        padding = ""
        new_lines = ""
        for i in range(spaces_in_size + 1):
            padding = padding + " "
        for i in range(int(spaces_in_size / 2)):
            new_lines = new_lines + "\n"
        output = padding + " "
        for i in range(self.size):
            spaces_in_number = spaces_to_align(i + 1)
            to_add = right_pad_string(str(i + 1), spaces_in_size - spaces_in_number)
            output = output + to_add
        print(output)
        for i in range(self.size):
            spaces_in_number = spaces_to_align(i + 1)
            output = right_pad_string(str(i + 1), spaces_in_size - spaces_in_number)
            for j in range(self.size):
                output = output + self.board[j][i] + padding
            print(output + new_lines)

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
        pieces_to_place = randrange(0,(i*i))
        print("testing piece placing. placing " + str(pieces_to_place) + " test pieces.")
        for j in range(pieces_to_place):
            x = randrange(0,i)
            y = randrange(0,i)
            board.place_piece(x,y, "Q")
            print("placing piece #" + str(j + 1) +" (" + str(x + 1) + ", " + str(y + 1) + ")")
        print("Placing out-of-bounds pieces:")
        board.place_piece(i-1,i,"Q")
        board.place_piece(i,i-1,"Q")
        print("Attempting placement at edge.")
        board.place_piece(i-1,i-1,"Q")
        print("Final Board:")
        board.print_board()

start = time()

test_board(15,16, 1)
"""
for i in range(0,250,5):
    print(i, end=" ")
    print(spaces_to_align(i))
"""


end = time()
print("Time to complete tests: " + str(end - start) + " seconds.")