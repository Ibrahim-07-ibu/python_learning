class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{self.name} deposited: {amount} New balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"{self.name} Not enough balance to transfer {amount}")
        else:
            self.balance -= amount
            print(f"{self.name} withdraw: {amount} New balance: {self.balance}")
    def show_balance(self):
        print(f"{self.name} current balance: {self.balance}")
    def transfer(self, amount, to_account):
        if amount > self.balance:
            print(f"{self.name} Not enough balance to transfer {amount}")
        else:
            self.balance -= amount
            to_account.balance += amount
            print(f"Transferred {amount} from: {self.name} to: {to_account.name} ")

acc1 = BankAccount("Ibu", 2000)
acc2 = BankAccount("Ibbu", 1000)


acc1.deposit(1000)
acc1.withdraw(4000)
acc1.show_balance()
acc1.transfer(1000,acc2)
acc1.show_balance()
class LibraryBook:
    def __init__(self, title, author,available_copies):
        self.title = title
        self.author = author
        self.available_copies = available_copies
    def borrow_book(self,borrow):
        if borrow > self.available_copies:
            print(f"Book not available! I have only:{self.available_copies} copies")
        else:
            self.available_copies -= borrow
            print(f"title: {self.title} name: {self.author} borrow: {borrow} total: {self.available_copies}")
    def return_book(self,returns):
        self.available_copies += returns
        print(f"title: {self.title} name: {self.author} returns: {returns} total: {self.available_copies}")
    def show_status(self):
        print(f"title: {self.title} author: {self.author} available_copies: {self.available_copies}")

bb1 = LibraryBook('three friends','ibu',3)
bb2 = LibraryBook('Tiger' , 'ibbu' , 4)
bb1.borrow_book(5)
bb1.return_book(1)
bb1.show_status()
