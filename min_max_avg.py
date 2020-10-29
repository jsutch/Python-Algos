#!/usr/local/bin/python
"""
Basic stats using python functions
"""
myarr = [1139, 3620, 3823, 2417, 2414, 1834, 2933, 151, 3899, 3841, 1023, 564, 1080, 323, 3337, 1549, 917, 1543, 910, 1150, 2878, 2525, 1407, 1548, 2808, 2444, 3899, 3120, 2382, 3037, 805, 791, 3795, 636, 3482, 2348, 3181, 3873, 311, 1719, 226, 667, 2820, 201, 1809, 3073, 1683, 2210, 3949, 1690, 787, 1051, 1330, 2617, 3086, 3606, 2254, 524, 3147, 3614, 1433, 3853, 1074, 1137, 1577, 2773, 1495, 1741, 3456, 2436, 880, 797, 597, 2450, 2383, 920, 208, 2024, 1125, 3383, 3290, 2508, 234, 382, 2870, 543, 2267, 1936, 772, 944, 3579, 2627, 1264, 1453, 3222, 679, 1271, 678, 3669, 1834]

def modeval(arr):
	"""
	there's got to be a better way to do this in a lambda one liner
	"""
   nums = {}
   for n in arr:
       if n in nums.keys():
           nums[n] +=1
       nums[n] = 1
   mode = sorted(nums.items(),key=lambda x: x[0])[0]
   if mode[1] < 2:
       return None
   return mode[0]



def stats(arr):
	return "Max", sorted(arr)[-1], "Min", sorted(arr)[0], "Average", sum(arr) / len(arr), "Range", sorted(arr)[-1] - sorted(arr)[0], "Mode?", modeval(myarr)



# stats([3,5,10,2,9,12])
# stats(myarr)