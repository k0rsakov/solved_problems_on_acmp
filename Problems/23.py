inF, outF = open('input.txt', 'r'), open('output.txt', 'w')

# Start program
array = inF.read().split()
n = int(array[0])
counter = 0
for i in range(1, n+1):
    if n % i == 0:
        counter += i
# End program

outF.write(str(counter))
inF.close()
outF.close()