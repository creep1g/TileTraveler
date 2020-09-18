# https://github.com/creep1g/TileTraveler

# Global reitir.
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
    """Innri veggir - gefur True ef það má ekki fara í ákveðna átt, annars False."""
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
    """Finnur staðsetningu leikmanns og gefur upp mögulega reiti."""
    if column == 1:
        if row == 1:
            return square1_1        # (1,1)
        elif row == 2:
            return square1_2        # (1,2)
        elif row == 3:
            return square1_3        # (1,3)
    elif column == 2:
        if row == 1:
            return square2_1        # (2,1)
        elif row == 2:
            return square2_2        # (2,2)
        elif row == 3:
            return square2_3        # (2,3)
    elif column == 3:
        if row == 1:
            return square3_1        # (3,1)
        elif row == 2:
            return square3_2        # (3,2)
        elif row == 3:
            return square3_3        # (3,3)

def move_player(user_input, row, column):
    """Athugar hvort leikamaður hefur valið mögulega átt & skilar þeim hnitum
    ef svo er annars skilar hann None & leikmaður færist ekki um reit."""
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

def victory(row, column, bool_controller):
    """Stöðvar keyrslu á forritinu þegar notandi fer
    á vinningsreit & prentar út vinningsskilaboð."""
    bool_controller = False
    return bool_controller, print("Victory!")

# Forritið byrjar hér.
row, column = 1,1       # Byrjunarreitur.
bool_controller = True

while bool_controller == True:
    # Keyrir þangað til notandi fer á reit (1,3), þá hættir keyrslan.
    print("You can travel:", give_directions(row, column))
    directions = input("Direction: ")
    directions = directions.lower()     # Leyfir notanda að nota há & lágstafi.

    if move_player(directions, row, column) == None:
        print("Not a valid direction!")
    else:
        row, column = move_player(directions, row, column)
    if row == 1 and column == 3:        # Athugar hvort leikmaður sé á vinningsreitinum (3,1).
        bool_controller = victory(row, column, bool_controller)
