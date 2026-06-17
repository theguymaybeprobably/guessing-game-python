import random
play = input("Play? y/n").lower()
while play != "y" and play != "n":
    print("Please only type y/n")
    play = input("Play? y/n").lower()
if play == "y":
    lowerbound = int(input("Enter lower bound:"))
    upperbound = int(input("Enter upper bound:"))
    if lowerbound >= upperbound:
        print("Invalid range!")
        exit()
    print(f"You only have 10 guesses to guess a random integer from {lowerbound} to {upperbound}")
    guesses = 0
    number = random.randint(lowerbound,upperbound)
    while guesses < 10:
        try:
            guess = int(input("Guess:"))
        except ValueError:
            print("Only type numbers!")
            continue
        if guess > upperbound:
            print("Guess must not be greater than the upper bound!")
            continue
        elif guess < lowerbound:
            print("Guess must not be less than the lower bound!")
            continue
        elif guess == number:
            print(f"You win in {1+guesses} attempts!")
            break
        elif guess > number:
            print("Guess too high!")
            guesses += 1
            print(f"Attempts left: {7-guesses}")
        elif guess < number:
            print("Guess too low!")
            guesses += 1
            print(f"Attempts left: {7-guesses}")
    else:
        print(f"GAME OVER! THE NUMBER WAS {number}")
elif play == "n":
    print("Thank you! Goodbye!")
