import random

options = ["rock", "paper", "scissors"]

running = True
while running:
    computer = random.choice(options)
    player = None
    
    while player not in options:
        player = input("Enter your choice (rock, paper, scissors): ").lower()
        if player not in options:
            print("Enter a valid choice!")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer :
        print("\nIt's a tie!")
    elif player == "rock" and computer  == "scissors":
        print("\nYou win!")
    elif player == "paper" and computer  == "rock":
        print("\nYou win!")
    elif player == "scissors" and computer  == "paper":
        print("\nYou win!")       
    else:
        print("\nYou lose!")
        
    if not input("\nPress y to continue: " ).lower() == "y":
        running = False
print("\nThanks for playing!")