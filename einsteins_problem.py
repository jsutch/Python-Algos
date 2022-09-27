"""
- In a street there are five houses, painted five different colors.
- In each house lives a person of different nationality.
- These five homeowners each drink a different kind of beverage, smoke different brand of cigar and keep a different pet.
- The British man lives in a red house. 
- The Swedish man keeps dogs as pets. 
- The Danish man drinks tea. 
- The Green house is next to, and on the left of the White house. 
- The owner of the Green house drinks coffee. 
- The person who smokes montecristo rears birds. 
- The owner of the Yellow house smokes Cao. 
- The man living in the center house drinks milk. 
- The Norwegian lives in the first house (first house left to right).
- The man who smokes Blends lives next to the one who keeps cats. 
- The man who keeps horses lives next to the man who smokes Cao. 
- The man who smokes Partagas drinks beer. 
- The German smokes Cohiba. 
- The Norwegian lives next to the blue house.
- The Davidoff smoker lives next to the one who drinks water.
"""

from constraint import *

# create the object
problem = Problem()


# variable lists
nation = ["british","swedish","norwegian","german","danish"]
house = ["red", "green","yellow","blue","white"]
pet = ["dog","cat","fish","horse","bird"]
order = ["first","second","third","fourth","fifth"]
drink = ["beer","milk","water","coffee","tea"]
cigar = ["cohiba","montecristo","cao","davidoff","partagas"]


# create the meta list
criteria = nation + house + pet + drink + cigar

# add the house order
problem.addVariables(criteria,[1,2,3,4,5])


# apply the lists
print('apply the lists')
problem.addConstraint(AllDifferentConstraint(), nation)
problem.addConstraint(AllDifferentConstraint(), house)
problem.addConstraint(AllDifferentConstraint(), pet)
problem.addConstraint(AllDifferentConstraint(), drink)
problem.addConstraint(AllDifferentConstraint(), cigar)



# add constraints
print('adding constraints')
problem.addConstraint(lambda b, r: b == r, ['british','red'])
problem.addConstraint(lambda s, d: s == d,['swedish','dog'])
problem.addConstraint(lambda c, g: c == g,['coffee','green'])
problem.addConstraint(lambda d, t: d == t,['danish','tea'])
problem.addConstraint(lambda g, w: g-w == 1,['green','white'])
problem.addConstraint(lambda p, b: p == b, ['montecristo','bird'])
problem.addConstraint(lambda d, y: d == y, ["cao","yellow"])
problem.addConstraint(InSetConstraint([3]), ["milk"])
problem.addConstraint(InSetConstraint([1]), ["norwegian"])
problem.addConstraint(lambda d, h: abs(d-h) == 1, ("cao","horse"))
problem.addConstraint(lambda b, c: abs(b-c) == 1, ("davidoff","cat"))
problem.addConstraint(lambda bm, b: bm == b, ["partagas","beer"])
problem.addConstraint(lambda g, p: g == p, ["german","cohiba"])
problem.addConstraint(lambda k, h: abs(k-h) == 1, ["norwegian","blue"])


# get solution
print('getting solutions')
solution = problem.getSolutions()[0]

# print out list
print('printing list')
for i in range(1,6):
    for x in solution:
        if solution[x] == i:
            print(str(i), x)


"""
apply the lists
adding constraints
getting solutions
printing list
1 cao
1 norwegian
1 yellow
1 cat
1 water
2 horse
2 blue
2 danish
2 tea
2 davidoff
3 red
3 british
3 montecristo
3 bird
3 milk
4 white
4 swedish
4 dog
4 beer
4 partagas
5 green
5 coffee
5 german
5 cohiba
5 fish
"""

