"""
Some notes about how to do make simple iterative string comparisons and use dictionary words guessing
"""

import random
import attotime


# implementation of strcmp with a timing increase
def compare1(str1, str2):
    """
    Here we're going to amplify the lib strcmp delays to make the weakness easier to analyze:
    1. evaluate strings l-to-r
    2. dope a positive match with a tiny wait to emphasize the delay for demonstration
    3. return a False match immediately
    """

    one, two = list(str1), list(str2)
    for x in range(0,len(one)):
        if one[x] == two[x]:
            time.sleep(.001)
            pass
        else:
            return False
    return True

# get a built-in dictionary
wordsraw = open('/usr/share/dict/words','r').readlines()
[x.strip('\n') for x in wordsraw]
words = [x.strip('\n') for x in wordsraw]


# set our name as 'apple'
name='apple'
# a longer one
name2 = 'unresourcefulness'


stash2 = {}
print('starting at:', datetime.now())
runstart = attotime.attodatetime.now()
for w in range(0,len(words)):
    start = attotime.attodatetime.now()
    if compare1(words[w], name):
            if compare1(words[w], name):
                if words[w] == name:
                    print('Name is', words[w])
                    break
            else:
                end = attotime.attodatetime.now()
                duration = end - start
                stash2[words[w]] = str(duration)
                print(words[w])
                stub = s
                break
    else:
        end = attotime.attodatetime.now()
        duration = end - start
        stash2[words[w]] = str(duration)
        pass
runend = attotime.attodatetime.now()
print('Finished. Total time:', runend - runstart)


#
stash3 = {}
for c in valid_chars:
    stub = c
    for loop in range(0, len(name2)):
    # create an array for each additional letter stub
        stublist = [stub + l for l in valid_chars]
        for s in stublist:
            start = attotime.attodatetime.now()
            if compare1(s, name2):
                if s == name2:
                    print('Name is', s)
                    break
                else:
                    end = attotime.attodatetime.now()
                    duration = end - start
                    stash3[s] = str(duration)
                    print(s)
                    stub = s
                    break
            else:
                end = attotime.attodatetime.now()
                duration = end - start
                stash3[s] = str(duration)
                pass

sorted(stash3.items(), key=lambda x: x[1])[-20:]
