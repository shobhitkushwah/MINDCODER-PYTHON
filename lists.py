list1=[]
# n=int(input("enter a numbers="))
# for i in range(n):
#     if i %2==0 :
#          list1.append(i)

# print("lenght of list =",len(list1))
# print(f"content of list {list1}")
# list1.insert(2,10)
# print(list1)
# for i in range(len(list1)) :
#      print(list1[i])
# list1=[]
# for i in range(1,11):
#     list1.insert(i,i)
# print(list1)
# print(list1[0],list1[1])
# for i in range(1,11):
#     list1.append(i)
# tup1=(10,20,30)
# tup1=list(tup1)
# print(type(tup1))
# list1=[]
# for i in range(1,11):
#     list1+=[i]
# print(list1)

# list1.append(1)
# print(list1)
# bubble sort 
# list1=[]
# n=int(input("enter the size of list1="))
# for i in range(n):
#     element=int(input(f"enter the element {i+1}="))
#     list1.append(element)
# # k=len(list1)-1
# count=0
# for i in range(0,len(list1)-1):

#     for j in range(0,len(list1)-1):
#               count+=1
#               if list1[j]>list1[j+1]:
#                     temp=list1[j]
#                     list1[j]=list1[j+1]
#                     list1[j+1]=temp 

# print(list1)   
# print(count)
# list1=["d","A","a"]
# list1.sort()
# print(list1)
# print("a">="a")
# a=input("enter a")
# a=1
# b=1 
# c=2
# lst=[a,c,b]
# lst.sort()
# print()
# reversing the string 
# a="A"
# b="B"
# c="C"
# d=" "
# lst=[a,b,c,d]
# lst.reverse()
# # print(lst)
# lst=[1]
# lst2=lst.copy()
# lst[0]=2
# print(lst2)
# a=1
# b=a 
# a=2 
# print(a)
# print(b)

#slicing 
# list1=[1,2,3,40]
# list2=list1[:]
# list1[0]=2
# print(list2)

# list1=[10,4,3,2,8,5]
# print(list1)
# print(list1[1:-1])
# print(list1[-1:1])
# print(list1[::-1])
# print(ord("A"))
# print(ord("b"))

lst=[10,8,6,4,2]

# print(10 in lst)

# print(5 not in lst)
# print(max(lst))
# maximum=lst[0]
# for i in lst :
#     if i > maximum :
#         maximum =i 
# print ("max=",maximum)
# lst=[]
# for i in range(1,31):
#     if i % 2==0 :
#         lst.append(i)
# print(lst)
# lst= [i for i in range (0,31,2)]
# print(lst)
# maximum=lst[0]
# for index in range(1,len(lst)):
#     if maximum < lst[index]:
#         maximum=lst[index]
# print(maximum)
# list1=[10,20,30,40,5,20,3013,1000]
# elment=5 
# a=0
# for i in list1:
#     if i == elment :
#         print("index=",a)
#         break
#     a+=1
# a=10
# b=20 
# print(a>b and b >a)
# print(a>b and b <a)
# print(not(a<b and a==10))
# my_list=[10,20,30,40,50]
# for i in range(len(my_list)):
#     my_list[i]=my_list[i]+1


# print(my_list)

# import numpy as np 
# list1=np.arange(1,10)

# print(list1)

# list1=[10,20,30,40,50,60,70,80,90,100]
# sum=0 
# for i in list1:
#     sum+=i
# print(f"sum={sum}")
# index=0
# for abc in list1 :
#     print(f"list1[{index}]=>{abc}")
#     index+=1

# a=10
# b=20
# a=a+b
# b=a-b
# a=a-b 
# print("a=>",a)
# print("b=>",b)
# my_list=[10,20,30,40,50,60,70,80,90,100,110]
# # swapping 
# my_list[1],my_list[5]=my_list[5],my_list[1]
# my_list[1]=my_list[1]+my_list[5]
# my_list[5]=my_list[1]-my_list[5]
# my_list[1]=my_list[1]-my_list[5]
# print(my_list)
list1=[2,4,6,8,10]


# count=0
# if sorted(list1)==list1 :
#     print("yes list is sorted:")
# else :
#     print("no")
#     for index in range(len(list1)-1):
#         for index_inner in range(len(list1)-index-1):
#             if list1[index_inner]>list1[index_inner+1]:
#                 list1[index_inner],list1[index_inner+1]=list1[index_inner+1],list1[index_inner]
#             count+=1
#     print(list1)

#     print(count)
# if [" "] :
#     print("yes")
# else :
#     print("no")
list1=[1,5,3,9]
# print(sorted(list1))

# list1.sort()
# print(list1)

# list1.reverse()
# print(list1)

# list1=["b","a","c","d"]
# list1.sort()
# print(list1)

# list1=[10,20,30,40,50,60]
# print(list1[-1:-4:-2])
# text = "python programming"

# if "p"  in text:
#     print("Java is not present")
#     print(text.count("p"))
# else:
#     print("Java is present")
# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a

# print(a == b)
# print(a is b)
# print(a is c)

list1=[10,20,40,5,1000,90]
# maxs=list1[0]
# for i in list1 :
#     if i > maxs :
#         maxs=i 
# print("max=",maxs)
# flag=0 
# n=int(input("enter a searching a no ="))
# for i in list1:
#     if i==n :
#         flag+=1
#         print(f"element found at index {flag}")
#         break 
#     else :
#         flag+=1

# remove duplicates in list 
# list1=[10,10,20,30,20,30,40,50,60,50,60]
# list2=[]
# for i in range(len(list1)):
#     if i not in list2 :
#         list2.append(i)
# for j in range(len(list2)):
#     list1[j]=list2[j]

# del list1[len(list2):]
# print(list1)

# list compremation 
# list1=[2**x  for x in range(8) ]
# print(list1)

# odds =[x for x in list1 if x %2!=0]

# print(odds)

# evens=[x for x in list1 if x % 2==0]
# print("evens=",evens)
# print("odds=",odds)

# boards=[]
# for i in range(8):
#     row=["empty !" for i in range(8)]
#     boards.append(row)
# print(boards)

# boards=[["empty !"for i in range(8)] ]
# print(boards)
print("checking branch changes")