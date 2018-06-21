# by default file will open in read mode
file = open('demo_1.txt')

# data = file.read()

# data = file.read(6)

# data = file.readlines()

# data = file.readline()

file.seek(10)
data = file.read()
print(data)

file.close()