print(f"...WELCOME TO BOI BANK !!!...")
try:
    customer_account_no=int(input("Enter your account_no "))
    if customer_account_no==0 or customer_account_no<0:
        print(f"enter a valid account number")
    else:
        
        customer_name=str(input("enter your name :"))
        if customer_name.isalpha() or customer_account_no<0:
            print(f"[DEPOSITE] [WITHDRAW]")
            print(f"click 1 to deposite \n click 2 for withdraw ")

            class Customer_Details:
                initial_balance=100
                def __init__(self,account_no,account_holder_name):
                    self.account_no=account_no
                    self.account_holder_name=account_holder_name
                    print(f"ACCOUNT NO: {self.account_no}")
                    print(f"ACCOUNT HOLDER NAME: {self.account_holder_name}")

                    
            class Bank_Account(Customer_Details):       
                def deposit(self):
                    deposit_amount=float(input("Enter amount  to deposit "))
                    if deposit_amount==0 or deposit_amount<0:
                        print(f"Enter a valid amount deposit")
                    else:
                        print(f"Account balance =: {obj.initial_balance}")
                        print(f"deposited amount :{deposit_amount}")
                        obj.initial_balance+=deposit_amount
                        print(f"current_balance ={obj.initial_balance}")
                        print(f"Thank u.. visit again...")
                    
                def withdraw(self):
                    withdraw_amount=float(input("Enter amount for withdraw"))
                    if withdraw_amount==0 or withdraw_amount<0:
                        print(f"Enter a valid amount for withdraw")
                    else:
                        
                        if int(withdraw_amount)>obj.initial_balance:
                            print(f"Sorry! You have not enough money for withdrawal")
                        else:
                            print(f"Account balance =: {obj.initial_balance}")
                            print(f"Total Amount receicevd: {withdraw_amount}")
                            obj.initial_balance-=withdraw_amount
                            print(f"current_balance ={obj.initial_balance}")
                            print(f"Thank u.. visit again...")
                        
            obj=Bank_Account(customer_account_no,customer_name)
            while True:
                getting_input=input("Enter your choice")
                if getting_input=="1":
                    obj.deposit()
                    break
                elif getting_input=="2":
                    obj.withdraw()
                    break
                else:
                    print(f"Enter a valid input")
                    
        else:
            print(f"Enter a valid account_name!!!")
except ValueError:
    print(f"Enter a valid account_number!!!")

