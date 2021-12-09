def ispal(word):
    if " " in word:
        word = "".join(word.split())
    for i in range(0, len(word)//2):
        if word[i] != word[len(word) -i -1]:
            return False
    return True

# tests
# true test
print(ispal('amanaplanacanalpanama'))
# are spaces working
print(ispal('a man a plan a canal panama'))
# false test
print(ispal('yo momma'))
