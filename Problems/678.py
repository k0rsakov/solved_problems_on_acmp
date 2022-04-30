inF, outF = open('input.txt', 'r'), open('output.txt', 'w')
array = ' '.join(inF.read()).split()

n = 'ABC'

for i in array:
    if i == 'A':
        n = n[1] + n[0] + n[2]
    if i == 'B':
        n = n[0] + n[2] + n[1]
    if i == 'C':
        n = n[2] + n[1] + n[0]

if n[0] == 'A':
    # print(1)
    outF.write('1')
elif n[1] == 'A':
    # print(2)
    outF.write('2')
elif n[2] == 'A':
    # print(3)
    outF.write('3')

inF.close()
outF.close()