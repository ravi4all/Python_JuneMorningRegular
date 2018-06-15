def add(x,y):
    result = x + y
    print("Addition is",result)

def sub(x,y):
    result = x - y
    print("Subtraction is", result)

def mul(x,y):
    result = x * y
    print("Multiplication is", result)

def div(x,y):
    result = x / y
    print("Division is", result)

print("""
1. Add
2. Sub
3. Mul
4. Div
""")

user_choice = input("Enter your choice : ")

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

todo = {
    '1' : add,
    '2' : sub,
    '3' : mul,
    '4' : div
}

todo.get(user_choice)(num_1, num_2)

