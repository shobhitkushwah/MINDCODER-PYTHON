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

#expression inside 

price,gst=500,18
print(f"price = {price} | Gst:Rs{price*gst:.2f}")