inF, outF = open('input.txt', 'r'), open('output.txt', 'w')

# Start program
array = inF.read()

if (int(array[0]) % 10 == int(array[3]) % 10000
        and int(array[1]) % 100 == int(array[2]) % 1000):
    outF.write('YES')
else:
    outF.write('NO')

inF.close()
outF.close()

# Second var

# inF, outF = open('input.txt', 'r'), open('output.txt', 'w')
#
# # Start program
# array = inF.read()
#
# if array == array[::-1]:
#     outF.write(str('YES'))
# else:
#     outF.write(str('NO'))
# # End program
#
# inF.close()
# outF.close()