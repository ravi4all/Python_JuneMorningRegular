# assert
# def withdraw():
#     total_bal = 10000
#     try:
#         amount = int(input("Enter the amount you want to withdraw : "))
#         assert (amount < total_bal), ValueError("Insufficient amount...")
#         total_bal -= amount
#     except AssertionError as err:
#         print(err)
#     print("Transaction Successfull...")

def withdraw():
    total_bal = 10000
    amount = int(input("Enter the amount you want to withdraw : "))
    assert (amount < total_bal), ValueError("Insufficient amount...")
    total_bal -= amount
    print("Remaining Balance",total_bal)
    print("Transaction Successfull...")

try:
    withdraw()
except AssertionError as err:
    print(err)
