def even_generator(nums):
    for i in range(2, nums + 1, 2): 
       # return i # this will return and stop the function to continue 
        yield i # this yield will remain the state of the function in the memory and also generate a value 
    
for num in even_generator(10):
    print(num)
