import time
from datetime import datetime as dt

# Host file path (for Windows, Linux, macOS)
hosts_path = "/etc/hosts"  # Modify this path accordingly

# List of websites to block
websites_to_block = ["www.facebook.com", "www.twitter.com"]

# IP address to redirect the blocked websites
redirect_ip = "127.0.0.1"

# Define the working hours during which the websites will be blocked
start_time = dt(dt.now().year, dt.now().month, dt.now().day, 8)  # Start time (e.g., 8 AM)
end_time = dt(dt.now().year, dt.now().month, dt.now().day, 16)   # End time (e.g., 4 PM)

while True:
    # Check if the current time is within the working hours
    if start_time <= dt.now() <= end_time:
        # Open the host file in append mode
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in websites_to_block:
                if website in content:
                    # Website is already blocked
                    continue
                # Add the blocked website to the host file
                file.write(redirect_ip + " " + website + "\n")
        print("Websites blocked.")
    else:
        # Open the host file in read mode
        with open(hosts_path, "r") as file:
            lines = file.readlines()
        with open(hosts_path, "w") as file:
            for line in lines:
                # Remove the blocked websites from the host file
                if not any(website in line for website in websites_to_block):
                    file.write(line)
        print("Websites unblocked.")
    
    # Check every 5 seconds (you can adjust this interval)
    time.sleep(5)

