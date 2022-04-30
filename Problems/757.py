inF, outF = open('input.txt', 'r'), open('output.txt', 'w')

# Start program
array = inF.read().split()
C = int(array[0])
H = int(array[1])
O = int(array[2])
result = int(min(C//2, H//6, O))
# End program

outF.write(str(result))
inF.close()
outF.close()