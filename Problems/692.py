# a = list(map(int, input().split()))
# a = a[0]
# b = a % 2
# if b == 0:
#     print("YES")
# else:
#     print("NO")

a = list(map(int, input().split()))
a = a[0]
n = 1
while n < a:
    n *= 2

if (n == a):
    print("YES")
else:
    print("NO")