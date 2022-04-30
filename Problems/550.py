inF, outF = open('input.txt', 'r'), open('output.txt', 'w')

# Start program
array = inF.read().split()
year = int(array[0])

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    outF.write('12/09/')
else:
    outF.write('13/09/')
year = str(year)
if len(year) == 4:
    outF.write(year)
elif len(year) == 3:
    outF.write('0' + year)
elif len(year) == 2:
    outF.write('00' + year)
elif len(year) == 1:
    outF.write('000' + year)
# End program

#outF.write(str(counter))
inF.close()
outF.close()


#
# int year;
#     cin>>year;
#         if ((year%400==0) || (year%4==0 && year%100!=0))
#                 cout<<"12/09/";
#         else
#             cout<<"13/09/";
#                  year<10?cout<<"000":year<100?cout<<"00":year<1000?cout<<"0":cout<<"";
#             cout<<year;
#     return 0;