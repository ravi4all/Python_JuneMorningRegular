import random

hello_intent = ['hello','hey','hi']
bye_intent = ['bye','bie','take care','ok bye']

while True:
    userinput = input("Enter your message : ")

    cpu_hello = random.choice(hello_intent)
    cpu_bye = random.choice(bye_intent)

    if userinput in hello_intent:
        print(cpu_hello)
    elif userinput in bye_intent:
        print(cpu_bye)
    else:
        print("I don't understand")