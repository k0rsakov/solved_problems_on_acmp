inF = open('input.txt','r')
outF = open('output.txt','w')
c = inF.read()
array = c.split()
a = int(array[0])
b = int(array[1])
s = a+b-1
g = s -a
l = s - b
#outF.writelines(str(g))
#outF.writelines(str(l))
print(g,file=outF)
print(l,file=outF)
inF.close()
outF.close()