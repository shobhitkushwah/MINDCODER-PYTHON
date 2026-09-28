# x=10
# def s(n):
#     print("n=",n)
#     x=20
# a=int(input("enter the vlaue of a ="))
# print(s(a))
# print(x)
# var=2
# def multiple(n):
#     return var*n 
# a=int(input("enter a no ="))
# print(multiple(a))


# def multiple(n):
#     var=int(input("enter the value of var="))
#     return var*n 
# a=int(input("enter a no ="))
# print(multiple(a))

# global variable in python 

# def my_function():
#     global var 
#     var+=1
#     print("hello var =",var)
# var=2
# my_function()
# var=2 
# def return_var():
#     global var 
#     var+=5
#     return var
# print(return_var())

# def My_function(n):
#     print('i got =',n)
#     n+=1 
#     print('i have ',n)
#     global var 
#     var=n
# var=1 
# My_function(var)
# print(var)


# def my_function(list2):
#     global list1
#     for i in range(len(list1)) :
#         list1[i]+=1


# list1=[10,20,30,40]
# my_function(list1)
# print(list1)


# def my_function(my_list1):
#     print("print#1=",my_list1)
#     del my_list1[0]
#     print(my_list1)
# my_list2=[2,3]
# my_function(my_list2)
# print(my_list2)

# def my_function(n):
#     del n 
# a=10 
# my_function(a)
# print(a)

# dictonariess 
# dict1={ }
# n=int(input("enter the size of dict ="))
# for i in range(n):
#     a=input(f"enter the value {i+1}=")
#     dict1[i]=a
 
# # print("dict1=",dict1)
# # print("dict1 type =",type(dict1))

# print(type(dict1.values()))
# milan="milans"
# dict1={
#     "shobhit":20,
#     "singh":30,
#     milan:40
# }
# print(dict1)

# print(dict1[20])
dict1={
    "cat":"thar",
    "dog":"baleno",
    "elephant":"bullet"
}

# keys=["cat","dog","elephant"]
# for key in keys:
#     if key in dict1 :
#         print(key,"->",dict[key])
#     else :
#         print(key,"is not in dictionary ") 

dict1={

    "shobhit":20,
    "koushal":21,
    "singh":22,
    "kushwah":25
}
# a=True 
# while True  :
#     key=input("enter the searching key =")
#     if key in dict1 :
#         print(key,f"found -> {dict1[key]}")  
#     else :
#         print(key,"not found ") 
#     a=input("True or False ")
#     if a==False :
#         break 
# for key in dict1.keys():
#     if key in dict1:
#         print(key,"->",dict1[key])
#     else :
#         print(key,"not found")
for keys,values in dict1.items():
    print(f"keys={keys} and values={values}")

for values in dict1.values():
    print(f"values ->{values}")

a=dict1
# print(id(dict1))
# print(id(a))
a["tk"]=40
print(dict1)


del dict1["tk"]
print(dict1)