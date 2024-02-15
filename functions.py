'''FUNCTIONS'''
'''average function'''
def average(a,b,c):
    sum = a+b+c
    avg = sum / 3
    print(avg)
    return avg

# average(1,1,1)

'''convert usd in inr function'''
def converter(usd_value):
    inr_value = usd_value*83
    print(usd_value,"usd = ", inr_value ,"inr")

# converter(4)

'''find even and odd function'''
n = int(input("enter any number :"))
def even_odd(n):
    if( n%2 == 0):
        print("even number")
    elif(n%2 != 0):
        print("odd number")
    
# even_odd(n)

'''RECURSION'''
'''print number in recursion'''
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

# show(6)
    
'''factorial recursion sum'''
def fact(n):
    if ( n == 0 or n == 1 ):
        return 1
    else:
        return n * fact(n-1)
    
# print(fact(5))

'''sum of first 5 num in recursion'''
def sum_nums(n):
    if(n == 0):
        return 0
    else:
        return sum_nums(n-1) + n

# print(sum_nums(5))

'''WAF to print all elements in list in recursion'''
def print_list(list,index=0):
    if( index == len(list)):
        return
    print(list[index])
    print_list(list,index+1)

list = [1,2,2,2,2,2,3,3,4,5667,6]

# print_list(list)