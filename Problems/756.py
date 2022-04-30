inF = open('input.txt','r')
outF = open('output.txt','w')
c = inF.read()

# Start program
array = c.split()
a = int(array[0])
b = int(array[1])
p = (a-1)*(b-1)
# End program

outF.write(str(p))
inF.close()
outF.close()