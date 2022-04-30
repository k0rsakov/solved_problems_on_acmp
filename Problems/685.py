a = list(map(int, input().split()))
s1 = a[:3]
s1.sort()
s2 = a[3:]
s2.sort()
all_sand = s1[0] * s2[0] + s1[1] * s2[1] + s1[2] * s2[2]
print(all_sand)