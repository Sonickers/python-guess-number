from random import randint

print("Welcome! Write your name:")
my_name = input()
print("So, " + my_name + "." + " Lets play a game. Guess number between 1 - 20!" )

turn = 0
first_num = 1
last_num = 20
number = randint(first_num, last_num)

while turn < 4:
    guess = int(input())

    if guess == number:
        print("You won!")
        break
    else:
        turn += 1
        print("Lower!" if guess > number else "Higher!")
        print("Try again!" if turn < 4 else "Lose. :( The number was {}".format(number))