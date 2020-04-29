def wordsort(word):
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



def reversewordsort(word):
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


wordsort('supercalifragilisticexplialidocious')
