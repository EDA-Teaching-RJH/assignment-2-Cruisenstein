### Part Two -- your code goes here. 

num = 34

start = str(input("Would you like to begin? (y/n)"))

while start == "y":
    guess = int(input("Guess the number between 1-100."))
    if guess == num:
        print("WELL DONE CORRECT!")
        break
    elif guess < num:
        print("HIGHER")
    else:
        print("LOWER")
