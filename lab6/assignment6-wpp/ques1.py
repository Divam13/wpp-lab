class Password_manager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        return self.old_passwords[-1] if self.old_passwords else None

    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            print("Password has been set successfully.")
        else:
            print("Password has been used before. Please choose a different password.")

    def is_correct(self, password):
        return password == self.get_password()

def main():
    pm = Password_manager()

    while True:
        print("\nPassword Manager")
        print("1. Set Password")
        print("2. Get Current Password")
        print("3. Check Password")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            new_password = input("Enter new password: ")
            pm.set_password(new_password)
        elif choice == '2':
            current_password = pm.get_password()
            if current_password:
                print(f"Current Password: {current_password}")
            else:
                print("No password set yet.")
        elif choice == '3':
            password = input("Enter password to check: ")
            if pm.is_correct(password):
                print("Password is correct.")
            else:
                print("Password is incorrect.")
        elif choice == '4':
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
