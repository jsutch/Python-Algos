"""
small snippet to find duplicates in short segments of descriptive notes. 

In this case there are two types of recommendations - positive and negative. 
Sometimes the "positive" recommendations are duplicated in the same list and 
sometimes they are mistakenly placed in the "negative" list. 

This code will look at a line, then examine the next 10 lines to see if there's a dupe.
Since some headers will naturally be copies, we want to ignore those.


* **positive recommendation**
* reviews list of requirements
* removes problematic requirements
* adds notes regularly
* regularly creates new lists
* completes new lists
* adds notes regularly

* **negative recommendations**
* doesn't list notes
* adds notes regularly
* misses deadlines

"""

mytextraw = open('mytext.md','r').read()

for x in range (2,len(mytextraw) -1):
    if '*' in mytextraw[x] and '**' not in mytextraw[x] and mytextraw[x] != "\n":
        if mytextraw[x] in  mytextraw[x + 1:x + 10]:
            print(mytextraw[x], mytextraw[x + 1:x + 10])
