import getpass


class PassWordManager:
    def __init__(self):
        self.passwords = {}

    @staticmethod
    def authenticate(func):
        def wrapper(self, *args, **kwargs):
            password = getpass.getpass(prompt="Enter Password: ")
            if password == self.passwords['master']:
                return func(self, *args, **kwargs)
            else:
                raise ValueError('Invalid Password')
        return wrapper

    def set_master_password(self):
        self.passwords['master'] = getpass.getpass(
            prompt="Enter Master Password: ")

    @authenticate
    def get_password(self):
        account = input("Enter the account name: ")
        if account in self.passwords:
            return self.passwords[account]
        else:
            raise ValueError("Account not present: ")

    @authenticate
    def add_password(self):
        account = input("Add the account: ")
        password = input(f"Add the password for {account}: ")
        self.passwords[account] = password

    @authenticate
    def del_password(self):
        account = input("Enter the account")
        del self.passwords[account]
        print(self.passwords)


p = PassWordManager()
p.set_master_password()
# p.passwords[master] = master
# print(p.passwords)

while True:
    try:
        print("\n 1. Add Password \n 2. Get Password \n 3. Delete Account \n 4. Exit \n 5.Get Master Records")
        choice = int(input("Enter the choice: "))
        if choice == 1:
            p.add_password()
        elif choice == 2:
            print(p.get_password())

        elif choice == 3:
            p.del_password()
        elif choice == 4:
            break
        elif choice == 5:
            if len(p.passwords) == 0:
                print("No records")
            else:
                print(p.passwords)

        else:
            print("Invalid Choice")
    except ValueError as e:
        print(e)
