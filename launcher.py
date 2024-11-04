import requests
import os
import time

# URL to your hosted script on GitHub
SCRIPT_URL = "https://raw.githubusercontent.com/eumonk/dotdot-series/main/Dos.py"
LOCAL_SCRIPT_PATH = "Dos.py"
CHECK_INTERVAL = 300  # Interval to check for updates (in seconds)

def download_latest_script():
    """Downloads the latest version of the script."""
    try:
        response = requests.get(SCRIPT_URL)
        response.raise_for_status()  # Ensure the request was successful

        # Write the latest script to file
        with open(LOCAL_SCRIPT_PATH, "w") as file:
            file.write(response.text)
        
        print("Latest version of Dos.py downloaded.")
    except Exception as e:
        print(f"Error downloading the script: {e}")

def execute_script():
    """Executes the downloaded script."""
    print("Executing Dos.py...")
    os.system(f"python {LOCAL_SCRIPT_PATH}")

def main():
    print("Starting the launcher and checking for updates...")
    last_update_time = 0

    while True:
        # Check if the update interval has passed
        if time.time() - last_update_time >= CHECK_INTERVAL:
            print("Checking for script updates...")
            download_latest_script()
            last_update_time = time.time()

        # Execute the script
        execute_script()
        
        # Wait for the next update check
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
