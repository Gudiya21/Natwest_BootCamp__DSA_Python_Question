def factorial(a):
    if a==1:
        return 1
    else:
        return a*factorial(a-1)
print(factorial(int(input("Enter a number: "))))