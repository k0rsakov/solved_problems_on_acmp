inF, outF = open('input.txt', 'r'), open('output.txt', 'w')

# Start program
array = inF.read().split()
array = list(map(int, array))
# [1 решение]
if array[0] == 1:
    outF.write(f'{array[1]} {array[1]}')
else:
    outF.write(f'{min(array[1:])} {max(array[1:])}')
# [2 решение]
# max = 0
# min = 30000
#
# if array[0] == 1:
#     outF.write(f'{array[1]} {array[1]}')
# else:
#     for i in range(1, len(array)):
#         if array[i] > max:
#             max = array[i]
#         if array[i] < min:
#             min = array[i]
#     outF.write(f'{min} {max}')
# End program

inF.close()
outF.close()