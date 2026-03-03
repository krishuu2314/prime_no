n = int(input("Enter any number: "))

if n <= 1:
    print("The number is not prime")
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            print("The number is not prime")
            break
        i += 1
    else:
        print("The number is prime")