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

def is_legal(change, board, color):

    # set variables for rows and columns

    if color:

        start_row = 9 - int(change[1])
        start_col = 9 - int(change[0])
        end_row = 9 - int(change[3])
        end_col = 9 - int(change[2])

    else:

        start_row = int(change[1])-1
        start_col = int(change[0])-1
        end_row = int(change[3])-1
        end_col = int(change[2])-1

    piece_type=str(board[start_row][start_col]).lower()

    print(piece_type)
    # FIRST thing to check

    if board[end_row][end_col] != 0 and board[start_row][start_col].isupper() == board[end_row][end_col].isupper():

        return False



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

                    if color:

                        if start_row == 2:

                            pass

                    if board[end_row - 1][end_col] == 0:

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

    # KNIGHT CASES

    if piece_type == "k":

        # no deliniation between colors, moves are the same for each

        # there are eight possible moves for any given knight

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

def move (change, board, color):
    print(change)
    if change.upper() == "O-O-O":
        #queen side castle
        pass
    elif change.upper() == "O-O":
        #king side castle
        pass
    elif change[-2]=="=":
        #promotion
        pass
    else:
        if is_legal(change, board, color) == True:
            board[end_row][end_col]=board[start_row][start_col]
            board[start_row][start_col] = 0
            return (board)
        else:
            return "Illegal move"
