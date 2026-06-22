list1=[]
n=int(input("enter a numbers="))
for i in range(n):
    if i %2==0 :
         list1.append(i)

print("lenght of list =",len(list1))
print(f"content of list {list1}")
list1.insert(2,10)
print(list1)