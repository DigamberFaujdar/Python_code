def largest_list(items):
    max=items[0]
    for i in items:
        if(max<i):
            max=i
    print("max items is : ",max)
largest_list([435,3,2,3,4,3345,5000])

#implement 2 

def largest(array):
    array.sort()
    print("largest ele is : ",array[-1])
largest([1,23,4,56,7,8])
