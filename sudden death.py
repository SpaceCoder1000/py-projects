import os
import time

def countdown_and_save_data():
    # Countdown from 5
    for i in range(5, 0, -1):
        print(f"Counting down: {i}")
        time.sleep(1)

    # Folder setup
    folder_name = "ha-ha-ha"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created.")
    else:
        print(f"Folder '{folder_name}' already exists.")

    # File creation for 50GB data
    file_size_gb = 2  # Size of each file in GB
    total_size_gb = 30  # Total size in GB
    content = "Ha!" * (1024 * 1024 * 256)  # Approx. 1GB of text
    num_files = total_size_gb // file_size_gb

    for i in range(num_files):
        file_path = os.path.join(folder_name, f"file_{i+60}.txt")
        with open(file_path, "w") as f:
            f.write(content)
        print(f"Created file {i+1}/{num_files}: {file_path}")

    print("50GB of data has been generated in the folder.")

# Run the function
countdown_and_save_data()
