# # a = list(map(int, input().split()))
# # a = a[0]
#
# petya = 1
# katya = 4
# sersh = 1
#
# katya1 = (petya+sersh)*2
#
# obsh = katya + petya + sersh
# # print(
# #     katya1, obsh
# # )

a = list(map(int, input().split()))
a = a[0]
obr = a // 3
petya = obr // 2
sersh = obr // 2
katya = a - (petya+sersh)
print(
     petya, katya, sersh
)