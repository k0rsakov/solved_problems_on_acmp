inF = open('input.txt','r')
outF = open('output.txt','w')
c = inF.read()
array = c.split()
n = int(array[0])
m = int(array[1])
k = int(array[2])
s=n*m
if s>=k:
    outF.write("YES")
else:
    outF.write("NO")
inF.close()
outF.close()



