even_numbers = []
# def even_num(num):
#     # return num % 2 == 0
#     if num % 2 == 0:
#         # return num
#         even_numbers.append(num)

def even_num(num):
    return num % 2 == 0

# print(even_num(10))

numbers = [i for i in range(1,51)]

# for n in numbers:
#     # print(even_num(n))
#     even_num(n)
#
# print(even_numbers)

# n = list(filter(even_num, numbers))
# print(n)


n = list(filter(lambda n : n % 2 == 0, [i for i in range(1,51)]))
print(n)



