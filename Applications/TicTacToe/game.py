import random
import time

gamePosition = [0,1,2,3,4,5,6,7,8]

possibility = [
    [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
]

def check_winner(char):
    pass
    # for i in range(len(possibility)):
    #     if possibility[i][0] == char and possibility[i][1] == char and possibility[i][2] == char:
    #         return True

def gameBoard():
    print("""
     {} | {} | {}
    -----------
     {} | {} | {}
    -----------
     {} | {} | {}
    """.format(gamePosition[0], gamePosition[1],
               gamePosition[2], gamePosition[3],
               gamePosition[4], gamePosition[5],
               gamePosition[6], gamePosition[7],
               gamePosition[8]))

def game():
    pos_occupied = []
    user_ch = input("Enter your choice : X or 0 ? ")
    cpu_ch = ""
    if user_ch == 'X':
        cpu_ch = '0'
    elif user_ch == '0':
        cpu_ch = 'X'

    gameBoard()
    while True:
        user_pos = int(input("Enter your position : "))
        gamePosition[user_pos] = user_ch
        pos_occupied.append(user_pos)
        gameBoard()

        if check_winner(user_ch):
            print("User Win")
            break

        print("CPU Turn...")
        time.sleep(1)
        while True:
            cpu_pos = random.randrange(9)
            if cpu_pos not in pos_occupied:
                # print("Already Occupied")
                gamePosition[cpu_pos] = cpu_ch
                pos_occupied.append(cpu_pos)
                gameBoard()
                break

        if check_winner(cpu_ch):
            print("CPU Win")
            break

game()