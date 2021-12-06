print("I'm chessing!")

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

def is_in_check(board, color):

    # FIRST: find the KING

    target = "K" if color else "k"

    for row in board:

        for col in row:

            if board[row][col] == target:

                king = (row, col)

                break

    # first: check if king is attacked horizontally/vertically


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
    # FIRST thing to check

    if str(board[end_row][end_col]) != '0' and str(board[start_row][start_col]).isupper() == str(board[end_row][end_col]).isupper():

        return False

    # SECOND thing to check: check


    # check for piece

    # PAWN CASES

    if piece_type == "p":

        if color:

            # if the piece is a white pawn:

            if end_col == start_col:

                # if the pawn is moving strictly forward:

                if end_row == start_row + 1:

                    # if the pawn is moving forward one space:

                    if board[end_row][end_col] == 0:

                        return True

                    else:

                        return False

                elif end_row == start_row + 2:

                    if color and start_row == 2:

                            return True

                    elif board[end_row - 1][end_col] == 0:

                        return True

                    else:

                        return False

            elif end_col == start_col + 1 or end_col == start_col - 1:

                # pawn must be capturing

                if board[end_row][end_col] != 0:

                    if end_row == start_row + 1:

                        if board[start_row][start_col].isupper() != board[end_row][end_col].isupper():

                            return True

                    else:

                        return False

                else:

                    return False
            else:

                return False

        elif not color:

            # if the piece is a black pawn:

            if end_col == start_col:

                # if the pawn is moving strictly forward:

                if end_row == start_row - 1:

                    # if the pawn is moving forward one space:

                    return True

                elif end_row == start_row - 2:

                    # if the pawn is moving forward two spaces:

                    if board[end_row + 1][end_col] == 0:

                        return True

                    else:

                        return False

            elif end_col == start_col + 1 or end_col == start_col - 1:

                # pawn must be capturing

                if board[end_row][end_col] != 0:

                    if end_row == start_row - 1:

                        if board[start_row][start_col].isupper() != board[end_row][end_col].isupper():

                            return True

                    else:

                        return False

                else:

                    return False
            else:

                return False

    #  CASES

    if piece_type == "n":

        # no deliniation between colors, moves are the same for each

        # there are eight possible moves for any given

        if end_row == start_row + 1 or end_row == start_row - 1:

            if end_col == start_col + 2 or end_col == start_col - 2:

                if board[end_row][end_col] == 0 or board[start_col][start_row].isupper() != board[end_row][end_col].isupper():

                    return True

                else:

                    return False

        elif end_row == start_row + 2 or end_row == start_row - 2:

            if end_col == start_col + 1 or end_col == start_col - 1:

                if board[end_row][end_col] == 0 or board[start_col][start_row].isupper() != board[end_row][end_col].isupper():

                    return True

                else:

                    return False

            else:

                return False

        else:

            return False

    # ROOK CASES

    if piece_type == "r":

        if end_col == start_col:

            # Rook is moving vertically

            #if end_row > start_row:

                # Rook is moving upward

            for i in range(end_row, start_row, (start_row-end_row)//abs(start_row-end_row)):

                print(f"{i}: {board[i][start_col]}")
                if board[i][start_col] != 0:

                    return False


            return True

            '''if end_row < start_row:

                # Rook is moving downward

                for i in range(end_row, start_row-1):
                    print(board[i][start_col])
                    if board[i][start_col] != 0:

                        return False

                return True'''

        elif end_row == start_row:

            # Rook is moving hortizontally

            if end_col > start_col:

                # Rook is moving to the right

                for i in range(end_row - start_row):

                    if board[i][start_col] != 0:

                        return False

                return True

            if end_col < start_col:

                # Rook is moving to the left

                for i in range(end_row - start_row):

                    if board[i][start_col] != 0:

                        return False

                return True
        else:

            return False

    # KING CASES

    if piece_type == "k":

        if abs(end_col - start_col) == 1 or abs(end_row - start_row) == 1:

            return True

        else:

            return False

    # BISHOP CASES

    if piece_type == "b":

        if end_row > start_row and end_col > start_col:

            # bishop is moving up and to the right

            if end_row - start_row == end_col - start_col:

                for i in range(end_row - start_row):

                    if board[start_row + i][start_col + i] != 0:

                        return False

                return True

            else:

                return False

        if end_row < start_row and end_col > start_col:

            # bishop is moving down and to the right

            if start_row - end_row == end_col - start_col:

                for i in range(start_row - end_row):

                    if board[start_row - i][start_col + i] != 0:

                        return False

                return True

            else:

                return False

        if end_row > start_row and end_col < start_col:

            # bishop is moving up and to the left

            if end_row - start_row == start_col - end_col:

                for i in range(end_row - start_row):

                    if board[start_row + i][start_col - i] != 0:

                        return False

                return True

            else:

                return False

        if end_row < start_row and end_col < start_col:

            # bishop is moving down and to the left

            if start_row - end_row == start_col - end_col:

                for i in range(start_row - end_row):

                    if board[start_row - i][start_col - i] != 0:

                        return False

                return True

            else:

                return False

    # QUEEN CASES

    if piece_type == "q":

        # ROOK CASES

        if end_col == start_col:

            # Rook is moving vertically

            if end_row > start_row:

                # Rook is moving upward

                for i in range(end_row - start_row):

                    if board[i][start_col] != 0:

                        return False

                return True

            if end_row < start_row:

                # Rook is moving downward

                for i in range(end_row - start_row):

                    if board[i][start_col] != 0:

                        return False

                return True

        elif end_row == start_row:

            # Rook is moving hortizontally

            if end_col > start_col:

                # Rook is moving to the right

                for i in range(end_row - start_row):

                    if board[i][start_col] != 0:

                        return False

                return True

            if end_col < start_col:

                # Rook is moving to the left

                for i in range(end_row - start_row):

                    if board[i][start_col] != 0:

                        return False

                return True

        # BISHOP CASES

        if end_row > start_row and end_col > start_col:

            # bishop is moving up and to the right

            if end_row - start_row == end_col - start_col:

                for i in range(end_row - start_row):

                    if board[start_row + i][start_col + i] != 0:

                        return False

                return True

            else:

                return False

        if end_row < start_row and end_col > start_col:

            # bishop is moving down and to the right

            if start_row - end_row == end_col - start_col:

                for i in range(start_row - end_row):

                    if board[start_row - i][start_col + i] != 0:

                        return False

                return True

            else:

                return False

        if end_row > start_row and end_col < start_col:

            # bishop is moving up and to the left

            if end_row - start_row == start_col - end_col:

                for i in range(end_row - start_row):

                    if board[start_row + i][start_col - i] != 0:

                        return False

                return True

            else:

                return False

        if end_row < start_row and end_col < start_col:

            # bishop is moving down and to the left

            if start_row - end_row == start_col - end_col:

                for i in range(start_row - end_row):

                    if board[start_row - i][start_col - i] != 0:

                        return False

                return True

            else:

                return False

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

    if is_legal(start_r, start_c, end_r, end_c, board, color) == True:
        print(board[end_r][end_c])
        board[end_r][end_c]=str(board[start_r][start_c])
        print("final: "+ board[end_r][end_c])
        board[start_r][start_c] = 0
        return (board)
    else:
        print('Illegal Move')
        return "Illegal move"
