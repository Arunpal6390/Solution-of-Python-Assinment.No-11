#5. Write a python script to calculate sum of first N even natural numbers
# Take input from user.
num = int(input("Print sum of even numbers till : "))
sum = 0

for i in range(2, num + 1):

    #Check for eveen or not
    if i%2 == 0:
        sum += i

print("\nSum of even numbers from 1 to", num, "is :", sum)
