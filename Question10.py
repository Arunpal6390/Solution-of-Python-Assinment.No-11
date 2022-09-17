'''
#10. Write a python script to print the octal equivalent of a given decimal number. (do not
use oct() method)
'''
decimal = int(input("Enter a decimal number: "))
octal = 0
ctr = 0
temp = decimal  # copying number

# computing octal using while loop
while (temp > 0):
    octal += ((temp % 8) * (10 ** ctr))  # Stacking remainders
    temp = int(temp / 8)  # updating dividend
    ctr += 1

print("Octal number of {x} is: {y}".format(x=decimal, y=octal))
