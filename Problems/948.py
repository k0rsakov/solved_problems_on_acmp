inF, outF = open('input.txt', 'r'), open('output.txt', 'w')

array = inF.read().split()
k = int(array[0])
n = int(array[1])

page_counter = 1
page_size = k

if k - n < 0:
    if n % k > 0:
        page_counter = n // k + 1
    else:
        page_counter = n // k

string_counter = n - page_size * (page_counter-1)

outF.write(str(page_counter)+' '+str(string_counter))