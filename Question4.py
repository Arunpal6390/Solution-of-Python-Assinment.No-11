#4. Write a python script to calculate sum of first N odd natural numbers
num = int(input("Print sum of odd numbers till : "))
sum = 0

for i in range(1, num + 1):

    #Check for odd or not
    if(not (i%2) == 0):
        sum += i

print("\nSum of odd numbers from 1 to", num, "is :", sum)