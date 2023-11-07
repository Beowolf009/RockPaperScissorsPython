import random
import pygame

#initialize pygame
pygame.init()

#load sound bites
win_sound = pygame.mixer.Sound("sounds/winGameSound.mp3")
lose_sound = pygame.mixer.Sound("sounds/loseGameSound.mp3")
tie_sound = pygame.mixer.Sound("sounds/tieGameSound.mp3")

#define variables and set score to zero
weapon_choices = ['R', 'P', 'S']
score = {'player': 0, 'computer': 0}

# establish computer choices
def computer_random_choice():
    computer_selection = random.choice(weapon_choices)
    return computer_selection

# establish user inputs
def input_user_choice():
    print("R - Rock")
    print("P - Paper")
    print("S - Scissors")
    while True:
        human_selection = input("Please select a weapon or 'Q' to quit: ")
        if human_selection.upper() in ['R', 'P', 'S', 'Q']:
            return human_selection.upper()

# define how to determine a winner
def determine_winner(computer_weapon, human_weapon):
    if computer_weapon == human_weapon:
        
        return None
    elif (computer_weapon == 'R' and human_weapon == 'S') or (computer_weapon == 'P' and human_weapon == 'R') or (computer_weapon == 'S' and human_weapon == 'P'):
        return 0
    else:
        return 1
    
# start a scoring system
def display_scoreboard():
    print(f"Player: {score['player']} - Computer: {score['computer']}")

# build ASCII art to show choice
def display_choice_art(choice):
    if choice == 'R':
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.______)
        """)
    elif choice == 'P':
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    elif choice == 'S':
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

# set game parameters
while True:
    print("\nROCK, PAPER, SCISSORS")
    display_scoreboard()
    computer_choice = computer_random_choice()
    human_choice = input_user_choice()
    if human_choice == 'Q':
        print("Thanks for playing!")
        break
    print("Your choice:")
    display_choice_art(human_choice)
    print("Computer's choice:")
    display_choice_art(computer_choice)
    check_winner = determine_winner(computer_choice, human_choice)
    if check_winner == 1:
        print("You win this round!")
        win_sound.play()
        score['player'] += 1
        
    elif check_winner == 0:
        print('The computer wins this round!')
        lose_sound.play()
        score['computer'] += 1
    elif check_winner is None:
        tie_sound.play()
        print("It's a tie! Go again.")
    

