# A number is a perfect number if is equal to sum of its proper divisors, that is, sum of its positive divisors excluding the number itself. Write a function to check if a given number is perfect or not. 
# Examples: 

# Input: n = 15
# Output: false
# Divisors of 15 are 1, 3 and 5. Sum of 
# divisors is 9 which is not equal to 15.

def perfect_Number():
    num=int(input("enter a number "))
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum+=i
    if(num==sum):
        print("Number is perfect ",sum)
    else:
        print("Number is not perfect ",sum)
perfect_Number()