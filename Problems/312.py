inF, outF = open('input.txt', 'r'), open('output.txt', 'w')
a = list(map(int, inF.read().split()))
step = a[1] - a[0]
outF.write(str(a[0]+step*(a[2]-1)))
inF.close()
outF.close()