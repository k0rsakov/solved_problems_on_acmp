inF = open('input.txt','r')
outF = open('output.txt','w')
c = inF.read()
array = c.split()
i=0
z=0
while i<8:
    z+=int(array[i])
    i+=2
j=1
y=0
while j<8:
    y+=int(array[j])
    j+=2
if z>y:
    outF.write("1")
else:
    if y>z:
     outF.write("2")
if z==y:
    outF.write("DRAW")
inF.close()
outF.close()