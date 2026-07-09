class Bankaccount:
    def __init__(self, balance=0):
        self.balance = balance

    
    def deposit(self, amount: float):
        if amount < 0:
            print("Amount manfiy bulishi mumkin emas!!!!")
            return
        self.balance += amount
        print(f"{amount} qo'yildi. Joriy balans: {self.balance}")

    
    def withdraw(self, amount: float):
        if amount < 0:
            print("MAnfiy son balans dan yechib bulmaydi!!!")
            return
        self.balance -= amount
        print(f"{amount} olindi. Joriy hisobdagi {self.balance}")


    
    def show_balance(self):
        return f"Sizning bank hisob raqamingizdagi summa {self.balance}"






account = Bankaccount()
account.deposit(250)
account.withdraw(30)
account.show_balance()