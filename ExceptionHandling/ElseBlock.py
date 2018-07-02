import io
try:
    file = open('demo_1.txt','w')
    data = "Hello this is some demo text"
    file.write(data)
    # d = file.read()
    # print("Data is",d)

except FileNotFoundError as ex:
    print(ex)
except io.UnsupportedOperation as ex:
    print("File read operation is not supported in write mode")

else:
    print("Else block is executed...")

finally:
    print("I will always execute...")
    file.close()