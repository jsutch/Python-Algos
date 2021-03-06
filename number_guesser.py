"""
 one way computer guesser
"""
import random 

def guesser(n):
    #lo, hi = 1, 100
    lo, hi = 30, 70
    guesses = 0
    guess = random.randint(1,100)
    while guess != n:
        guesses +=1
        print(f"The computer takes guess number {guesses} with {guess} - no luck!")
        if guess > n:
            hi = guess
        elif guess < n:
            lo = guess + 1
        guess = (lo + hi) //2
    print(f"computer guess of {guess} if correct with  {guesses} number of guesses" )



def main():
    print("*" *20)
    print("computer number guessing game. you put in a number between 1 and 100 and the computer attempts to guess it")
    print("it should guess in 5 tries or less")
    print("*" *20)
    num = int(input("Enter a number: "))
    if num < 1 or num > 100:
        print("number must be between 1 and 100")
    else:
        guesser(num)

if __name__ == '__main__':
    main()
