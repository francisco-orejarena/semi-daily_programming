print("Please think of a number between 0 and 100!")
lo = 0
hi = 100
while True:
    guess = (hi + lo) // 2
    print("Is your secret number", guess)
    ans = input("Enter 'h' to indicate the guess is too high. "
                "Enter 'l' to indicate the guess is too low. "
                "Enter 'c' to indicate I guessed correctly. ")
    if ans == "h":
        hi = guess
    elif ans == "l":
        lo = guess
    elif ans == 'c':
        print("Game over. Your secret number was:", guess)