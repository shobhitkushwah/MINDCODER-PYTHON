# binary serch algorithm
# def binary_search(list1,k):
#     left=0 
#     right=len(list1)-1
#     while left <= right :
#         mid=(left+right)//2
#         if list1[mid]==k :
#             return mid 
#         elif list1[mid]>k :
#             left=mid+1 
#         else :
#             right=mid-1
#     return -1 
# a=int(input("enter the size fo array ="))
# list1=[]
# for i in range(a):
#     k=int(input(f"enter the element {i+1}="))
#     list1.append(k)

# list1.sort()
# k=int(input("enter the searching element ="))
# print(binary_search(list1,k))
# lamda function use 


# double =lambda x,y : x %2==0 


# print(double(4,2))


a=float(input("enter a no ="))
print(a)
print(dir(complex))
a="python"
print(a[6:1:-1])



print(a.find("t"))
print(a.index("t"))
print(a.isascii())
a+="s"
print(a)

a=tuple(1,2,3,4)
a+=20
print(a)

