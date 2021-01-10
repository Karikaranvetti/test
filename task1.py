# Enter your code here. Read input from STDIN. Print output to STDOUT
    # Enter your code here. Read input from STDIN. Print output to STDOUT
   
        
def isprime(num):
     
    if num==2:
        return True
    for i in range(2, num):
    
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
        if (num % i) == 0:
            return False
    return True


 print(isfeb(1))
print(isprime(1))
dupl = set()
de={}
x= list( map( int, input().split()))
    # 
    # x = val.split()
for num in x :
        
    if isfeb(num):
            
        if isprime(num):
                # print(num)
            if x.count(num) >= 1:
                dupl.add(num)
                de[num]=x.count(num)
            # print(num,x.count(num))
for nn in dupl:
    print(nn,de[nn] )           
        
def isfeb(n):
     
    c=0
    a=1
    b=1
    if n==0 or n==1:
        return True
     
    else:
        while c<n:
            c=a+b
            b=a
            a=c
        if c==n:
            return True
        else:
            return False

