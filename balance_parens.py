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
                # print "pop, last char", (last, c)
                if (last, c) not in match:
                    return 0, "Unbalanced - stack may have leftovers", stack
    return 1, "Balanced - stack should be empty", stack
