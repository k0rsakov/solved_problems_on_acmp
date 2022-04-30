inF, outF = open('input.txt', 'r'), open('output.txt', 'w')
array = inF.read()
if sum(map(int, array[0:3])) == sum(map(int, array[3:6])):
    outF.write('YES')
else:
    outF.write('NO')
