import random
import time

word_bank = ['dead','word','real','dead','deal','tied','open','shut','dunk','drug']
word_one = ''
word_two = ''
skipper = ""
score = 0

#play around with the score system

def main_menu(): #this function prints the main menu of the game and prompts user to make a choice
    print()
    print("----------------------------------")
    print("What would you like to do ?")
    print("     1. Read the rules")
    print("     2. Play the game")
    print("     3. Exit")
    print("")
    selection = int(input("Enter in your selection: "))
    print("----------------------------------")
    print("")
    return selection

def word_picker():
    global word_one
    global word_two
    word_one = random.choice(word_bank)
    word_two = random.choice(word_bank)
    while word_one == word_two:
        word_two = random.choice(word_bank)

def difference(original,new):
    counter = 0
    difference = 0
    for letter in original:   #for each letter in word 1 
        if letter != new[counter]: #if the letter is not equal to the users_word[index]
            difference += 1
        counter += 1
    return difference
   

    
        
def rules():
    print("Rules:")
    print("----------------------------------")
    print()
    print("The computer will randomly generate a starter word and an ending word and your job is to turn the starter word to the ending word by changing only one character in the least amount of attempts.")
    print()
    skipper = input("Press enter to continue...")

def game():
    global difference
    global word
    global score
    attempts = 0
    users_word = ''
    
    global word_one
    global word_two
    word_picker()
    
    
    print("Score: "+str(score))
    print()
    print("Turn this word: "+str(word_one))
    print("Into this word: "+str(word_two))
    print()
    
    #brainsssss
    
    while users_word != word_two:
        users_word = input("Enter word: ") #new 
        if users_word == "bypass": #admin controls for now 
            break
        users_word = list(users_word)
        word_one = list(word_one)
        word_two = list(word_two)
        users_word = list(users_word)
        comparrison = difference(word_one,users_word) #performs the comparisson
        if comparrison > 1:
            print("You can only change one letter at a time!")
            users_word = ''
            print()
        elif comparrison == 0:
            print("Cannot be the same word")
        else:
            word_one = users_word
        attempts += 1
    score += 1
    print()
    print("Congrads! You solved this puzzle!")
    print()
    
    
    
        
  
        






#main program

print("Hello and welcome to word ladder.")

choice = main_menu()  #Calls Main Menu and returns the user's selection

while choice !=3:
    if choice == 1:                  #User selects rules
        rules()

    elif choice == 2:      #User is ready to play
        game()
    
    else:
        print("Invalid Selection. Choose a number between 1 and 3.")
        
    choice = main_menu()
    
    
#goodbye message 

print("Have a good day!")
