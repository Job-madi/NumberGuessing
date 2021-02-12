import random
#guess the random number program
randomNum = random.randrange(1, 101)


def check(guess):
    if (randomNum == guess):
        answer = "You've guess the right number!"
        return answer


def difference(guess):
    difference = randomNum - guess
    return difference


while True:
    try:
        guessedNum = int(input('Please enter your guessed Number'))
        if (isinstance(check(guessedNum), str)):
            print(check(guessedNum))
            break
        elif (isinstance(difference(guessedNum), int)):
            print(f'The difference is ${difference(guessedNum)}')

    except ValueError:
        print("You've entered an invalid number")
