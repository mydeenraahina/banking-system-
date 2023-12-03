print("Hey! customer..")
class BankingSystem:
                initial_balance=100
                def __init__(self,account_no=None,account_holder_name=None):
                   if account_no!=None and account_holder_name!=None:
                       self.account_no=account_no
                       self.account_holder_name=account_holder_name
                       print(f"ACCOUNT NO: {self.account_no}")
                       print(f"ACCOUNT HOLDER NAME: {self.account_holder_name}")
                def account_creation(self):
                    while True:
                        getting_acc_no=input("Enter [11-didgit] Number to create you new account_no:")
                        if getting_acc_no.isdigit() and len(getting_acc_no)==11:
                            break
                        else:
                           print(f"Enter a valid input..")
                    while True:
                        getting_acc_name=input("Enter Your Name :")
                        if getting_acc_name.isalpha():
                            break
                        else:
                             print(f"Enter a valid input..")
                    while True:
                        try:
                            getting_initial_balance=int(input("Enter initial balance here :"))
                            BankingSystem.initial_balance=getting_initial_balance#inital amount changed
                            break
                        except ValueError as e1:
                            print(f"Enter a valid input..")
                            print(e1)
            
                    print(f"Account_No={getting_acc_no}\nAccount holder={getting_acc_name}\nAccount created successfully!")
                    
                def deposit(self):
                    while True:
                        deposit_amount=float(input("Enter amount  to deposit "))
                        if deposit_amount==0 or deposit_amount<0:
                            print(f"Enter a valid amount deposit")
                        else:
                            print(f"Account balance =: {self.initial_balance}")
                            print(f"deposited amount :{deposit_amount}")
                            self.initial_balance+=deposit_amount
                            print(f"current_balance ={self.initial_balance}")
                            print(f"Thank u.. visit again...")
                            break
                            
                def withdraw(self):
                    withdraw_amount=float(input("Enter amount for withdraw"))
                    if withdraw_amount==0 or withdraw_amount<0:
                        print(f"Enter a valid amount for withdraw")
                    else:
                        if int(withdraw_amount)>self.initial_balance:
                            print(f"Sorry! You have not enough money for withdrawal")
                        else:
                            print(f"Account balance =: {self.initial_balance}")
                            print(f"Total Amount receicevd: {withdraw_amount}")
                            self.initial_balance-=withdraw_amount
                            print(f"current_balance ={self.initial_balance}")
                            print(f"Thank u.. visit again...")
                def account_balance(self):
                    print("Account balance:",BankingSystem.initial_balance)
def menu_block():
    print(f"Here are the options available for you..")
    menu_list=["Menu","1.Create Account","2.Deposite","3.Withdraw","4.Display Balance","5.Exit"]
    [print(option) for option in menu_list]
def account_details_validation():
    while True:
        account_no=input("Enter your account number..")
        if account_no.isdigit() and len(account_no)==11:
                break
        else:
                print(f"Enter a valid input..")
    while True:
        account_holder_name=input("Enter account holder name..")
        if  account_holder_name.isalpha():
                break
        else:
                print(f"Enter a valid input..")
    return account_no,account_holder_name
    
def main_block():
    menu_block()
    while True:
        getting_input=input("Enter your choice from the above options: ")
        if getting_input=="1":
            obj=BankingSystem()
            obj.account_creation()
            break
        elif getting_input=="2":
            account_no,account_holder_name=account_details_validation()
            deposit_obj=BankingSystem(account_no,account_holder_name)
            deposit_obj.deposit()
            break
        elif getting_input=="3":
            account_no,account_holder_name=account_details_validation()
            withdrawal_obj=BankingSystem(account_no,account_holder_name)
            withdrawal_obj.withdraw()
            break
        elif getting_input=="4":
            account_no,account_holder_name=account_details_validation()
            balance_obj=BankingSystem(account_no,account_holder_name)
            balance_obj.account_balance()
            break
        elif getting_input=="5":
            print(f"you are going to exit!..")
            exit()
        else:
            print(f"Enter a valid input")
            
def continue_choice():
    while True:
        getting_choice=input(f"Do you want to continue baking....[yes/no] :").casefold()
        if getting_choice=="yes":
            main_block()
            break
        elif getting_choice=="no":
            print(f"you are going to exit!..")
            exit()
        else:
            print(f"Enter a valid input")
            
main_block()#calling main_block
continue_choice()#calling continue_choice
                    
