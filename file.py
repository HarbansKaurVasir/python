'''READ FILE'''
# f = open("demo.txt","r")
# data = f.read()
# print(data)
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()

'''WRITE FILE'''
# w = open("demo.txt","a") #w to remove previous and add new 
# w.write("how area your ")

# w.close()

'''deleting'''
# import os 
# os.remove("demo.txt")

'''create new file '''
# with open("practice.txt","w") as f:
#     f.write("hi everyone\nwe are learning file i/o\n")
#     f.write("using java.\nI like programming in java.")

# '''to replace data '''
# with open("practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("java","python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)

# '''to find a word '''
# word = "learning"
# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")

# def check_word():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1

# print(check_word())

'''how many even values are their in the list'''

count = 0 
with open("practice.txt","r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count +=1
print(count)