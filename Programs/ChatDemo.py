hello_intent = ['hello','hey','hi']
bye_intent = ['bye','bie','take care','ok bye']

# if userinput == 'hi' or userinput == 'hello' or userinput == 'hey':
#     print("Hi")
# elif userinput == 'bye' or userinput == 'take care':
#     print('Bye..See you soon')
# elif userinput == 'how are you':
#     print('Fine')

while True:
    userinput = input("Enter your message : ")
    if userinput in hello_intent:
        print('Hi')
    elif userinput in bye_intent:
        print('Bye')