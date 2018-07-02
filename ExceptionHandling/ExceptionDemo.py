try:
    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))
    i = num_1 + num_2
    print("Sum is",i)

    j = num_1 - num_2
    print("Diff is",j)

    k = num_1 / num_2
    print("Div is",k)

    l = num_1 * num_2
    print("Mul is",l)

except BaseException as ex:
    print(ex)