def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operations = {"+":add,"-":subtract,"*":multiply, "/":divide}

a = int(input("Enter the first number"))
for key in operations:
    print(key)
choice = input("choose any operation")
b = int(input("Enter the next number"))

operation_done = operations[choice]
value = operation_done(a, b)
print(value)


