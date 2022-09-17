#8. Write a python script to calculate sum of digits of a given number.
n=int(input("Enter any number:"))
sum=0
while(n>0):
    dig=n%10
    sum=sum+dig
    n=n//10
print("The sum of digits is:",sum)
