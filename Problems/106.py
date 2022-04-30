o = 0
r = 0
i = 0
N = 0
a = list(map(int, input().split()))
a = a[0]
for i in range(a):
    N = input()
    if int(N) == 0:
        o += 1
    elif int(N) == 1:
        r += 1
print(min(o, r))
