inF, outF = open('input.txt', 'r'), open('output.txt', 'w')
a = list(map(int, inF.read().split()))

x = a[0]
y = a[1]
d = 0
def gcd_rem_division(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2

# for i in range(1, (max(x, y)+1)):
#     if x % i == 0 and y % i == 0:
#         d = i

outF.write(str(gcd_rem_division(x,y)))
inF.close()
outF.close()