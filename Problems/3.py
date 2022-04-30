# а = list(map(int, input().split()))
a = int(input())
b = 25
step = a // 10
c = 0
c = step * (step + 1)
if c == 0:
    print(25)
else:
    print(c, b, sep="")
