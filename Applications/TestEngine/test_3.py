import random

options = [
    ['pass','skip','continue','break'],
    ['C','C++','B','ABC'],
    ['pygame','numpy','pandas','opencv'],
    ['randomize','random','randint','rand'],
    ['rb','r','r+','rw']
]

answers = ['continue','ABC','pygame','random','rw']
counter = 0

wrong_var = []

file = open('questions.txt')
questions = file.readlines()

for i in range(len(questions)):
    index = random.randrange(len(questions))
    print(questions[index])
    opt_index = index
    opt = options[opt_index]
    print("1", opt[0], "2", opt[1])
    print("3", opt[2], "4", opt[3])
    user_input = int(input("Enter your choice : [1/2/3/4] : "))
    if opt[user_input - 1] == answers[opt_index]:
        counter += 1
    else:
        wrong_var.append(answers[opt_index])
    del questions[index]
    del options[opt_index]

print("Total",counter)
print("Correct Answers :",wrong_var)

file.close()

