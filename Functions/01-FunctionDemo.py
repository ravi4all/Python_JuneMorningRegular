# Scope - Local and Global

# Global Variable
message = 'Output is'

def add():
    # local variables
    a = 10
    b = 12
    c = a + b
    # print("Sum is",c)
    print(message,c)

def sub():
    a = 23
    b = 10
    c = a - b
    # print("Diff is",c)
    print(message,c)

# function call
add()
sub()