inF, outF = open('input.txt', 'r'), open('output.txt', 'w')

# Start program
array = inF.read().split()
t_room = int(array[0])
t_cond = int(array[1])
func = array[2]

if func == 'fan':
    outF.write(str(t_room))
elif func == 'auto':
    outF.write(str(t_cond))
elif func == 'freeze':
    if t_room == t_cond:
        outF.write(str(t_room))
    elif t_room >= t_cond:
        outF.write(str(t_cond))
    elif t_room <= t_cond:
        outF.write(str(t_room))
elif func == 'heat':
    if t_room == t_cond:
        outF.write(str(t_room))
    elif t_room >= t_cond:
        outF.write(str(t_room))
    elif t_room <= t_cond:
        outF.write(str(t_cond))
# End program

# outF.write(str(result))
inF.close()
outF.close()