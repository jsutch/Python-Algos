#/usr/bin/env python3

"""
Find the largest rectangle created by the area in a histogram

Every bar is pushed and popped a single time.  O(n).
"""

def largest_rectangle(hist):
    stack = []
    max_area = i = 0
    while i < len(hist):
        if (not stack) or (hist[stack[-1]] <= hist[i]):
            stack.append(i)
            i +=1
        else:
            top_of_stack = stack.pop()
            area = (hist[top_of_stack] * ((i - stack[-1] - 1) if stack else i))
            max_area = max(max_area, area)
    while stack:
        top_of_stack = stack.pop()
        area = (hist[top_of_stack] * ((i - stack[-1] -1) if stack else i))
        max_area = max(max_area, area)
    return max_area


"""
# helper code
In [68]: histarr1
Out[68]: [24, 29, 9, 37, 22, 33, 44, 24, 11, 27, 30, 18, 12, 24, 38, 47, 16, 17, 30, 4]

In [69]: histarr2 = [2,1,5,6,2,3]

In [70]: histarr3= [6, 2, 5, 4, 5, 1, 6]

In [74]: largest_rectangle(histarr1)
Out[74]: 176

In [76]: largest_rectangle(histarr2)
Out[76]: 10

In [77]: largest_rectangle(histarr3)
Out[77]: 12
"""
