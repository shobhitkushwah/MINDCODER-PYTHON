# #lists
# numbers=[10,50,30,40,100]
# # print(numbers)
# # print(type(numbers))
# # list1=[]


# # n=int(input("enter a size ="))
# # for i in range(n):
# #     element=int(input("enter a element ="))
# #     list1.append(element)
# # print(list1)
# # numbers[3]=200
# # print(numbers[0])
# # print(id(numbers[0]))
# # print(id(numbers[1]))
# print("orginial list ",numbers)
# numbers[1]=numbers[4]
# print("new list contents :",numbers)
# print(len(numbers))
# del numbers[1]
# print(numbers)
# print(len(numbers))
# print(numbers[-1])
# print(numbers[-4:-1])

# # for printing the last with the help of minus element dynamically 
# print(numbers[len(numbers)*-1])
list1=[]
n=int(input("enter the size of list ="))
for i in range(n):
    element=int(input("ener the element ="))
    list1.append(element)

print("length of list =",len(list1))
del list1[len(list1)-1]
n=int(input("enter a middle number ="))
k=len(list1)//2
list1[k]=n 
print("final list=",list1)
