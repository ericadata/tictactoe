from random import choice

board = [["","",""],["","",""],["","",""]]
locations = [1,2,3,4,5,6,7,8,9]
counter = 0

def display_board():
    pass

def virtual_play():
    global counter
    if letter_selection == "X":
        virtual_letter = "O"
    virtual_letter = "X"
    location = choice(locations)
    print("The location {location} was taken!".format(location=location))
    counter += 1
    print(counter)
    locations.remove(location)

def player_play():
    global counter
    location = input("Where do you want the {letter_selection} to go? ".format(letter_selection=letter_selection))
    location = int(location)
    #print(location in locations)
    while location not in locations:
        print("That location is taken! Pick again.") 
        location = input("Where do you want the X to go? ")
        location = int(location)
    counter += 1
    print(counter)
    locations.remove(location)

print("Welcome to a game of tic-tac-toe!")
letters = ["X", "O", "x", "o"]
letter_selection = ""
letter_selection = input("Would you like to be X or O? ")
while letter_selection not in letters:
    print("Please choose an X or O.")
    letter_selection = input("Would you like to be X or O? ")
    print(letter_selection)

print("Let the game begin!")
print("""
----------------     1 | 2 | 3
TIC - TAC - TOE      4 | 5 | 6
________________     7 | 8 | 9

TO PLAY TIC - TAC - TOE, YOU NEED TO GET THREE IN A ROW.
YOUR CHOICES ARE BETWEEN 1 TO 9.
""")
while counter < 5:
    if letter_selection.upper() == "X":
        player_play()
    else:
        virtual_play()
    print("Now the computer shall chose a spot!")
    virtual_play()

