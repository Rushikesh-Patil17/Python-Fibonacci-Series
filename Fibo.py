limit = eval(input("Enter the no of terms for Fibonacci Series: "))

a = 0
b = 1

count = 0

while count < limit:
    print(a)
    temp = a + b
    
    a = b
    b = temp

    count += 1
