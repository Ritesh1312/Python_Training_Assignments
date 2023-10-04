from banking.bank import Bank
from banking.atm import ATM
def main():
    print('HELLO (^_^)')
    sbi = Bank('SBI', 12)
    atm = ATM(sbi)
    sbi.create_account('Ritesh' ,'pass', 50000)
    sbi.create_account('Mohak' ,'pass', 50000)
    sbi.create_account('Pradumn' ,'pass', 50000)
    sbi.create_account('Amitabh' ,'pass', 50000)
    sbi.create_account('Aditya' ,'pass', 50000)
    sbi.info_all__accounts()
    while True:
        if atm.start():
            continue



if __name__=='__main__':
    main()