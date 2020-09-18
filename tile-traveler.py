#https://github.com/creep1g/TileTraveler
#Global reitir
square1_1 = "(N)orth."
square1_2 = "(N)orth or (E)ast or (S)outh."
square1_3 = "(E)ast or (S)outh."
square2_1 = "(N)orth."
square2_2 = "(S)outh or (W)est."
square2_3 = "(E)ast or (W)est."
square3_1 = "(N)orth."
square3_2 = "(N)orth or (S)outh."
square3_3 = "(S)outh or (W)est."

def walls(directions, row, column):
    '''Innri veggir - gefur True ef það má ekki fara í ákveðna átt, annars False'''
    if column == 1 and row == 1:
        if directions == "e":
            return True
    elif column == 2 and row == 1:
        if directions == "e":
            return True
        elif directions == "w":
            return True
    elif column == 2 and row == 2:
        if directions == "e":
            return True
        elif directions == "n":
            return True
    elif column == 2 and row == 3:
        if directions == "s":
            return True
    elif column == 3 and row == 2:
        if directions == "w":
            return True
    else:
        return False

def give_directions(row, column):
    '''Finnur staðsetningu leikmans og gefur viðeigandi skilaboð'''
    if column == 1:
        if row == 1:
            return square1_1
        elif row == 2:
            return square1_2
        elif row == 3:
            return square1_3
    elif column == 2:
        if row == 1:
            return square2_1
        elif row == 2:
            return square2_2
        elif row == 3:
            return square2_3
    elif column == 3:
        if row == 1:
            return square3_1
        elif row == 2:
            return square3_2
        elif row == 3:
            return square3_3

def move_player(user_input, row, column):
    '''Athugar hvort leikamaður hefur valið mögulega átt skilar þeim hnitum ef svo er
    annars skilar hann None og leikmaður færist ekki um reit'''
    user_input = user_input.lower()

    if walls(user_input, row, column):
        return None
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

# Byrjunarreitur
row, column = 1,1

bool_controler = True
while bool_controler == True:

    print("You can travel:", give_directions(row, column))
    directions = input("Direction: ")

    if move_player(directions, row, column) == None:
        print("Not a valid direction!")
    else:
        row, column = move_player(directions, row, column)
    # Athugar hvort leikmaður sé á vinningsreitinum
    if row == 1 and column == 3:
        bool_controler = False

print("Victory!")

