import getpass


class PasswordManager:
    def __init__(self):
        self.passwords = {}

    @staticmethod
    def authenticate(func):
        def wrapper(self, *args, **kwargs):
            password = getpass.getpass(prompt="Enter password: ")
            if password == self.password:
                return func(self, *args, **kwargs)
            else:
                raise ValueError("Invalid password")
        return wrapper

    def add_password(self, account, password):
        self.passwords[account] = password

    @authenticate
    def get_password(self, account):
        return self.passwords[account]

    @authenticate
    def delete_password(self, account):
        del self.passwords[account]

    def set_master_password(self):
        self.password = getpass.getpass(prompt="Set master password: ")


if __name__ == '__main__':
    manager = PasswordManager()
    manager.set_master_password()
    print(manager.passwords)

    while True:
        try:
            print("\n1. Add password\n2. Get password\n3. Delete password\n4. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                account = input("Enter account name: ")
                password = getpass.getpass(prompt="Enter password: ")
                manager.add_password(account, password)
                print(manager.passwords)
            elif choice == 2:
                account = input("Enter account name: ")
                password = manager.get_password(account)
                print(f"Password for {account}: {password}")
            elif choice == 3:
                account = input("Enter account name: ")
                manager.delete_password(account)
                print(f"Deleted password for {account}")
            elif choice == 4:
                break
            else:
                print("Invalid choice")
        except ValueError as e:
            print(f"Error: {e}")
