board = [["","",""],["","","",],["","",""]]

print("Welcome to a game of tic-tac-toe!")
letters = ["X", "O", "x", "o"]
letter_selection = ""
letter_selection = input("Would you like to be X or O? ")
while letter_selection not in letters:
    print("Please choose an X or O.")
    letter_selection = input("Would you like to be X or O? ")
    print(letter_selection)

print("Let the game begin!")