# i = 1
# while i <= 5:
#     print("hello", i)
#     i+=1

'''print number from i to 100'''
# i = 1 
# while i <= 100:
#     print(i)
#     i+=1

'''print numbers from 100 - 1'''
# i = 100
# while i > 0:
#     print(i)
#     i-=1

'''print table by input from user'''
# n = int(input("enter number to print its table :"))
# i = 1
# while i <= 10:
#     print(i*n)
#     i+=1

'''print the elements of the follownig list in loop'''
# list = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(list):
#     print(list[i])
#     i+=1

'''search for a number x in this tuple using loop '''
# x = int(input("enter number to search :"))
# tuple = (1,4,9,16,25,36,49,64,81,100)
# i = 0 
# while i < len(tuple):
#     if (tuple[i] == x):
#         print("number index is :",  i )
#         break
#     i+=1

'''print 1 - 6 skin 3 '''

# i = 1 
# while i<=6:
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1
'''sum of first n numbers '''
# n = 7 
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
    
# print("sum is :", sum)

''' FOR LOOPS'''
'''PRINTH THE FOLLOWING USING LOOPS '''
# list = [1,4,9,16,23,48,97,100]

# for values in list:
#     print(values)

'''SEARCH FOR A LOOP IN THE TUPLE '''
# tuple = (1,4,9,16,23,48,97,100)
# x = 16
# i = 0
# for items in tuple:
#     if(items == x):   
#         print(x," is at index",i)
#         break
#     i+=1

'''PRINT NUMBERS FROM 1 - 100'''
# for i in range(101):
#     print(i)

'''PRINT NUMBERS FROM 100 - 1'''
# for i in range(100,0,-1):
#     print(i)
   
'''PRINT THE MULTIPLICATION NUMBER OF N '''
# for i in range(1,11):
#     print(i*2)

'''FACTORIAL OF FIRST N NUMBERS'''
fact = 1 
for i in range(1,6):
    fact *= i
    
print("fact is :" , fact)