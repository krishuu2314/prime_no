n= int(input("Enter any number: "))
i=2
f=0
while i<n:
    if n%i==0:
        f=1
    i+=1
if f==0:
    print("The number is prime")
else:
    print("The number is not prime")