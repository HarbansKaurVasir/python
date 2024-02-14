'''this is a if else statement we can use as many elif as much we want '''

# light = "yellow"
# if( light == "red"):
#     print("stop")
# elif( light == "green"):
#     print("go")
# elif( light == "yellow"):
#     print("ready to go")
# else:
#     print("light is not working")

'''grade according to marks'''
    
# marks = int(input("enter student's marks :"))
# if( marks >= 90):
#     grade = "A"
# elif( marks >= 80 and marks < 90):
#     grade = "B"
# elif( marks >= 70 and marks < 80):
#     grade = "C"
# else:
#     grade = "D"
# print("GRADE :" , grade)

'''WAP to check number entered by user is odd or even '''

# number = int(input("enter any number :"))
# if( number % 2 == 0):
#     value = "even"
# else:
#     value = "odd"
# print("The number is :" , value)

'''find the greatest number of 3 numbers entered by user'''

# num1 = int(input("enter first number :"))
# num2 = int(input("enter second number :"))
# num3 = int(input("enter third number :"))

# if ( num1 > num2 and num3 ):
#     print(" greatest number is :" , num1 )
# elif( num2 > num1 and num3):
#     print(" greatest number is :" , num2 )
# else:
#     print("greates number is :" , num3)

'''chcek if number is multiple of 7 or not'''

num = int(input("enter any number :"))

num = num%7
if(num == 0):
    print("divisible by 7")
else:
    print("not divisible by 7")
