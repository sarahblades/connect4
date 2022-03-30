import random, time

# Checking  a valid column number is entered
def is_column_number_valid():
    global piece
    while True:
        if piece == " X ":
            column = 0
            while column not in range(1, 8):
                try:
                    column = int(input("Enter column number between 1 and 7: "))
                except ValueError:
                    print("Invalid column number")

        elif piece == " O ":
            column = random.randrange(1, 8)

        # check if column full
        if check_column_full(column) == "Empty":
            break
        else:
            if piece == " X ":
                print("Column", column, "is full, please choose another")
    return column

def check_column_full(column):
    global connect_four
    # 3 is the top row, therefore checking if full
    if connect_four[3][(column*2-1)] == " X " or connect_four[3][(column*2-1)] == " O ":
        return "Full"
    else:
        return "Empty"

def place_piece(column, piece):
    global connect_four
    global won, draw
    global place_in_column1, place_in_column2, place_in_column3, place_in_column4, \
            place_in_column5, place_in_column6, place_in_column7

    if column == 1: row = place_in_column1; place_in_column1 -= 4

    elif column == 2: row = place_in_column2; place_in_column2 -= 4

    elif column == 3: row = place_in_column3; place_in_column3 -= 4

    elif column == 4: row = place_in_column4; place_in_column4 -= 4

    elif column == 5: row = place_in_column5; place_in_column5 -= 4

    elif column == 6: row = place_in_column6; place_in_column6 -= 4

    elif column == 7: row = place_in_column7; place_in_column7 -= 4

    # putting piece down
    connect_four[row][(column * 2 - 1)] = piece

    columns = [place_in_column1, place_in_column2, place_in_column3, place_in_column4, place_in_column5,
               place_in_column6, place_in_column7]

    # checking if winning move
    if check_winner(column, piece, row):
        won = True

    # checking if all columns are full, so no available moves left
    elif all(position == -1 for position in columns):
        draw = True

