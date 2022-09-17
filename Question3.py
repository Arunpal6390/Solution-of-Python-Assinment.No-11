#3. Write a python script to calculate sum of cubes of first N natural numbers
n=int(input("Enter a number: "))
sum = 0
while(n>0):
    sum=sum+(n**3)
    n=n-1
print("The sum of first n square natural numbers is",sum)

