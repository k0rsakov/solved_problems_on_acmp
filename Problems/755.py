a = list(map(int, input().split()))
if a[0] + a[1] - a[2] < 0:
    print("Impossible")
else:
    print(
        a[0] + a[1] - a[2]
    )
