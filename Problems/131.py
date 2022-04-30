inF, outF = open('input.txt', 'r'), open('output.txt', 'w')
a = list(map(int, inF.read().split()))
max = 0
mans = []

i = 2
while i < len(a):
    if a[i] == 1:
        if a[i-1] > max:
            max = a[i-1]
        mans.append(a[i-1])
    i += 2
# print(mans)

if max == 0:
    print(-1)
else:
    for i in range(0, len(mans)):
        if mans[i] == max:
            print(i+1)
            break


















# for i in range(1, len(a)):
#      i += 1
#     print(a[i])
# mans = []
# peoples = []
# i = 2
# while i < len(a):
#     # print(a[i])
#     # print(f'nubmer i={i}')
#     if a[i] == 1:
#         mans.append(a[i-1])
#     i += 2
#
# j = 1
# while j < len(a):
#     # print(a[i])
#     # print(f'peoples i={i}')
#     peoples.append(a[j])
#     j += 2
#
# print(peoples)

# if len(mans) == 0:
#     outF.write(str(-1))
# else:
#     age = max(mans)
#
#     index = []
#     for i in range(0, len(mans)):
#         # print(f'number={i} num_array={}')
#         if mans[i] == age:
#             index.append(i+1)
#     outF.write(str(min(index)))



inF.close()
outF.close()