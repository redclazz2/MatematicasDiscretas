a,b,max,check = 0,1,50,True 
for n in range(0,50):
    if(check):
        print(a); print(b); check = False
    c = a + b; a = b; b = c; print(c)

