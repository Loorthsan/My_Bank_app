import random
 #higifg

balance = 0.0
transactions = []
account_book = {}

# login progream
def user_login():
    print("1. custemer_create")
    print("2. admin_login")
    while True :
        try :
            choose = int(input("enter a namber (1 or 2): "))

            if choose == 1:
                user_info()
                return
            elif choose == 2 : 
                admin_login()
                return
            else:
                print("Please choose a number between 1 or 2.")
        
        except ValueError:
            print("Please enter a valid number.")  
          
              

# ------------------Generate account number----------------------
def generate_account_number():
    return random.randint(222222, 333333)

# ------------------------User create account----------------------
def custemer_create():
    holder_name = input("Enter your name: ")
    password_number = input("Enter your password: ")
    phone_number = input("Enter your phone number: ")
    address = input("Enter your address: ")
    acc_number = generate_account_number()


    with open("customers.txt","a") as cust_fle: 
        cust_fle.write(f"{holder_name} \t {password_number} \t {phone_number} \t {address} \t {acc_number} \n")


    account_book[acc_number] = {
        "holder_name": holder_name,
        "password_number": password_number,
        "phone_number": phone_number,
        "address": address,
    }
    print("Account created successfully!")
    return acc_number 

    



#-------------------- Get initial balance--------------------
def get_initial_balance():
        try:
            balance = float(input("Enter initial deposit amount (Rs): "))
            print(f"Your balance is set to Rs {balance}")
            return balance
        except ValueError:
            print("Please enter a valid number.")
            return get_initial_balance()


# ---------------------------Deposit money------------------------------------
def deposit():
    global balance
    try:
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            balance += amount
            transactions.append(f"Deposited: Rs {amount}")
            print(f"Deposited: Rs {amount:.2f}")
            print(f"New balance: Rs {balance:.2f}")
        else:
            print("Please enter a positive amount.")
    except ValueError:
        print("Invalid input. Please enter a number.")

#-------------------------------- Withdraw money-------------------------
def withdraw():
    global balance
    try:
        amount = float(input("Enter the amount to withdraw: "))
        if amount > 0:
            if amount <= balance:
                balance -= amount
                transactions.append(f"Withdrawn: Rs {amount}")
                print(f"Withdrawn: Rs {amount:.2f}")
                print(f"New balance: Rs {balance:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Please enter a positive amount.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# ------------------Main program menu-----------------------------
def user_info ():
    global balance
    print("\n-----user menu")
    print("1. Create account")
    print("2. Deposit money")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. Transaction history")
    print("6. Exit")
    
    while True:
        try:
            choose = int(input("Enter a number (1-6): "))
            
            if choose == 1:
                acc_number = custemer_create()
                balance = get_initial_balance()
                print(f"Account created with balance: Rs {balance:.2f}")
                print(f"Your account number is: {acc_number}")
                print()

            elif choose == 2:
                deposit()
                print(f"Current balance is Rs {balance:.2f}")
                print()

            elif choose == 3:
                withdraw()
                print(f"Current balance is Rs {balance:.2f}")
                print()

            elif choose == 4:
                print(f"Your current balance is Rs {balance:.2f}")
                print()

            elif choose == 5:
                print("Transaction history:")
                for t in transactions:
                    print(f"- {t}")
                    print()

            elif choose == 6:
                print("Go bake!")
                user_login()
                break

            else:
                print("Please choose a number between 1 and 6.")
        
        except ValueError:
            print("Please enter a valid number.") 

# -----------------------------------admin login account----------------------------
def admin_info():
    admin_name="sangar"
    admin_password="1234"

    name = input("enter your name: ")
    password = input("enter your password: ")

    if name == admin_name and password == admin_password:
        print("access granted. wellcome!")
        return True
    else:
        print("access denied!")
        return False


def view_users_accounts():
    try:
        acc_number = int(input("Enter User's ID to lookup: "))
        if acc_number in account_book:
            print("User found:", account_book[acc_number])
        else:
            print("User not found.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for User ID.")


# -----------------------------------------delete account---------------------------------------
def delete_account():
    try:
        acc_number = int(input("Enter ID acc_number: "))
        if acc_number in account_book:
            del account_book[acc_number]
            print(f"User {acc_number} deleted.")
        else:
            print("User ID not valid.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")



def admin_login():
    while True:
        print("\n--- Admin Menu ---")
        print("1. admin_info")
        print("2. View all accounts")
        print("3. Delete account")
        print("4. Exit")

        try:
            choice = int(input("Enter a number (1-4): "))
            if choice == 1:
                admin_info()
            elif choice == 2:
                view_users_accounts()
                print()

            elif choice == 3:
                delete_account()
                print()

            elif choice == 4:
                print("work completed!")
                break
            else:
                print("Please choose a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

user_login()
