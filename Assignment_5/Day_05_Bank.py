### Model For Bank Account Transactions

class Bank:
    pass

def create_account(account_number,name,password,balance,interest):
    b = Bank()
    b.account_number = account_number
    b.name = name
    b.password = password
    b.balance = balance
    b.interest = interest
    return b

def is_valid(amount):
    return amount>0

def deposit(b,amount):
    if is_valid(amount):
        b.balance += amount
        print(f'Amount deposited = {amount}')

    else:
        print("< Invalid amount input >")

def withdraw(b, amount, password="Ritesh@123"):
    if amount > 0 and (amount < b.balance) and password == b.password :
        b.balance -= amount
        print(f'Amount withdrawn = {amount}')
    else:
        print("< Invalid amount input or Invalid Password >")

def credit_interest(b):
    b.balance += ((b.balance*b.interest)/1200)
    print(" Showing Balance after Credit Interest")

def info(b):
    return f' Account Number = {b.account_number} \n Name = {b.name} \n Balance = {b.balance} \n Interest rate = {b.interest}% \n\n '
   
def info_display(b):
    print(info(b))

def main():
    b = create_account(397106315261,"Ritesh","Ritesh@123",50000,12)

    if isinstance(b,Bank):
        info_display(b)
        deposit(b,5000)
        info_display(b)
        withdraw(b,30000,'Ritesh@123')
        info_display(b)
        credit_interest(b)
        info_display(b)
    else:
        print(" Invalid Object ")

if __name__ == '__main__':
    main()



