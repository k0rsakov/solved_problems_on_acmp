inF = open('input.txt','r')
outF = open('output.txt','w')
c = inF.read()
array = c.split()
a = int(array[0])
b = int(array[1])
c=a+b
outF.write(str(c))
inF.close()
outF.close()
