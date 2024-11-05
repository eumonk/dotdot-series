from cryptography.fernet import Fernet
import bcrypt

# Load encryption key from file
with open("secret.key", "rb") as key_file:
    key = key_file.read()

# Initialize Fernet with the key
fernet = Fernet(key)

# Load and decrypt hashed passwords
with open("hashed_passwords.enc", "rb") as enc_file:
    encrypted_hashes = enc_file.read().splitlines()

# Decrypt each hash to get the actual hashed passwords
HASHED_PASSWORDS = [fernet.decrypt(encrypted_hash) for encrypted_hash in encrypted_hashes]

def validate_password(password):
    """Check if the provided password matches any stored hash."""
    return any(bcrypt.checkpw(password.encode('utf-8'), hashed) for hashed in HASHED_PASSWORDS)

def main():
    print("Welcome to the dot dot series")

    # Loop until the correct password is entered
    while True:
        password = input("Please enter the password to proceed: ")
        if validate_password(password):
            print("Access granted.")
            break
        else:
            print("Access denied. Please try again.")

    # Proceed with other functionalities after authentication
    print("Authenticated successfully!")
    # Additional code here...

if __name__ == "__main__":
    main()
