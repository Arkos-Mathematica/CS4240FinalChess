print("I'm chessing!")

p = {"Q":u'\u265B', "K":u'\u265A', "R":u'\u265C', "B":u'\u265D', "N":u'\u265E', "P":u'\u265F',
     "q":u'\u2655', "k":u'\u2654', "b":u'\u2657', "r":u'\u2656', "n":u'\u2658', "p":u'\u2659', 0:0}

board = [
["R","N","B","Q","K","B","N","R"],
["P","P","P","P","P","P","P","P"],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
["p","p","p","p","p","p","p","p"],
["r","n","b","q","k","b","n","r"]
]
check_board = [
["R","N","B","Q","K","B","N","R"],
["P","P","P","P","P","P","P","P"],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
["p","p","p","p","p","p","p","p"],
["r","n","b","q","k","b","n","r"]
]

final_board = [[p[x] for x in board[z]] for z in range(len(board))]

def clear_board():
    print('clearing')
    global board
    board = [
    ["R","N","B","Q","K","B","N","R"],
    ["P","P","P","P","P","P","P","P"],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    ["p","p","p","p","p","p","p","p"],
    ["r","n","b","q","k","b","n","r"]
    ]

    check_board = [
    ["R","N","B","Q","K","B","N","R"],
    ["P","P","P","P","P","P","P","P"],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    ["p","p","p","p","p","p","p","p"],
    ["r","n","b","q","k","b","n","r"]
    ]

def is_in_check(board, color):

    print("is_in_check running")

    # FIRST: find the KING

    target = "K" if color else "k"

    for row in range(8):

        for col in range(8):

            if board[row][col] == target:

                print("king found")

                king = (row, col)

                break

    # first: check if king is attacked horizontally/vertically

    for i in range(king[0] + 1, 8):

        print("vertically moving")

        if board[i][king[1]] != 0:

            print("unoccupied space at " + str(board[i][king[1]]))

            if board[i][king[1]].isupper() != color and board[i][king[1]].lower() == "r" or board[i][king[1]].lower() == "q":
                print("you are in check (vertically up)")
                #return True

            else:

                break

    for i in range(king[0]-1, 0):


        if board[i][king[1]] != 0:

            if board[i][king[1]].isupper() != color and board[i][king[1]].lower() == "r" or board[i][king[1]].lower() == "q":
                print("you are in check (vertically down)")
                #return True

            else:

                break

    for i in range(king[1] + 1, 8):

        print("horizontally moving (right)")

        if board[king[0]][i] != 0:

            print(str(board[king[0]][i]) + " is not occupied")

            if board[king[0]][i].isupper() != color and board[king[0]][i].lower() == "r" or board[king[0]][i].lower() == "q":
                print("you are in check (horizontally right)")
                #return True

            else:

                break

    for i in range(king[1] - 1, 0):

        print("horizontally moving (left)")

        if board[king[0]][i] != 0:

            if board[king[0]][i].isupper() != color and board[king[0]][i].lower() == "r" or board[king[0]][i].lower() == "q":
                print("you are in check (horizontally left)")
                #return True

            else:

                break

    # second: check if king is attacked diagonally
    row = king[0]+1
    col = king[1]+1
    while row <8 and col < 8:
        if board[row][col] != 0:

            if board[row][col].isupper() != color and board[row][col].lower() == "b" or board[row][col].lower() == "q":
                print("you are in check diagonally up right")
                #return True

            else:

                break
        row = row + 1
        col = col + 1

    row = king[0]-1
    col = king[1]+1
    while row > 0 and col < 8:
        if board[row][col] != 0:

            if board[row][col].isupper() != color and board[row][col].lower() == "b" or board[row][col].lower() == "q":

                print("you are in check down up right")
                #return True

            else:

                break
        row = row - 1
        col = col + 1

    row = king[0]-1
    col = king[1]-1
    while row > 0 and col > 0:
        if board[row][col] != 0:

            if board[row][col].isupper() != color and board[row][col].lower() == "b" or board[row][col].lower() == "q":
                print("you are in check diagonally down left")
                #return True

            else:

                break
        row = row - 1
        col = col - 1

    row = king[0]+1
    col = king[1]-1
    while row <8 and col > 0:
        if board[row][col] != 0:

            if board[row][col].isupper() != color and board[row][col].lower() == "b" or board[row][col].lower() == "q":
                print("you are in check diagonally up left")
                #return True

            else:

                break
        row = row + 1
        col = col - 1

    # third: check if king is attacked by knight

    if king[0] < 6 and king[1] < 6:

        if str(board[king[0] + 1][king[1] + 2]).lower() == "n":

            if board[king[0] + 1][king[1] + 2].isupper() != color:
                print("you are in check knight")
                #return True

        if str(board[king[0] + 2][king[1] + 1]).lower() == "n":

            if board[king[0] + 2][king[1] + 1].isupper() != color:
                print("you are in check knight")
                #return True

    if king[0] > 1 and king[1] < 6:

        if str(board[king[0] - 1][king[1] + 2]).lower() == "n":

            if board[king[0] - 1][king[1] + 2].isupper() != color:
                print("you are in check knight")
                #return True

        if str(board[king[0] - 2][king[1] + 1]).lower() == "n":

            if board[king[0] - 2][king[1] + 1].isupper() != color:
                print("you are in check knight")
                #return True

        # halfway

    if king[0] < 6 and king[1] > 1:

        if str(board[king[0] + 1][king[1] - 2]).lower() == "n":

            if board[king[0] + 1][king[1] - 2].isupper() != color:
                print("you are in check knight")
                #return True

        if str(board[king[0] + 2][king[1] - 1]).lower() == "n":

            if board[king[0] + 2][king[1] - 1].isupper() != color:
                print("you are in check knight")
                #return True

    if king[0] > 1 and king[1] > 1:

        if str(board[king[0] - 1][king[1] - 2]).lower() == "n":

            if board[king[0] - 1][king[1] - 2].isupper() != color:
                print("you are in check knight")
                #return True

        if str(board[king[0] - 1][king[1] - 2]).lower() == "n":

            if board[king[0] - 1][king[1] - 2].isupper() != color:
                print("you are in check knight")
                #return True
    #pawns

    if color:

        if str(board[king[0] + 1][king[1] + 1]) == "p" or str(board[king[0] + 1][king[1] - 1]) == "p":
            print("you are in check pawn")
            #return True

    if color:

        if str(board[king[0] - 1][king[1] + 1]) == "P" or str(board[king[0] - 1][king[1] - 1]) == "P":
            print("you are in check pawn")
            #return True

    return False

