# Program to check whether a number is prime or not
num=int(input("Enter a number : "))
if num <= 1:
print(num," is not a Prime Number")
else:
is_prime = True
for i in range(2, num):
    if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")
