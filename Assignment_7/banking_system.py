class Bank_Account:
    def __init__(self, account_number, name, password, balance, account_type):
        self._id = account_number
        self._name = name
        self._balance = balance
        self._password = password
        self._account_type = account_type
        self._interest_rate = 5

    def check_balance(self):
        return self._balance
    
    def is_valid_transact_amount(self, amount):
        if(amount > 0):
            return True
        raise Exception(' Enter Valid Amount for transaction !! ')
    
    def withdraw(self, amount):
        if self.is_valid_transact_amount(amount) :
            self._balance -= amount
            return True
    
    def deposit(self, amount):
        if self.is_valid_transact_amount(amount):
            self._balance += amount
            return True

    def credit_interest(self):
        if not self._balance<=0:
            interest = self._balance * self._interest_rate/1200
            self.deposit(interest)

    def get_info(self):
        return f'{self._name} {self._balance}'

class Savings_Account(Bank_Account):
    def __init__(self, account_number, name, password, balance, min_balance=5000):
        super().__init__(account_number, name, password, balance, account_type='SAVING')
        self._interest_rate = 12
        self._min_balance = min_balance
    
    def get_max_withdrawal_amount(self):
        return self._balance - self._min_balance
    
    def withdraw(self, amount):
        if amount < self.get_max_withdrawal_amount(): 
            return super().withdraw(amount)
    

class Current_Account(Bank_Account):
    def __init__(self, account_number, name, password, balance):
        super().__init__(account_number, name, password, balance, account_type='CURRENT')
        self._interest_rate = 0
        self._min_balance = 0
    
class OverDraft_Account(Bank_Account):
    def __init__(self, account_number, name, password, balance):
        super().__init__(account_number, name, password, balance, account_type='OVERDRAFT')
        self._interest_rate = 8
        self._max_balance = 0
        self._od_limit = 0
        self._od_fee_interest = 1


    def get_od_limit(self):
        limit = self._max_balance / 10
        return limit
    
    def get_max_withdrawal_amount(self):
        return self._balance + self.get_od_limit()
    
    def calculate_od_fee(self, amount):
        return (amount - self._balance)/100
    
    def withdraw(self, amount):
        if(amount < self.get_max_withdrawal_amount()):
            od_fee = self.calculate_od_fee(amount)
            super().withdraw(amount)
            super().withdraw(od_fee)
            return True
        return False
    
    def deposit(self, amount):
        super().deposit(amount)
        if self._balance > self._max_balance:
            self._max_balance = self._balance
    



class Bank:
    def __init__(self):
        self.__accounts = []
        self.__last_id = 1

    def is_valid_account(self, account):
        return isinstance(account, Bank_Account)

    def create_account(self, name, password, balance = 0, min_balance = 0 , account_type='SAVING'):
        if account_type.upper()=='CURRENT' :
            account = Current_Account(self.__last_id, name, password, balance)

        elif account_type.upper()=='OVERDRAFT' :
            account = OverDraft_Account(self.__last_id, name, password, balance)

        else:
            account = Savings_Account(self.__last_id, name, password, balance, min_balance)

        self.__accounts.append(account)
        self.__last_id += 1
        return account

    def authenticate(self, account, password):
        if self.is_valid_account(account):
            return account._password == password
        raise Exception('Invalid Credentials')
    
    def get_account(self, account_number):
        for index, account in enumerate(self.__accounts):
            if account._id == account_number:
                return (index, account)
        
        raise Exception('Account does not exist')
    
    def get_account_type(self, account_type):
        if(account_type == 'SAVING'):
            return Savings_Account
        elif account_type == 'CURRENT':
            return Current_Account   
        elif account_type == 'OVERDRAFT':
            return OverDraft_Account
        else:
            return None

    def delete_account(self, account_number):
        index, account = self.get_account(account_number)
        self.__accounts.pop(index)

    def transfer_money(self, from_account, to_account, amount):
        if not self.is_valid_account(from_account) or not self.is_valid_account(to_account): 
            raise Exception('Invalid account object')
        if from_account.withdraw(amount):
            to_account.deposit(amount)
            return True
        raise Exception('Insufficient Funds')
    
    def info_all__accounts(self, account_type=''):
        for account in self.__accounts:
            print(f'Number : {account._id}\t Name: {account._name}\t Balance {account._balance}')
    
    def deposit(self, account, amount):
        if self.is_valid_account(account):
            account.deposit(amount)
    

    def withdraw(self, account, amount):
        if self.is_valid_account(account):
            account.withdraw(amount)

    def credit_interest_all(self):
        for account in self.__accounts:
            account.credit_interest()

class ATM: 
    
    def __init__(self, Bank: Bank):
        self.__Bank = Bank

    def __get_user_after_auth(self):
        account_number = int(input('Enter Account Number'))
        password = input('Enter password')
        index, account = self.__Bank.get_account(account_number)
        print(self.__Bank)
        if account :
            if(self.__Bank.authenticate(account, password)):
                return account

            raise Exception('Invalid password')

        raise Exception('Account does not exist')
        

    def check_balance(self):
        account = self.__get_user_after_auth()
        print(f'Available Balance : {account._balance}')

    def cash_money(self):
        account = self.__get_user_after_auth()  
        amount = int(input('Enter Amount to withdraw'))
        account.withdraw(amount)

    

axis = Bank()
sbi = Bank()

account1 = axis.create_account('Ritesh', '@Ritesh1223', 50000)
account2 = axis.create_account('Amitabh', '@ami1223', 55000)
account3 = axis.create_account('Pradumn', '@Rprad1223', 60000)


account4 = sbi.create_account('Ritesh', '@Ritesh1223', 50000)
account5 = sbi.create_account('Amitabh', '@ami1223', 55000)
account6 = sbi.create_account('Pradumn', '@Rprad1223', 60000)

axis.info_all__accounts()
print()
sbi.info_all__accounts()


# axis.transfer_money(account1, account2, 100000)

axis.credit_interest_all()
sbi.credit_interest_all()
print()
axis.info_all__accounts()
print()
sbi.info_all__accounts()
print()
sbi_atm = ATM(sbi)
sbi_atm.check_balance()
sbi_atm.cash_money()
