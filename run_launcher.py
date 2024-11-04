import os
import platform
import subprocess

def open_in_new_terminal(script_name):
    """Opens the specified script in a new terminal window."""
    system = platform.system()
    
    if system == "Windows":
        # For Windows, use 'start' to open in a new cmd terminal window
        subprocess.Popen(f'start cmd /k "python {script_name}"', shell=True)
    
    elif system == "Darwin":
        # For MacOS, use 'osascript' to open a new Terminal window
        subprocess.Popen(['osascript', '-e', f'tell application "Terminal" to do script "python3 {script_name}"'])
    
    elif system == "Linux":
        # For Linux, use x-terminal-emulator if available
        terminals = ["x-terminal-emulator", "gnome-terminal", "konsole", "xfce4-terminal", "lxterminal", "xterm"]
        for terminal in terminals:
            if subprocess.call(['which', terminal], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
                subprocess.Popen([terminal, '-e', f'python3 {script_name}'])
                return
        print("No supported terminal emulator found. Please install a terminal emulator.")
    else:
        print(f"Unsupported operating system: {system}")

if __name__ == "__main__":
    # Specify the script to run in a new terminal
    script_name = "launcher.py"
    open_in_new_terminal(script_name)
