num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is a even number")
else:
    print(f"{num} is a odd number")


# even no
for i in range(2,10,2):
    print(i,end=",")

# odd no 
for i in range(1,10,2):
    print(i,end=",")

# list 
my_list = [0,1,2,3,4,5]
for item in my_list:
    print(my_list)