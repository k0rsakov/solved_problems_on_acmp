# Чтобы треугольник существовал, сумма двух сторон треугольника всегда должна быть больше третей стороны.
# a + b > c, b + c > a, a + c > b.

inF, outF = open('input.txt', 'r'), open('output.txt', 'w')

# Start program
array = inF.read().split()
a = int(array[0])
b = int(array[1])
c = int(array[2])
if a + b > c and b + c > a and a + c > b:
    outF.write('YES')
else:
    outF.write('NO')
# End program

inF.close()
outF.close()