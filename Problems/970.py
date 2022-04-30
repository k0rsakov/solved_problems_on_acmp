a = list(map(int, input().split()))
a1 = a[0]
a2 = a[1]
a3 = a[2]

if a1 + a2 == a3 or a1 + a3 == a2 or a3 + a2 == a1:
    print("YES")
else:
    print("NO")