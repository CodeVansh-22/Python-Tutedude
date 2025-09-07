def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n-1)
num= int(input("Enter A Number:"))
result=fact(num)
print(f"The Factorial Of {num} is {result}")