#a = list(map(int, input().split()))
# a = 7
# b = 2
# d = a %b
# c = a//b
# f = b * c
# g = a - f
# print(
#     "a=", a, '\n'
#     "b=", b, '\n'
#     "Остаток от деления, %, d=", d, '\n'
#     "Деление без остатка, //, c=", c, '\n'
#     "Произведение b и остатка без деления, f=", f, '\n'
#     "а минус произведение, g=", g
# )

a = list(map(int, input().split()))
a = a[0]
b = 0
if a > 1:
    if a % 2 == 0:
        b = a/2
    elif a % 2 != 0:
        b = a
    elif a <= 1:
        b = 0
print(int(b))
