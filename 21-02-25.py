# 1.Print numbers from 1 to 100 using for loop
for i in range(1,101):
    print(i)

# 2.write a program to print the sum of the first  n  natural  
n = int(input("Enter a positive number: "))
sum_n = (n * (n + 1)) // 2
print(f"The sum of the first {n} natural numbers is: {sum_n}")

#7.write a program that keeps asking the user to enter numbers 
# until they enter a negative number. Use a  while  loop. 

while True:
    positive_integer=int(input("enter non negative number : "))
    if  positive_integer<0:
        break

#  1. Print the first 10 terms of the Fibonacci series using a  for loop

input=int(input("enter the range : "))
first=0
second=1
for i in range(input):
    print(first)
    temp=first+second
    first=second
    second=temp

# 2.check if a given number is a prime number using a  for loop.

prime_input=int(input("enter number : "))
if prime_input>1:
    for i in range(2,(prime_input//2)+1):
        if prime_input % i == 0:
            print("Not a prime")
            break
    else:
        print("Prime Number")
            
else:
    print("Not a prime")

# 6. implement a basic login system where the user has three 
# attempts to enter the correct password using a loop.
attempts=3
username="xyz"
password="123"   

while attempts >= 1:
    username_input=input("enter username")
    user_password=input("enter password")

    if username_input=="xyz" and user_password=="123":
        print("login successful")
        break
    else:
        attempts-=1
        print(f"you have {attempts} left")
        if attempts==0:
            print("attempts exceeded,try again later")

# 5. implement a menu-driven program where the user can choose to: 
# 1.  Find the square of a number. 
# 2.  Find the cube of a number. 
# 3.  Exit.

while True:
    user_input=int(input("choose your option 1 or 2 and 3 to exit:"))
    if  user_input==1:
        square_input=int(input("Enter a number :"))
        print(square_input*square_input)
    elif  user_input==2:
        cube_input=int(input("Enter a number :"))
        print(cube_input**3)
    elif user_input==3:
        print("byee")
        break
    else:
        print("enter 1 or 2 or 3")                   