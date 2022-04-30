inF, outF = open('input.txt', 'r'), open('output.txt', 'w')
a = list(map(int, (' '.join(inF.read())).split()))
sum = 0
for i in range(1, len(a)):
    sum += a[i]
outF.write(str(sum-a[0]+1))
inF.close()
outF.close()