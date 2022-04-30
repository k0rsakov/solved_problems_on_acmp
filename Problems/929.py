inF, outF = open('input.txt', 'r'), open('output.txt', 'w')
a = list(map(int, inF.read().split()))
n = a[0]
max = n * 6
min = n // 6
n %= 6
if n > 0:
    min += 7 - n
outF.write(f'{min} {max}')
inF.close()
outF.close()