from cryptography.fernet import Fernet
import os

def write_key(filename="key.key"):
    """Generates a Fernet key and writes it to a file."""
    try:
        key = Fernet.generate_key()
        with open(filename, "wb") as key_file:
            key_file.write(key)
        print(f"Key successfully written to {filename}")
    except OSError as e:
        print(f"Error writing key to file: {e}")
        raise

def load_key(filename="key.key"):
    """Loads a Fernet key from a file."""
    try:
        with open(filename, "rb") as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        print(f"Error: Key file '{filename}' not found. Generating a new key.")
        write_key(filename) # Generate a new key if the file doesn't exist
        return load_key(filename) # Load it
    except OSError as e:
        print(f"Error reading key file: {e}")
        raise

# Load or generate the key
try:
    key = load_key()
except OSError:
    print("Failed to load or generate key. Exiting.")
    exit()

fer = Fernet(key)

def view():
    try:
        with open('password.text', 'r') as f:
            print("Here are the stored passwords:")
            for line in f:
                try:
                    data = line.rstrip()
                    user, encrypted_pass = data.split(":")  # Corrected split character
                    decrypted_pass = fer.decrypt(encrypted_pass.encode()).decode()
                    print(f"User: {user} | Password: {decrypted_pass}")
                except ValueError:
                    print(f"Warning: Invalid format in line: {line.strip()}")  # Handle bad lines
                except Exception as e:
                    print(f"Error decrypting password for user {user}: {e}") # Handle decryption errors

    except FileNotFoundError:
        print("Password file 'password.text' not found.")
    except Exception as e:
        print(f"An error occurred while viewing passwords: {e}")


def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    encrypted_pass = fer.encrypt(pwd.encode()).decode() #Encode password and decode the encrypted to string, to store in the file
    try:
        with open('password.text', 'a') as f:
            f.write(f"{name}:{encrypted_pass}\n")  # Corrected separator
        print("The name and password have been successfully added to the file.")
    except Exception as e:
        print(f"An error occurred while adding the password: {e}")

while True:
    mode = input("Would you like to add a new password or view existing ones (add/view), or press 'q' to quit? ").lower() #.lower() for case insensitive input
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")