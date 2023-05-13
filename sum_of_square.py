#Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2. 

def sum_square(num):
    sum=0
    for i in range(1,num+1):
        sum+=i**3
    
    print("sum of square of first N number :",sum)
    return sum
#sum_square(5)
print(sum_square(7))