def check_winner(column, piece, row):
    global connect_four

    # CHECK 1: checking 3 pieces to right of current piece
    try:
        if connect_four[row][((column + 1) * 2 - 1)] == piece and\
                connect_four[row][((column + 2) * 2 - 1)] == piece and\
                connect_four[row][((column + 3) * 2 - 1)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 2: checking 3 pieces to left of current piece
    try:
        if connect_four[row][((column - 1) * 2 - 1)] == piece and\
                connect_four[row][((column - 2) * 2 - 1)] == piece and\
                connect_four[row][((column - 3) * 2 - 1)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 3: checking 2 pieces to left of current piece and 1 to right
    try:
        if connect_four[row][((column - 1) * 2 - 1)] == piece and\
                connect_four[row][((column - 2) * 2 - 1)] == piece and\
                connect_four[row][((column + 1) * 2 - 1)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 4: checking 2 pieces to right of current piece and 1 to left
    try:
        if connect_four[row][((column + 1) * 2 - 1)] == piece and \
                connect_four[row][((column + 2) * 2 - 1)] == piece and \
                connect_four[row][((column - 1) * 2 - 1)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 5: checking 3 pieces below current piece
    try:
        if connect_four[row+4][((column) * 2 - 1)] == piece and \
                connect_four[row+8][((column) * 2 - 1)] == piece and \
                connect_four[row+12][((column) * 2 - 1)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 6: checking 3 pieces diagonally above and to right of current piece
    try:
        if connect_four[row-4][((column + 1) * 2 - 1)] == piece and \
                connect_four[row-8][((column + 2) * 2 - 1)] == piece and \
                connect_four[row-12][((column + 3) * 2 - 1)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 7: checking 3 pieces diagonally above and to left of current piece
    try:
        if connect_four[row - 4][((column - 1) * 2 - 1)] == piece and \
                connect_four[row - 8][((column - 2) * 2 - 1)] == piece and \
                connect_four[row - 12][((column - 3) * 2 - 1)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 8: checking 3 pieces diagonally below and to right of current piece
    try:
        if connect_four[row+4][((column + 1) * 2 - 1)] == piece and \
                connect_four[row+8][((column + 2) * 2 - 1)] == piece and \
                connect_four[row+12][((column + 3) * 2 - 1)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 9: checking 3 pieces diagonally below and to left of current piece
    try:
        if connect_four[row+4][((column - 1) * 2 - 1)] == piece and \
                connect_four[row+8][((column - 2) * 2 - 1)] == piece and \
                connect_four[row+12][((column - 3) * 2 - 1)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 10: checking 1 piece diagonally below and to left of current piece
    # and 2 pieces diagonally above and to right
    try:
        if connect_four[row+4][((column - 1) * 2 - 1)] == piece and \
                connect_four[row-4][((column + 1) * 2 - 1)] == piece and \
                connect_four[row-8][((column + 2) * 2 - 1)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 11: checking 2 pieces diagonally below and to left of current piece
    # and 1 piece diagonally above and to right
    try:
        if connect_four[row+4][((column - 1) * 2 - 1)] == piece and \
                connect_four[row+8][((column - 2) * 2 - 1)] == piece and \
                connect_four[row-4][((column + 1) * 2 - 1)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 12: checking 1 piece diagonally above and to left of current piece
    # and 2 pieces diagonally below and to right
    try:
        if connect_four[row-4][((column - 1) * 2 - 1)] == piece and \
                connect_four[row+4][((column + 1) * 2 - 1)] == piece and \
                connect_four[row+8][((column + 2) * 2 - 1)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 13: checking 2 pieces diagonally above and to left of current piece
    # and 1 piece diagonally below and to right
    try:
        if connect_four[row-4][((column - 1) * 2 - 1)] == piece and \
                connect_four[row-8][((column - 2) * 2 - 1)] == piece and \
                connect_four[row+4][((column + 1) * 2 - 1)] == piece:
            return True
    except IndexError:
        pass

connect_four = [["  ", "1", "   ", "2", "   ", "3", "   ", "4", "   ", "5", "   ", "6", "   ", "7", "   "],
                ["+---+---+---+---+---+---+---+"],
                ["|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|"],
                ["|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|"],
                ["|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|"],
                ["+---+---+---+---+---+---+---+"],
                ["|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|"],
                ["|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|"],
                ["|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|"],
                ["+---+---+---+---+---+---+---+"],
                ["|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|"],
                ["|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|"],
                ["|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|"],
                ["+---+---+---+---+---+---+---+"],
                ["|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|"],
                ["|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|"],
                ["|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|"],
                ["+---+---+---+---+---+---+---+"],
                ["|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|"],
                ["|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|"],
                ["|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|"],
                ["+---+---+---+---+---+---+---+"],
                ["|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|"],
                ["|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|"],
                ["|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|"],
                ["+---+---+---+---+---+---+---+"]]

# 23 represents the bottom row, therefore empty at start
place_in_column1 = 23
place_in_column2 = 23
place_in_column3 = 23
place_in_column4 = 23
place_in_column5 = 23
place_in_column6 = 23
place_in_column7 = 23

won = False
draw = False

playing = True

num_of_moves = 0

while playing:

    # determining which turn it is
    if num_of_moves % 2 == 0:
        piece = " X "
    else:
        piece = " O "

    print("\n" + piece.strip() + "'s TURN")

    for line in connect_four:
        for item in line:
            print(item, end="")
        print()

    # enter a valid column number
    column_number = is_column_number_valid()

    # place piece
    num_of_moves += 1
    if piece == " O ":
        time.sleep(1)
    place_piece(column_number, piece)

    if won == True:
        result = "WINNER: " + piece.strip() + " in " + str(num_of_moves) + " moves!"
        playing = False

    elif draw == True:
        result = "DRAW - no available moves left!"
        playing = False

print("\n")
for line in connect_four:
    for item in line:
        print(item, end="")
    print()

print(result)
