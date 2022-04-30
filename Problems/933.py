inF, outF = open('input.txt', 'r'), open('output.txt', 'w')

# Start program
array = inF.read().split()
a = int(array[0])
b = int(array[1])
c = int(array[2])
t = int(array[3])

if t <= a:
    result = t * b
else:
    result = (t-(t-a))*b + ((t-a)*c)
# End program

outF.write(str(result))
inF.close()
outF.close()