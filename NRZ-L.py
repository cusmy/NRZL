string = input("Masukan String : ")

res = ''.join(format(ord(i), 'b') for i in string) 
ar= [None]*len(res)
dump = 0
dump_a = []

for i in range(len(res)):
   if len(res[i:i+4]) == 4:
      ar[i] = res[i:i+4]
   else:
      del ar[i:-1]
      del ar[-1]
      break
for i in ar:
    bah = int (i,2)
    


    if bah > dump or bah == dump :
        dump_a.append(1) 
    else:
        dump_a.append(0)

    dump = bah
    
s = ''.join(map(str, dump_a))
print (s)
