from random import choice

#CHANGE BOARD TO STRING THINGY THAT CAN BE PRINTED OUT
board = """
    1 | 2 | 3
    4 | 5 | 6
    7 | 8 | 9
    """
#[["","",""],["","",""],["","",""]]
locations = [1,2,3,4,5,6,7,8,9]
counter = 0

#FILL THIS OUT
def display_board():
    print(board)

def virtual_play():
    global counter
    letter_selection = "O"
    location = choice(locations)
    board.replace(str(location), letter_selection)
    print("The location {location} was taken!".format(location=location))
    counter += 1
    print(counter)
    locations.remove(location)

def player_play():
    global counter
    letter_selection = "X"
    location = input("Where do you want the X to go? ")
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

print("Let the game begin!")
print("""
----------------     1 | 2 | 3
TIC - TAC - TOE      4 | 5 | 6
________________     7 | 8 | 9

TO PLAY TIC - TAC - TOE, YOU NEED TO GET THREE IN A ROW.
YOUR CHOICES ARE BETWEEN 1 TO 9.
""")
while counter < 5:
    player_play()
    display_board()
    print("Now the computer shall chose a spot!")
    virtual_play()
    display_board()

positive = ["y", "Y", "Yes", "yes", "YES"]
negative = ["n", "N", "no", "NO", "No"]
end_game = input("Check the board. Did anyone win yet? ")
if end_game in positive:
    result = input("Did you win? y/n ")
    if result in positive:
        print("You won!")
    print("Better luck next time!")
else:
    while end_game not in positive:
        player_play()
        virtual_play()
        print(board)
        end_game = input("Check the board. Did anyone win yet? ")