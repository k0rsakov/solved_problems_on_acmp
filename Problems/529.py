inF, outF = open('input.txt', 'r'), open('output.txt', 'w')

# Start program
array = inF.read().split()
x1 = int(array[0])
y1 = int(array[1])
x2 = int(array[2])
y2 = int(array[3])

y = y2 - y1
x = x2 - x1

z = y**2 + x**2
result = pow(z,0.5)
# End program

outF.write(str(result))
inF.close()
outF.close()