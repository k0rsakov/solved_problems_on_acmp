inF, outF = open('input.txt', 'r'), open('output.txt', 'w')
array = ' '.join(inF.read()).split()

def alphabet_position(text):
    nums = [str(ord(x) - 96) for x in text.lower() if x >= 'a' and x <= 'z']
    return " ".join(nums)

number = int(alphabet_position(array[0])) + int(array[1])

if number % 2 == 0:
    # print('BLACK')
    outF.write('BLACK')
else:
    # print('WHITE')
    outF.write('WHITE')

inF.close()
outF.close()