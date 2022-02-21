from random import choice

#CHANGE BOARD TO STRING THINGY THAT CAN BE PRINTED OUT
board = [["","",""],["","",""],["","",""]]
locations = [1,2,3,4,5,6,7,8,9]
counter = 0

#FILL THIS OUT
def display_board():
    pass

def virtual_play():
    global counter
    letter_selection = "O"
    location = choice(locations)
    print("The location {location} was taken!".format(location=location))
    counter += 1
    print(counter)
    locations.remove(location)

def player_play():
    global counter
    letter_selection = "X"
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

print("Let the game begin!")
print("""
----------------     1 | 2 | 3
TIC - TAC - TOE      4 | 5 | 6
________________     7 | 8 | 9

TO PLAY TIC - TAC - TOE, YOU NEED TO GET THREE IN A ROW.
YOUR CHOICES ARE BETWEEN 1 TO 9.
""")
#FIGURE OUT REVERSE LOGIC, WHAT IF THE OTHER PERSON IS O? OR JUST MAKE IT EASIER AND GET RID THE CHOICE
while counter < 5:
    player_play()
    virtual_play()
    print("Now the computer shall chose a spot!")
    virtual_play()

