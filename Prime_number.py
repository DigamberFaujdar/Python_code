# a number that can be divided exactly only by itself and 1, for example 7, 17 and 41
def prime(num):
    count=0
    for i in range(2,num+1):
        for j in range(2,i):
            if(i%j==0):
                count+=1
        if(count==0):
            print("prime ",i)
            count=0
        else:
            count=0
prime(10)        

def prime_in_interval(start ,num):
    count=0
    for i in range(start,num+1):
        for j in range(2,i):
            if(i%j==0):
                count+=1
        if(count==0):
            print("prime ",i)
            count=0
        else:
            count=0
prime_in_interval(10,15) 


