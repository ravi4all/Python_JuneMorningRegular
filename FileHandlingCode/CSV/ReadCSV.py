import csv

def read_csv(filename):
    dataset = []
    with open(filename) as file:
        data = csv.reader(file)
        for row in data:
            # print(row)
            dataset.append(row)

    return dataset

path = 'data.csv'
dataset = read_csv(path)
print(dataset)