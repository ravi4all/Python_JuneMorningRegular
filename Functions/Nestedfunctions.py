# Nested Functions
def outer():
    print("This is outer function")

    def inner_1():
        print("this is inner_1 function")

    def inner_2():
        print("this is inner_2 function")

    inner_1()
    inner_2()

# inner()
outer()