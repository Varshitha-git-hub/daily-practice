
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

print(add(5, 3))  
print(subtract(10, 4))  
print(multiply(7, 2))  
print(divide(9, 3))  

