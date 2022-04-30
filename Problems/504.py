inF, outF = open('input.txt', 'r'), open('output.txt', 'w')
# Start program
array = inF.read().split()
k = int(array[0])
start = 'GCV'
for i in range(k):
    start = start[0] + start[2] + start[1]
    start = start[1] + start[0] + start[2]
# End program
outF.write(str(start))
inF.close()
outF.close()