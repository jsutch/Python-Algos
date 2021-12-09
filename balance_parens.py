test1='(h[e{lo}!]<~)()()()(' #unbalanced - 2 leftovers (, <
# test1='(h[e{lo}!]<~)(' #unbalanced - 1 leftover (
test2='({)}' #unbalanced - out of order closure - 2 leftovers ({
test3='(]' #unbalanced - 1 leftover (
test4=')' #unbalanced, empty stack test
test5='()' #balanced
test6='({<>})' #balanced
test7='(h[e{lo}!]~)' #balanced
test8='[](){}<>' #balanced, no leftovers
test8='}{][><)(' #balanced, no leftovers, but out of order


def balanced(string):
    stack=[]
    opens, closes = "<({[", ">)}]"
    match=set([ ('(',')'), ('[',']'), ('{','}'), ('<','>')])
    items=list(string)
    bal=-1
    for c in items:
        if c in opens:
            stack.append(c)
        elif c in closes:
            if not stack:
                return "Unbalanced - stack is empty", stack #unbalanced
            else:
                last=stack.pop()
                # print("pop, last char", (last, c))
                if (last, c) not in match:
                    return 0, "Unbalanced - stack may have leftovers", stack
    return 1, "Balanced - stack should be empty", stack


print("Test 1", balanced(test1))
print("Test 2", balanced(test2))
print("Test 3", balanced(test3))
print("Test 4", balanced(test4))
print("Test 5", balanced(test5))
print("Test 6", balanced(test6))
print("Test 7", balanced(test7))
print("Test 8", balanced(test8))
print("Test 9", balanced(test8))
