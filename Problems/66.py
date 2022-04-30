inF, outF = open('input.txt', 'r'), open('output.txt', 'w')

# Start program
keyboard = 'qwertyuiopasdfghjklzxcvbnm'
letter = inF.read()
# key = keyboard.find(letter)
# key += 1
# if key == len(keyboard):
#     outF.write(keyboard[0])
# else:
#     outF.write(keyboard[key])
# End program

# for i in range(len(keyboard)):
#     if keyboard[i] == letter:
#         if keyboard[i] == 'm':
#             # outF.write(keyboard[0])
#             outF.write(str(keyboard[0]))
#         else:
#             outF.write(str(keyboard[i+1]))
#             # print(keyboard[i+1])

# index = 0
# for i in range(len(keyboard)):
#     if keyboard[i] == letter:
#         index = i
#         index += 1
#         outF.write(str(keyboard[index]))
letter = input()
keyboard = 'qwertyuiopasdfghjklzxcvbnm'
if letter == 'm':
    #outF.write(str(keyboard[0]))
    print(keyboard[0])
else:
    key = keyboard.find(letter)
    key += 1
    #outF.write(str(keyboard[key]))
    print(keyboard[key])

inF.close()
outF.close()

letter = input()
keyboard = 'qwertyuiopasdfghjklzxcvbnm'
key = keyboard.find(letter)
key += 1
if key == len(keyboard):
    print(keyboard[0])
else:
    print(keyboard[key])
