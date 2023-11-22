customer_account_no=input("Enter your account_no ")
customer_name=input("enter your name :")
try:
    account_balance=input("Enter your account balance")
    print(f"[DEPOSITE] [WITHDRAW]")
    print(f"click 1 to deposite \n click 2 for withdraw ")
    class bank_account:
        def __init__(self,account_no,account_holder_name,account_balance):
            self.account_no=account_no
            self.account_holder_name=account_holder_name
            self.account_balance=account_balance
            print(f"ACCOUNT NO: {self.account_no}")
            print(f"ACCOUNT HOLDER NAME: {self.sccount_holder_name}")
            print(f"ACCOUNT BALANCE: {self.account_balance}")
        def deposit(self):
            deposit_amount=input("Enter amount  to deposit ")
            tot_val=int(self.account_balance)+int(deposit_amount)
            print(f"current_balance ={tot_val}")
        def withdraw(self):
            withdraw_amount=input("Enter amount for withdraw")
            tot_val=int(self.account_balance)-int(withdraw_amount)
            print(f"current_balance ={tot_val}")
    obj=bank_account(customer_account_no,customer_name,account_balance)
    getting_input=input("Enter your choice")
    if int(getting_input)==1:
        obj.deposit()
    elif int(getting_input)==2:
        obj.withdraw()
    else:
        print("enter a valid input")
except ValueError:
    print("Enter valid amount ")
