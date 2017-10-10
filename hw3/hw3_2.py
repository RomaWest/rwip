import math

s = input()
s_middle = int(math.ceil(len(s)/2))
s1 = s[:s_middle]
s2 = s[s_middle:]
s_result = s2 + s1

print(s_result)
