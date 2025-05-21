def sum_all(*args):
    print(args) # this will return a tuple 
    print(*args) # this will return each elements passed as a arguement
    # for i in args:
    #     sum+=i
    return sum(args)

print(sum_all(2,3))
print(sum_all(2,3,4,5,6))