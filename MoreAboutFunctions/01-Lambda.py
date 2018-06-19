temp = [34.5,33.2,34.8,39.8,37.6,31.2]

# def temp_conv(c):
#     return 9/5 * c + 32
#
# for t in temp:
#     print(temp_conv(t))

# f = list(map(temp_conv,temp))
# print(f)

f = list(map(lambda c : 9/5 * c + 32, temp))
print(f)