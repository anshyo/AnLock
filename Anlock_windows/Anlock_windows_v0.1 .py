# all the modules

import random   
import string
from time import sleep
from os import system
from getpass import getpass
import pathlib
import clipboard

# here is teh class having all kinds of functions i used in this password managment

class PasswordManager:
    def __init__(self, file_name):
        """
        Initialize the PasswordManager.

        Args:
            file_name (str): The name of the file to store passwords.
        """
        self.file_name = file_name
        self.passwords = {}
        self.logged_in = False
        self.load_passwords()

    def authenticate_user(self, master_password):
        """
        Authenticate the user with a master password.

        Args:
            master_password (str): The master password to check.

        """
        predefined_master_password = "dpsbsr"

        if master_password == predefined_master_password:
            self.logged_in = True
            print("Authentication successful.")
        else:
            print("Authentication failed. Access denied.")

    def load_passwords(self):
        """
        Load passwords from the file into the password manager.
        """
        try:
            with open(self.file_name, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    service, password = line.strip().split(',')
                    self.passwords[service] = password
        except FileNotFoundError:
            # File doesn't exist yet, initialize an empty dictionary.
            self.passwords = {}

    def save_passwords(self):
        """
        Save passwords to the file.
        """
        with open(self.file_name, 'w') as file:
            for service, password in self.passwords.items():
                file.write(f"{service},{password}\n")

    def add_password(self, service, password):
        """
        Add a new password entry for a service.

        Args:
            service (str): The name of the service.
            password (str): The password for the service.
        """
        self.passwords[service] = password
        self.save_passwords()

    def get_password(self, service):
        """
        Retrieve the password for a given service.

        Args:
            service (str): The name of the service.

        Returns:
            str: The password for the service or "Service not found" if not found.
        """
        return self.passwords.get(service, "Service not found")

    def update_password(self, service, new_password):
        """
        Update the password for a service.

        Args:
            service (str): The name of the service.
            new_password (str): The new password for the service.
        """
        if service in self.passwords:
            prev_pass = getpass(prompt="enter the previous password: ")
            if prev_pass == self.get_password(service):
                self.passwords[service] = new_password
                self.save_passwords()
            else:
                print("error")
        else:
            print(f"{service} not found in password manager.")

    def delete_password(self, service):
        """
        Delete a password entry for a service.

        Args:
            service (str): The name of the service to delete.
        """
        if service in self.passwords:
            del self.passwords[service]
            self.save_passwords()
        else:
            print(f"{service} not found in password manager.")

    def list_passwords(self):
        """
        List all stored password entries.
        """
        for service, password in self.passwords.items():
            print(f"Service: {service}, Password: {password}")
    
    def generate_password(self, length=12):
        """
        Generate a random password.

        Args:
            length (int): The length of the generated password.

        Returns:
            str: The generated password.
        """
        service = input("Name the service: ")
        password = ''
        for i in range(length):
            characters = string.ascii_letters + string.digits + string.punctuation
            password += str(random.choice(characters))
        self.add_password(service,password)
        clipboard.copy(password)
        print("password is copied to your clipboard")


    def is_strong_password(password):
        """
        Check if a password is strong based on certain criteria.

        Args:
            password (str): The password to check.

        Returns:
            bool: True if the password is strong, False otherwise.
        """

        return (
            len(password) >= 8 and
            any(char.isupper() for char in password) and
            any(char.islower() for char in password) and
            any(char.isdigit() for char in password) and
            any(char in string.punctuation for char in password)
        )
    
    def clear_all_password(self):
        """
        clears all the passwords and services
        """
        try:
            open(self.file_name , "a").truncate(0)
        except FileNotFoundError:
            open(self.file_name , "a").write(" ")

class paths:
    '''
    returns path of the file in with it is running or can just make a new folder
    '''
    def __init__(self) -> None:
        self.currentFilePath = self.path()

    def path():
        '''returns the file in which this is running'''
        path = str(pathlib.Path(__file__))
        path = path[::-1]
        npath = ""
        j = 0
        for i in path:
            if i == "\\" and j == 0:
                j += 1
            elif j == 1:
                npath += i
            else:
                pass
        return npath[::-1]

    def folder(self, name: str) -> str:
        """creates a new folder and gives returns its path"""
        return self.currentFilePath + "\\" + name

def main():
    password_manager = PasswordManager("pass.txt")
    while True:

        if not password_manager.logged_in:
            master_password = getpass(prompt="Enter your master password: ")
            password_manager.authenticate_user(master_password)
            if not password_manager.logged_in:
                continue


        print("\nPassword Manager Menu:")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. Update Password")
        print("4. Delete Password")
        print("5. List Passwords")
        print("6. Generate Password")
        print("7. Check Password Strength")
        print("8. Logout")
        print("9. Exit")
        print("10. Clear everything")

        choice = input("Enter your choice: ")

        system("cls")

        if choice == '1':
            print("""
Check password strength criteria (you can customize these criteria):
At least 8 characters
Contains at least one uppercase letter
Contains at least one lowercase letter
Contains at least one digit
Contains at least one special character
                """)
            service = input("Enter the service name: ")
            password = getpass(prompt="Enter the password: ")
            check = getpass(prompt="Re-enter the password: ")
            if check == password:
                pass
            else:
                print()
                print("Password didn't match")
            if PasswordManager.is_strong_password(str(password)):
                password_manager.add_password(service, password)
            else:
                print("Password does not meet the strength criteria.")

        elif choice == '2':
            service = input("Enter the service name: ")
            print(f"Password: {password_manager.get_password(service)}")

        elif choice == '3':
            print("""
Check password strength criteria (you can customize these criteria):
At least 8 characters
Contains at least one uppercase letter
Contains at least one lowercase letter
Contains at least one digit
Contains at least one special character
                """)
            service = input("Enter the service name: ")
            new_password = getpass(prompt = "Enter the new password: ")
            password_manager.update_password(service, new_password)

        elif choice == '4':
            service = input("Enter the service name: ")
            password_manager.delete_password(service)

        elif choice == '5':
            a = getpass(prompt="enter the master password:")
            if a == "dpsbsr":
                password_manager.list_passwords()
            else:
                print("error")

        elif choice == '6':
            password = str(password_manager.generate_password())

        elif choice == '7':
            password = input("Enter the password to check: ")
            if PasswordManager.is_strong_password(password):
                print("Password is strong.")
            else:
                print("Password is weak.")

        elif choice == '8':
            password_manager.logged_in = False
            print("Logged out.")
            sleep(3)
            break

        elif choice == '9':
            sleep(3)
            break
        
        elif choice == '10':
            password_manager.clear_all_password()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()