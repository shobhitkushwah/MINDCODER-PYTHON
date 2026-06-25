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
list1=[]
n=int(input("enter the size of list1="))
for i in range(n):
    element=int(input(f"enter the element {i+1}="))
    list1.append(element)
k=list1[0]
for i in range(0,len(list1)-1):
    for j in range(0,len(list1)-1):
              if list1[j]>list1[j+1]:
                    temp=list1[j]
                    list1[j]=list1[j+1]
                    list1[j+1]=temp 
print(list1)
            