print("I'm chessing!")
def main():
    position= [
    ["R","N","B","K","Q","B","N","R"],
    ["P","P","P","P","P","P","P","P"],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    ["p","p","p","p","p","p","p","p"],
    ["r","n","b","k","q","b","n","r"]
    ]
    print(move("21","41", position))
def move (start, end, position):
    start_row = int(start[0])-1
    start_col = int(start[1])-1
    end_row = int(end[0])-1
    end_col = int(end[1])-1
    position[end_row][end_col]=position[start_row][start_col]
    position[start_row][start_col] = 0
    return (position)
main()

print("Checking... tv")
