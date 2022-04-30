# inF, outF = open('input.txt', 'r'), open('output.txt', 'w')
#
# # Start program
# array = inF.read().split()
# k = int(array[0])
# word = array[1]
# replace_letter = word[k-1]
# index_letter = word.index(replace_letter)
# result = word[0:index_letter]+word[index_letter+1:]
# # End program
#
# outF.write(str(result))
# inF.close()
# outF.close()

inF, outF = open('input.txt', 'r'), open('output.txt', 'w')

array = inF.read().split()
s = array[1]
a = int(array[0])
ss = []
for i in s:
    for j in i:
        ss.append(j)
ss.pop(a - 1)
aa = ''
aa = aa.join(ss)
outF.write(str(aa))
