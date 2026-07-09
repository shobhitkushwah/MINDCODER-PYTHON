# def prime(count):
#     list1 = []
#     num = 2

#     while len(list1) < count:
#         is_prime = True

#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break

#         if is_prime:
#             list1.append(num)

#         num += 1

#     return list1


# # Number of rows
# a = int(input("Enter number of rows: "))

# # Total prime numbers required
# total = a * (a + 1) // 2

# # Generate required prime numbers
# list1 = prime(total)

# k = 0

# # Print the pyramid
# for i in range(1, a + 1):
#     for j in range(i):
#         print(list1[k], end=" ")
#         k += 1
#     print()

# power=1
# for exp in range(16):
#     if exp==7 :
#         continue
#     print("2 to the power of ",exp,"is",power)
#     if exp==11 :
#         break
#     power*=2
largest_number=-999999999
counter=0 
while True :
    number=int(input("enter a number or type -1 for exit :"))
    if number ==-1 :
        break
    counter+=1
    if number>largest_number:
        largest_number=number
if counter !=0 :
    print("the largest number is =",largest_number)
else :
    print("you have't enter any number")


