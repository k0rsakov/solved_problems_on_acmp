inF = open('input.txt','r')
outF = open('output.txt','w')
c = inF.read()
array = c.split()
a = int(array[0])
b = int(array[1])
c = int(array[2])
minimal = min(a,b,c)
maximum = max(a,b,c)
dif = maximum-minimal
print(dif,file=outF)
inF.close()
outF.close()