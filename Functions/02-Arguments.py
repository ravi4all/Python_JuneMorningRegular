# Arguments/Parameters
def add(x,y):
    z = x + y
    print("Sum is",z)

def sub(x,y):
    z = x - y
    print("Diff is",z)

def mul(x=1,y=1):
    z = x * y
    print("Mul is",z)

add(12,20)
sub(x = 10, y = 2)
mul(50,2)
