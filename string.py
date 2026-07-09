# city="shobhit"
# # print(city[-3])
# # print(city[0])

# # print(city[0:3])
# # print(city[::-1])

# # print(city[-1:0:-1])

# city.capitalize()
# print(city)
# city.strip()
# city.replace("shobhit",'singh')
# print(city)
# a="Rahul,22,bhopal,indore,2"
# p=a.split(",")
# print(" | ".join(p))
# print("hello123".isalnum())
# print("12345".isdigit())
# print("Python".upper())
# print(" ".isspace())
# print("python is good".endswith("good"))
# print("python is good".startswith("python "))
# data = "  shobhit,20,bhopal,python123  "
# data=data.strip()
# print(data.replace(","," "))
# print(data.capitalize())
# print(" | ".join(data))
# print(data.endswith())
##formating string57
name,marks,rank="anita",45.666777,100.57
# basics 
print(f"my name is ={name}")
print(f"marks:{marks:.2f}")
print(f"rank:{rank:.0f}")#round off

# padding and alignment 
print(f"{name:<15}hii| {marks:<8.2f} ")#left righ align

# #expression inside 

# price,gst=500,18
# print(f"price = {price} | Gst:Rs{price*gst:.2f}")

# name = "Shobhit"
# salary = 45678.9876
# bonus = 7890.567
# tax = 18
# print(f"name :{name}")

# print(f"slary :{salary:.2f}")
# print(f"bonus : {bonus:.1f}")
# print(f"bonus : {bonus:.0f}")
# print(f"total salary ={salary+bonus-(salary*tax/100):.0f}")

# print(f"{salary:.}")
# first_name,last_name=input("enter your name=").split(" ")
# age=int(input("enter your age="))
# first=len(first_name)
# last=len(last_name)
# ages=str(age)


# print("-"*25)
# print(f"| Name :{first_name:<17}|\n| LastName :{last_name:<12} |\n| AGE :{age :<17} |")
# print("-"*25)
# number=int(input("enter a number ="))
# even=0
# odd=0
# while number !=0 :
#     if number % 2==0 :
#         even+=1
#     else :
#         odd+=1
#     number=int(input("enter a number ="))
# print("even count =",even)
# print("odd count =",odd)

i=1
j=not not i 
print(j)

''''
Truthy : 1,2,3,-1,"a",
Falsy : 0,"",[],None,NULL
'''
list1=[10,20,30]
del list1[20]
list1.remove(20)
print(list1)