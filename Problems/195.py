inF = open('input.txt','r')
outF = open('output.txt','w')
c = inF.read()
array = c.split()
a = int(array[0])
b = int(array[1])
k = int(array[2])
p = a*b*k*2
outF.write(str(p))
