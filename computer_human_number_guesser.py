"""
 a turn based number guesser player between a human and the computer. 
 At numbers < 100, The computer should solve the problem in 5 turns or less
 Usage:  python computer_human_number_guesser.py
"""

import random 

def getguess():
    """
    get the guess from the player
    """
    guess = int(input("What's your guess - 1-100?, q: "))
    if ((guess <100) and (guess > 0)):
        return guess
    else:
        print("need an integer 1-100")
        return getguess()

def compguess(lastguess):
    """
    computer guesses by creating smaller ranges narrowing lo and hi values divided by 2
    """
    global guesses, lo, hi
    if lastguess > num:
        hi = lastguess
    elif lastguess < num:
        lo = lastguess + 1
    guess = (lo + hi) //2
    guesses.append(guess)
    return guess

def otherguy():
    """
    helper to switch turns
    """
    if turn == 'person':
        return 'computer'
    return 'person'


def outcome(guess):
    """
    who won?
    """
    global turn,inplay
    if guess == num:
        inplay = False
        return turn, 'correctly guessed', num
    else:
        turn = otherguy()
        return f"{guess} was not correct. {turn}'s turn"

def newgame():
    """
    set the global variables for a new game
    """
    global num, turn, inplay, guesses, lastguess, lo, hi
    num, turn, inplay, guesses, lastguess, lo, hi = random.randint(1,101),'person',True,[], random.randint(30,70), 1, 100


def main():
    """
    main turn based logic
    """
    global guesses, turn, inplay, lastguess
    while inplay:
        if turn == 'person':
            guess = getguess()
            print(outcome(guess))
        elif turn =='computer':
            guess = compguess(lastguess)
            lastguess = guess
            print(outcome(guess))
            print(lastguess, guesses, len(guesses), 'moves so far')


if __name__ == '__main__':
    print("*" *20)
    print("starting game")
    print("you're playing the computer - enter a number between 1 and 100 to take your turn.")
    print("if you miss, the computer will try.")
    print("*" *20)
    newgame()
	# for debugging
    # print(num, turn, inplay, guesses)
    while True:
        if inplay == True:
            main()
        else:
            print('Game Over!')
            break

