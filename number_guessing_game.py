import random

print("Welcome to the Number Guessing Game!\n")
start_point = int(input("Enter starting number : "))
end_point = int(input("Enter ending number : "))

number = random.randint(start_point,end_point)

print(f"Select a number between {start_point} and {end_point} : ")

while True:
    user_guess = int(input("Guess number : "))
    if user_guess > number:
        print("Guess lower, try again!")
    elif user_guess < number:
        print("Guess higher, try again!")
    else:
        print("Bingo! Correct Answer")
        break