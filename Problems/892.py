day_of_year = {
1 : "Winter",
2 : "Winter",
3 : "Spring",
4 : "Spring",
5 : "Spring",
6 : "Summer",
7 : "Summer",
8 : "Summer",
9 : "Autumn",
10 : "Autumn",
11 : "Autumn",
12 : "Winter"
}
a = list(map(int, input().split()))
a = a[0]
if a > 12:
    print("Error")
else:
    print(day_of_year[a])