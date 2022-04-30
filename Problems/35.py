inF, outF = open('input.txt', 'r'), open('output.txt', 'w')

array = inF.read().split()

list_n = []
list_m = []

for i in range(1, len(array)):
    if i % 2 == 1:
        list_n.append(int(array[i]))
    else:
        list_m.append(int(array[i]))

print('ar_n',list_n,'arr_m',list_m)

for i in range(len(list_n)):
    result = int(19 * list_m[i] + (list_n[i] + 239) * (list_n[i] + 366) / 2)
    outF.write(str(result)+'\n')
    # print(result)

inF.close()
outF.close()