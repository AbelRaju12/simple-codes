# print a welcome game

print("\nWelcome to a lost ruin!")
print("You are a thrill seeker with a lust for adventure. On your journey through the remote parts of the Amazon rainforest, you stumble upon an ancient ruin.")
print("Curious as you are, you decided to take a look.")
print("The ruin is large, worn-out and falling apart. You enter through the destroyed front door.")
print("\nDo you want to enter the ""Vast hall"" before you or detour to the interesting looking ""Dinning room"" onto your left? ")

# the game!
player = True
sword = True
fruit = True
while(player):
    roomChoice = input("> ").lower()
    player = True
    if(roomChoice == "vast hall" or roomChoice == "hall"):
        print("\nYou entered the vast hall.")
        print("You see a shining sword kept on a mantle in the center of the room!")
        print("\nDo you take the sword?")
        while(sword):
            swordChoice = input("> ").lower()
            sword = True
            if(swordChoice == "yes"):
                print("\nYou get transported to the Grand Line. You are now Zoro with swords in each hand and one between your teeth.")
                player = False
                sword = False       
            elif(swordChoice == "no"):
                print("\nYou glare at the sword but doesn't touch it but suddenly it jumps from the mantle onto your hand. You get transported to the Grand Line and now you are Zoro with swords in each hand and one between your teeth. ")        
                player = False
                sword = False        
            else:
                print("Invalid choice! Enter yes or no.")
    elif(roomChoice == "dinning room" or roomChoice =="dining room" or roomChoice == "Dinning" or roomChoice == "Dining"):
        print("\nYou entered the dining room.")
        print("You see an interesting looking fruit on the dining table.")
        print("\nDo you take the fruit and eat it?")
        while(fruit):
            fruitChoice = input("> ").lower()
            fruit = True
            if(fruitChoice == "yes"):
                print("\nYou ate the fruit. Alas! it was rotten because duh..")
                print("You are dead.")
                player = False
                fruit = False
            elif(fruitChoice == "no"):
                print("\nYou decided to ignore the fruit.")
                print("Suddenly a sword comes flying to your hand  from somewhere and you get transported to the Grand Line. You are now Zoro with swords in each hand and one between your teeth.")
                player = False
                fruit = False
            else:
                print("Invalid choice! Enter yes or no.")    
    else:
        print("Invalid Choice!! Enter Vast hall or Dinning rooom")