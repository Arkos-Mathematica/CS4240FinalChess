print("I'm chessing!")

board = [
["R","N","B","K","Q","B","N","R"],
["P","P","P","P","P","P","P","P"],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
["p","p","p","p","p","p","p","p"],
["r","n","b","k","q","b","n","r"]
]

def main():

    print(move("5254", board))

def is_legal(change, board):

    # set variables for rows and columns

    start_row = int(change[1])-1
    start_col = int(change[0])-1
    end_row = int(change[3])-1
    end_col = int(change[2])-1

    # FIRST thing to check

    if board[end_row][end_col] != 0 and board[start_row][start_col].isupper() == board[end_row][end_col].isupper():

        return False



    # check for piece



    # PAWN CASES

    if board[start_row][start_col].lower() == "p":

        if board[start_row][start_col] == "P":

            # if the piece is a white pawn:

            if end_col == start_col:

                # if the pawn is moving strictly forward:

                if end_row == start_row + 1:

                    # if the pawn is moving forward one space:

                    return True

                elif end_row == start_row + 2:

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

        elif board[start_row][start_col] == "p":

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

    if board[start_row][start_col].lower() == "k":

        # no deliniation between colors, moves are the same for each

        # there are eight possible moves for any given knight

        if end_row == start_row + 1 or end_row == start_row - 1:

            if end_col == start_col + 2 or end_col == start_col - 2:

                if board[end_row][end_col] == 0 or board[start_col][start_row].isupper() != board[end_row][end_col].isupper():

                    return True

                else:

                    return False

        if end_row == start_row + 2 or end_row == start_row - 2:

            if end_col == start_col + 1 or end_col == start_col - 1:

                if board[end_row][end_col] == 0 or board[start_col][start_row].isupper() != board[end_row][end_col].isupper():

                    return True

                else:

                    return False

def move (change, board):
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
        start_row = int(change[1])-1
        start_col = int(change[0])-1
        end_row = int(change[3])-1
        end_col = int(change[2])-1
        board[end_row][end_col]=board[start_row][start_col]
        board[start_row][start_col] = 0
        return (board)


main()