def is_legal(start_row, start_col, end_row, end_col, board, color):

    """
    start_row (int): Row of the piece to be moved
    start_col (int): Column of the piece to be moved
    end_row (int): Row of the desired end sqaure
    end_col (int): Column of the desired end square

    board (list): List of lists; array representing board state

    color (bool): Either 1 or 0, represents current player (white or black)
    """

    piece_type=str(board[start_row][start_col]).lower()

    print(piece_type)

    # FIRST things to check

    if str(board[end_row][end_col]) != '0' and str(board[start_row][start_col]).isupper() == str(board[end_row][end_col]).isupper():

        print("end square is occupied")

        return False

    if str(board[start_row][start_col]).isupper() != color:

        print("Cannot move opponet's piece")

        return False

    # check for piece

    # PAWN CASES (FINISHED)

    if piece_type == "p":

        forward = 1 if str(board[start_row][start_col]).isupper() else -1

        #move 2 from initial line
        #move 1 forward
        #taking (allowance for horizontal movement)

        if forward*(end_row-start_row) == 2 and (start_row == 1 or start_row == 6) and start_col == end_col and board[start_row - forward][start_col] != 0:

            return True

        elif forward * (end_row - start_row) == 1:

            if end_col == start_col and str(board[end_row][end_col]) == "0":

                return True

            elif abs(end_col - start_col) == 1 and str(board[end_row][end_col]) != "0" and str(board[end_row][end_col]).isupper() != str(board[start_row][start_col]).isupper():

                return True

            else:

                return False

        else:

            return False

    # knight CASES (FINISHED)

    if piece_type == "n":

        # no deliniation between colors, moves are the same for each

        # there are eight possible moves for any given

        if end_row == start_row + 1 or end_row == start_row - 1:

            if end_col == start_col + 2 or end_col == start_col - 2:

                return True

            else:

                return False

        elif end_row == start_row + 2 or end_row == start_row - 2:

            if end_col == start_col + 1 or end_col == start_col - 1:

                return True

            else:

                return False

        else:

            return False

    # ROOK CASES (FINISHED)

    if piece_type == "r":

        if end_col == start_col:

            # Rook is moving vertically

            #if end_row > start_row:

                # Rook is moving upward
            modifier = (start_row-end_row)//abs(start_row-end_row)
            for i in range(end_row+modifier, start_row, modifier):

                print(f"{i}: {board[i][start_col]}")
                if board[i][start_col] != 0:

                    return False


            return True


        elif end_row == start_row:

            # Rook is moving hortizontally
            modifier =  (start_col-end_col)//abs(start_col-end_col)
            for i in range(end_col+modifier, start_col, modifier):

                print(f"{i}: {board[start_row][i]}")
                if board[start_row][i] != 0:

                    return False


            return True

        else:

            return False

    # KING CASES (FINISHED)

    if piece_type == "k":

        if abs(end_col - start_col) < 2 and abs(end_row - start_row) < 2:

            return True

        else:

            return False

    # BISHOP CASES (FINISHED)

    if piece_type == "b":

        if abs(end_row - start_row) == abs(end_col - start_col):

            xd = 1 if end_col > start_col else -1
            yd = 1 if end_row > start_row else -1

            for i in range(1, abs(end_row - start_row)):

                if str(board[start_row + (i * yd)][start_col + (i * xd)]) != "0":

                    return False

            return True

        else:

            return False

    # QUEEN CASES (FINISHED)

    if piece_type == "q":

        # ROOK CASES

        if end_col == start_col:

            # Rook is moving vertically

            #if end_row > start_row:

                # Rook is moving upward
            modifier = (start_row-end_row)//abs(start_row-end_row)
            for i in range(end_row+modifier, start_row, modifier):

                print(f"{i}: {board[i][start_col]}")
                if board[i][start_col] != 0:

                    return False


            return True


        elif end_row == start_row:

            # Rook is moving hortizontally
            modifier =  (start_col-end_col)//abs(start_col-end_col)
            for i in range(end_col+modifier, start_col, modifier):

                print(f"{i}: {board[start_row][i]}")
                if board[start_row][i] != 0:

                    return False


            return True

        # BISHOP CASES

        elif abs(end_row - start_row) == abs(end_col - start_col):

            xd = 1 if end_col > start_col else -1
            yd = 1 if end_row > start_row else -1

            for i in range(1, abs(end_row - start_row)):

                if str(board[start_row + (i * yd)][start_col + (i * xd)]) != "0":

                    return False

            return True

        else:

            return False


def move (start_r, start_c, end_r, end_c, board, color):
    """
    start_r (int): Row of the piece to be moved
    start_c (int): Column of the piece to be moved
    end_r (int): Row of the desired end sqaure
    end_c (int): Column of the desired end square

    board (list): List of lists; array representing board state

    color (bool): Either 1 or 0, represents current player (white or black)
    """
    can_move = is_legal(start_r, start_c, end_r, end_c, board, color)
    if can_move == True:
        check_board[end_r][end_c]=str(check_board[start_r][start_c])
        check_board[start_r][start_c] = 0
        if is_in_check(check_board, color) == False:
            print(board[end_r][end_c])
            print("start:"+ str(board[start_r][start_c]))
            board[end_r][end_c]=str(board[start_r][start_c])
            print("final: "+ board[end_r][end_c])
            board[start_r][start_c] = 0
            check_board[start_r][start_c] = board[start_r][start_c]
            check_board[end_r][end_c] = board[end_r][end_c]

            return (board)

        else:

            print("You are in check")
            return "In check"
    #elif can_move == "in check"
    else:
        print('Illegal Move')
        return "Illegal Move"
