import random
import math

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

chances = round(math.log(upper - lower + 1, 2))

print("You've only", chances, "chances") # or add round(math.log(upper - lower + 1, 2)) in the chances place

x = random.randint(lower, upper)

count=0

while count < math.log(upper - lower + 1, 2):
    count+=1
    guess=int(input("\nEnter your guess now!: "))
    
    if x == guess:
        print("congratulations! You've got it in",count," tries")
        break
    elif x > guess:
        print("You've guessed too small!")
    elif x < guess:
        print("you've guess too big!")


if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\nBetter Luck Next time!")