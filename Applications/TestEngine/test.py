import random
import copy

questions = [
    {'ques_id':1,'ques':'Which keyword is used to skip current iteration ?'},
    {'ques_id':2,'ques':'Python is successor of which language ?'},
    {'ques_id':3,'ques':'Which module is used for game development ?'},
    {'ques_id':4,'ques':'Which module is used get random numbers ?'},
    {'ques_id':5,'ques':'Which file mode is wrong ?'},
]

ques_copy = copy.deepcopy(questions)

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

for i in range(len(questions)):
    ques = random.choice(questions)
    print(ques['ques_id'],ques['ques'])
    opt_index = ques['ques_id'] - 1
    opt = options[opt_index]
    print("1",opt[0], "2",opt[1])
    print("3",opt[2], "4",opt[3])
    user_input = int(input("Enter your choice : [1/2/3/4] : "))
    if opt[user_input - 1] == answers[opt_index]:
        counter += 1
    else:
        wrong_var.append(answers[opt_index])
    del questions[opt_index]
print("Total",counter)
print("Correct Answers :",wrong_var)



