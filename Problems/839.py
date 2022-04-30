inF, outF = open('input.txt', 'r'), open('output.txt', 'w')
a = list(map(int, (' '.join(inF.read())).split()))
if len(a) == sum(a):
    outF.write('YES')
else:
    outF.write('NO')
inF.close()
outF.close()