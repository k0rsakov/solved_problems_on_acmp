inF, outF = open('input.txt', 'r'), open('output.txt', 'w')

# Start program
array = inF.read().split()
k = int(array[0])
height_bus = 437
crash = 0

for i in range(1, k+1):
    if int(array[i]) > height_bus:
        pass
    else:
        crash = i
        break

if crash == 0:
    outF.write(f'No crash')
else:
    outF.write(f'Crash {crash}')

inF.close()
outF.close()