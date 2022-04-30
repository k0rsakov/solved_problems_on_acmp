inF = open('input.txt', 'r')
outF = open('output.txt', 'w')
c = inF.read()
array = c.split()
a = int(array[0])
b = int(array[1])
c = int(array[2])
if a*b==c:
    print("YES", file=outF)
else:
    print("NO", file=outF)
inF.close()
outF.close()