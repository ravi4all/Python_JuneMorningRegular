import time

a = []

start = time.time()

# for i in range(1,10000001):
#     a.append(i)

a = [i for i in range(1,10000001)]

end = time.time()

total = end - start
print("Total time taken",total)