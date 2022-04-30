inF, outF = open('input.txt', 'r'), open('output.txt', 'w')
a = list(map(int, inF.read().split()))
b = a[0]
outF.write(str(b*b-3*b+2))
inF.close()
outF.close()