inF, outF = open('input.txt', 'r'), open('output.txt', 'w')

# Start program
array = inF.read().split()
s = int(array[0])
t = int(array[1])

if s > t:
    result = 12 - s + t
else:
    result = t - s
# End program

outF.write(str(result))
inF.close()
outF.close()