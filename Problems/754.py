inF = list(map(int, input().split()))
a = inF[0]
b = inF[1]
c = inF[2]
d = 0
if a >= 94 and a <= 727 and b >= 94 and b <= 727 and  c >= 94 and c <= 727:
    d = max(a, b, c)
    print(d)
else:
    print("Error")
#
#     :
# d = 0
# d = max(a, b, c)
# if d >= 94 and d <= 727:
#     print(d)
# else:
#     print("Error")