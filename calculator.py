running = True

while(running):
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Remainder")
    print("6. Exit\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("\nEnter the numbers to add")
        x=float(input())
        y=float(input())
        # z=x+y
        print("\nThe sum of", x, "and", y, "is", float(x)+float(y), "\n")
    elif choice == 2:
        print("\nEnter the numbers to subtract")
        x=float(input())
        y=float(input())
        # z=x-y
        print("\nThe difference between", x, "and", y, "is", float(x)-float(y), "\n")
    elif choice == 3:
        print("\nEnter the numbers to multiply")
        x=float(input())
        y=float(input())
        # z=x*y
        print("\nThe product of", x, "and", y, "is", float(x)*float(y), "\n")
    elif choice == 4:
        print("\nEnter the numbers to divide")
        x=float(input())
        y=float(input())
        # z =float(x / y)
        print("The quotient of", x, "divided by", y, "gives", float(x/y), "\n")
    elif choice == 5:
        print("\nEnter the numbers to divide")
        x=float(input())
        y=float(input())
        # z =float(x % y)
        print("The remainder of", x, "divided by", y, "gives", float(x%y), "\n")        
    elif choice == 6:
        running = False
    else:
        print("\nInvalid Input!!!\n")    