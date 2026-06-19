#lists
numbers=[10,50,30,40,100]
# print(numbers)
# print(type(numbers))
# list1=[]


# n=int(input("enter a size ="))
# for i in range(n):
#     element=int(input("enter a element ="))
#     list1.append(element)
# print(list1)
# numbers[3]=200
# print(numbers[0])
# print(id(numbers[0]))
# print(id(numbers[1]))
print("orginial list ",numbers)
numbers[1]=numbers[4]
print("new list contents :",numbers)

del numbers[1]
print(numbers)