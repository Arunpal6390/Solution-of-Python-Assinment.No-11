#2. Write a python script to calculate sum of squares of first N natural numbers
n=int(input("Enter a number: "))
sum = 0
while(n>0):
    sum=sum+(n**2)
    n=n-1
print("The sum of first n square natural numbers is",sum)