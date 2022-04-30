a = list(map(int, input().split()))
W = a[0]
H = a[1]
R = a[2]

# W = 4
# H = 7
# R = 3
D = R * 2

if D <= W and D <= H:
    print("YES")
else:
    print("NO")
