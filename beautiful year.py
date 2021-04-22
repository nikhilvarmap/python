x  = int(input())
if x>=1987 and x<2013:
    x = x+ 26
else:
    x = x+1
z = x
s = []
u = []

for i in range(len(str(x))):
    while z>0:
        t = z%10
        z = z//10
        for i in range(len(str(z))):
            y = str(z)
            y = list(y)
            for q in y:
                q = int(q)
                u.append(q)
            for w in range(10):
                if t in u:
                    t = w
            s.append(t)
            del u[:]
s = s[::-1]
print(s)
s = ''.join(s)
s = int(s)
            
        
    

                        

        
print(s)
            
    
    
