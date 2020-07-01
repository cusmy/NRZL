import numpy as np
string = input('masukan String : ')

res = ''.join(format(ord(i), 'b') for i in string)
dump = 0
dump_a = []
mantap = str(res)
split_strings = []
n  = 4
for index in range(0, len(mantap), n):
    split_strings.append(mantap[index : index + n])
mantap = np.array(split_strings)
for i in mantap:
    bah = int (i,2)
    


    if bah > dump or bah == dump :
        dump_a.append(1) 
    else:
        dump_a.append(0)

    dump = bah
    
s = ''.join(map(str, dump_a))
print ('Hasil NRZ-L adalah : ' +s)
