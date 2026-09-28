# # # # file handling in python 
# # # f=open("sample.txt","w")
# # # user_name=input("Enter your user_name=")
# # # age= input("Enter your age=")
# # # f.write(user_name+"\n")
# # # f.write(age)
# # # f.close()

# # # f=open("sample.txt","r")
# # # l=f.readline()
# # # while l !="":
# # #     print(l,end=" ")
# # #     l=f.readline()
# # # f.close()
# # name1=input("Enter your name1=")
# # name2=input("Enter your name2=")
# # name3=input("Enter your name3=")
# # name4=input("Enter your name4=")
# # name5=input("Enter your name5=")
# # f=open("sample.txt","w")
# # f.writelines([
# #     name1 + "\n",
# #     name2 + "\n",
# #     name3 + "\n",
# #     name4 + "\n",
# #     name5 + "\n"
# # ])
# # f.close()

# # f=open("sample.txt","r")

# # l=f.readline()
# # while l !="":
# #     print(l,end=" ")
# #     l=f.readline()

# # f.close()

# # f=open("sample.txt","a")
# # name6=input("Enter your name6=")
# # f.write("\n"+name6)


# # f=open("sample.txt","r")

# # l=f.readline()
# # while l !="":
# #     print(l,end=" ")
# #     l=f.readline()

# # f = open("sample.txt", "r")

# # data = f.read()

# # total_lines = len(data.splitlines())
# # total_words = len(data.split())

# # print("Total lines =", total_lines)
# # print("Total words =", total_words)

# # f.close()

# list1=[]
# n=int(input("enter the no of students="))
# for i in range(1,n+1):
#     list2=[]
#     Name=input(f"enter the name of student {i}=")
#     Roll_no=input(f"enter the roll_no of studnet {i}=")
#     Marks=input(f"Enter the Marks of students {i}=")
#     list2.append(Name)
#     list2.append(Roll_no)
#     list2.append(Marks)
#     list1.append(list2)

# f=open("sample.txt","a")
# for i in range(n):
#      f.write(", ".join(list1[i]) + "\n")

# f.close()

# f=open("sample.txt","r")
# print(f.read())
# f.close()
# a=input("Enter the searching words=").lower()
# f=open(r"C:\Users\shobh\Downloads\radha.txt","r")
# c=0
# l=f.readline()
# while l!="":
#      if a in l .lower():
#           c+=1 
#           print(l)
#      l=f.readline()
# print("total count=",c)
# f.close()
# a=input("Enter the replacing word=").lower()
# b=input("Enter the replaced word=").lower()
# f=open(r"C:\Users\shobh\Downloads\krishna.txt","r")
# data=f.read().lower()
# data=data.replace(a,b)
# f.close()

# f=open(r"C:\Users\shobh\Downloads\krishna.txt","w")
# f.write(data)
# f.close()

# f=open(r"C:\Users\shobh\Downloads\krishna.txt","r")
# print(f.read())
# f.close()

# f=open(r"C:\Users\shobh\Downloads\radhakrishna.txt","w")
# f.write('''Python is a popular programming language.
# File handling allows us to store data permanently.
# We can read data from a file.
# We can write data into a file.
# Python provides read(), readline(), and readlines().
# We can also use write() and writelines().
# Append mode adds new content without deleting old data.
# File handling is an important topic in Python.jay shree krishna''')

# f.close()
# f=open(r"C:\Users\shobh\Downloads\radhakrishna.txt","r")
# print("First line=",f.readline())
# print(f.read())

# f.close()

# f=open(r"C:\Users\shobh\Downloads\radhakrishna.txt","a")
# string=input("Enter the string =")
# f.write(string)

# f.close()

# f=open(r"C:\Users\shobh\Downloads\radhakrishna.txt","r")
# data=f.read()
# lenght=len(data.splitlines())
# print(lenght)
# f.close()
# a=input("Enter the searching a word=")
# f=open(r"C:\Users\shobh\Downloads\radhakrishna.txt","r")
# c=0
# l=f.readline()
# while l!="":
#     if a in l :
#         c+=1
#     l=f.readline()
# print(c)
# f.close()


# file2=open(r"C:\Users\shobh\Downloads\radha.txt","r")
# data1=file2.read()
# file2.close()

# file1=open(r"C:\Users\shobh\Downloads\krishna.txt","r")
# data2=file1.read()
# file1.close()

# if data1==data2:
#     print("data are same ")
# else :
     
#     data1=data2 
# file1=open(r"C:\Users\shobh\Downloads\krishna.txt","w")
# file1.write(data1)
# file1.close()

# with open(r"C:\Users\shobh\Downloads\data.txt","r") as f :
#     data=f.read()
#     total_lines=len(data.splitlines())
#     total_words=len(data.split())
#     total_char=len(data)
#     print("total_lines=",total_lines)
#     print("total_words=",total_words)
#     print("total_char=",total_char)

# with open(r"C:\Users\shobh\Downloads\data.txt", "r") as f:

#     l = f.readline()

#     max_line = len(l)
#     max_lines = l

#     while l != "":

#         if max_line < len(l):
#             max_line = len(l)
#             max_lines = l

#         l = f.readline()

# print(max_lines)
# print(max_line)
