a = list(map(int, input().split()))
A = a[0]
B = a[1]
C = a[2]
V = A * B * C
P = 2*(A * B + A * C + B * C)
print(P, V)