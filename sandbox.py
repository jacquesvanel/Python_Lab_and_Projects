def deposit():
    while True:
        amount = input("How much are you betting? $")
        if amount.isdigit():
            amount = int(amount)
            if amount <= 0:
                print("Enter more than $0.")
            else:
                break
        elif amount == float(amount):
                break
        else:
            print("That is not a number")
           
    return amount

deposit()
    