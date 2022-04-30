inF, outF = open('input.txt', 'r'), open('output.txt', 'w')

# Start program
array = inF.read().split()
l = int(array[0])
w = int(array[1])
h = int(array[2])
result = (((l+l) * h) + ((w+w) * h))
if result % 16 == 0:
    outF.write(str(result // 16))
else:
    outF.write(str((((l + l) * h) + ((w + w) * h)) // 16 + 1))
# End program
inF.close()
outF.close()



# L, W, H = list(map(int, input().split()))
# if (2*H*L + 2*H*W) % 16 == 0:
#     print((2*H*L + 2*H*W)//16)
# else:
#     print((2*H*L + 2*H*W)//16 + 1)
