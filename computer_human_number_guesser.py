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
    num, turn, inplay, guesses, lastguess, lo, hi = random.randint(1,101),'person',True,[], random.randint(1,101), 1, 100


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
            print(lastguess, guesses)


if __name__ == '__main__':
    print("starting game")
    newgame()
    print(num, turn, inplay, guesses)
    while True:
        if inplay == True:
            main()
        else:
            print('Game Over!')
            break

