#Global reitir
square1_1 = "(N)orth"
square1_2 = "(N)orth or (E)ast or (S)outh"
square1_3 = "(E)ast or (S)outh"
square2_1 = "(N)orth"
square2_2 = "(W)est or (S)outh"
square2_3 = "(E)ast or (W)est"
square3_1 = "(N)orth"
square3_2 = "(N)orth or (S)outh"
square3_3 = "(W)est or (S)outh"

def give_directions(row, column):
    if row == 1 and column == 1:
        return square1_1
    elif column == 1 and row == 2:
        return square1_2
    elif column == 1 and row == 3:
        return square1_3
    elif column == 2 and row == 1:
        return square2_1
    elif column == 2 and row == 2:
        return square2_2
    elif column == 2 and row == 3:
        return square2_3
    elif column == 3 and row == 1:
        return square3_1
    elif column == 3 and row == 2:
        return square3_2
    elif column == 3 and row == 3:
        return square3_3

def move_player(user_input, row, column):
    user_input = user_input.lower()
    if user_input == "w":
        if column > 1:
            column -= 1
            return row, column
    elif user_input == "e":
        if column < 3:
            column += 1
            return row, column
    elif user_input == "s":
        if row > 1:
            row -= 1
            return row, column
    elif user_input == "n":
        if row < 3:
            row += 1
            return row, column
    else:
        return None

row, column = 1,1

bool_controler = True
while bool_controler == True:
    print("You can travel:", give_directions(row, column))
    directions = input("Direction: ")

    if move_player(directions, row, column) == None:
        print("Not a valid direction")
    else:
        row, column = move_player(directions, row, column)

    if row == 1 and column == 3:
        break

print("Victory!")

