class BankAcc():
    def __init__(self, bank_acc_no):
        self.bank_acc_no = bank_acc_no
        self.balance = 0
    def deposit(self, depo):
        self.balance += depo
    def withdraw(self, widra):
        if(self.balance - widra < 0):
            print("Insufficient funds on the account")
        else:
            self.balance -= widra
    def status(self):
        status = (f"Bank Account No: {self.bank_acc_no}\n"
                  f"Balance: PLN {self.balance:.2f}")
        print(status)

my_acc = BankAcc("11 1111 1111 1111 1111 1111 1111")

my_acc.status()

my_acc.deposit(25.30)
my_acc.status()

my_acc.withdraw(31.70)

my_acc.withdraw(14)
my_acc.status()