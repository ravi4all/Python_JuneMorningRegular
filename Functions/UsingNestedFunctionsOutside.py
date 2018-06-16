def calc(x,y):

    def add():
        return x + y

    def sub():
        return x - y

    def div():
        return x / y

    def mul():
        return x * y

    return add,sub,div,mul

result = calc(5,8)
# print(result)
print(result[0]())