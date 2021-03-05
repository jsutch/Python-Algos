"""
 one way computer guesser
"""
from random import randint

def guesser(n):
    low, hi = 1, 100
    guess = random.randint(1,100)
    while guess != n:
        print("The computer takes a guess...", guess)
        if guess > n:
            high = guess
        elif guess < n:
            low = guess + 1
        guess = (low + high) //2
    print("computer guess of", guess, "is correct!")



def main():
    num = int(input("Enter a number: "))
    if num < 1 or num > 100:
        print("number must be between 1 and 100")
    else:
        guesser(num)

if __name__ == '__main__':
    main()
