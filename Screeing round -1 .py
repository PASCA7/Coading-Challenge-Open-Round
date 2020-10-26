tc=int(input())

a = [] 
for i in range(tc): 
    b=[]
    for j in range(1):
        b=input().split()
    a.append(b)    
    


            
 
for i in range(len(a)):
    for j in range(3):
        if j == 0:
            p=int(a[i][j])   
        elif j== 1:
            n=int(a[i][j])
        elif j==2:
            d=int(a[i][j])
    total=p+(d-1)*n  
    print(total)      
    