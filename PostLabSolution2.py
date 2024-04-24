class SavingsAccount:
    def __init__(self, name, pin, balance=0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        return f"Name: {self.name}\nPin: {self.pin}\nBalance: {self.balance}"

    def get_balance(self):
        return self.balance

    def get_pin(self):
        return self.pin

    def get_name(self):
        return self.name

    def __eq__(self, account):
        return self.name == account.name

    def __lt__(self, account):
        return self.name < account.name

    def __gt__(self, account):
        return self.name > account.name or self.name == account.name

class Bank:
    def __init__(self):
        self.accounts = {}

    def add(self, account):
        key = self.make_key(account.get_name(), account.get_pin())
        self.accounts[key] = account

    def __str__(self):
        return '\n'.join(map(str, sorted(self.accounts.values())))

    def make_key(self, name, pin):
        return f"{name}/{pin}"

def main():
    bank = Bank()
    bank.add(SavingsAccount("Naya", 9999, 3000.00))
    bank.add(SavingsAccount("Artemis", 8888, 2000.00))
    bank.add(SavingsAccount("Athena", 7777, 1000.00))

    print(bank)

if __name__ == "__main__":
    main()
