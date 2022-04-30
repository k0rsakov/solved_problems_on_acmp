
inF, outF = open('input.txt', 'r'), open('output.txt', 'w')

array = inF.read().split()
time = array[0].split(':')

print(array, time)

hours = int(array[1]) + int(time[0])
minutes = int(array[2]) + int(time[1])

minutes_hours = hours * 60

all_time = minutes_hours+minutes

result_hour = all_time // 60 % 24
result_minutes = all_time % 60

if result_hour // 10 == 0:
    outF.write(f'0{result_hour}:')
else:
    outF.write(f'{result_hour}:')

if result_minutes // 10 == 0:
    outF.write(f'0{result_minutes}')
else:
    outF.write(f'{result_minutes}')

inF.close()
outF.close()