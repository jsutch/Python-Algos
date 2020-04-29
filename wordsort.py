def lettersort(word):
    """
    Sort the letters of a string alphabetically by ascii comparison.
    Return as a string.
    """
    strarr = list(str((word))
    for i in range(len(strarr) - 1):
        for j in range(len(strarr) - i - 1):
            if strarr[j] > strarr[j + 1]:
                strarr[j],strarr[j+1] = strarr[j + 1], strarr[j]
    newstr =  "".join(strarr)
    return str(newstr)



def reverselettersort(word):
    """
    Sort the letters of a string alphabetically by ascii comparison.
    Return as a string.
    """
    strarr = list(str((word))
    for i in range(len(strarr) - 1):
        for j in range(len(strarr) - i - 1):
            if strarr[j] > strarr[j + 1]:
                strarr[j],strarr[j+1] = strarr[j + 1], strarr[j]
    strarr.sort()
    newstr =  "".join(strarr)
    return newstr


lettersort('supercalifragilisticexplialidocious')

def sortwords(phrase):
    words = phrase.split()
    for loop in range(len(words) -1, -1, -1):
        for x in range(loop):
            if words[x][0] > words[x + 1][0]:
                words[x],  words[x+1] =  words[x+1],  words[x]
    return words
words = phrase.split()
sortwords(phrase)
def sortwordsreverse(phrase):
    words = phrase.split()
    for loop in range(len(words) -1, -1, -1):
        for x in range(loop):
            if words[x][0] > words[x + 1][0]:
                words[x],  words[x+1] =  words[x+1],  words[x]
    return words[::-1]

