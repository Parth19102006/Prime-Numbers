def prime_number(n):                                    #Prime number function.
    x = 2                                               #Initialize the first prime number.
    c = 0

    while c<n:
        for d in range(2, int(x**0.5)+1):
            if x%d == 0:                               #Check if the number is prime or not.
                break
        else:
            print(x)                                   #Prints the number if it is prime.
            c+=1
        x+=1

#Taking input for first n prime numbers.
prime_number(int(input("Enter number: ")))
