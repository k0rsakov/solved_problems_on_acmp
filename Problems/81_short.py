o = open('output.txt', 'w')
a = list(map(int, open('input.txt', 'r').read().split()))
if a[0] == 1:
    o.write(f'{a[1]} {a[1]}')
else:
    o.write(f'{min(a[1:])} {max(a[1:])}')