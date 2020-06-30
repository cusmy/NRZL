cuk = "HELLO WOLRD"
  
# print("String :" + (cuk)) 

res = ''.join(format(ord(i), 'b') for i in cuk) 
er = (res[0:4])
et = (res[7])
ey = (res [11:14])
eu = (res [22:26])
eo = (res [38:42])
ep = (res [56:60])
ew = (res [61:65])
eq = (res [-11 : -7])
T = er + et + ey + eu + eo + ep + ew + eq
print(len(res))
print("Conversi Ke NRZ-L: " +(T))