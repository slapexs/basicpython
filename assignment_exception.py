user = {"name":"John", "amount":5000}
print(user)

def deposit(amount):
    user["amount"] += amount

deposit(5000)
print(user)

def updatemoney(amount):
    user["amount"] -= amount
    print("update:", user)

def withdraw(amount):
    try:
        if user["amount"] >= amount:
            updatemoney(amount)
        else:
            raise Exception("Money invalid")
    except Exception as e:
        print("Error is: ", e)

withdraw(20000)