"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""

import datetime

def main():
    bug_dict = {}

    while True:
        choice = input("Enter 'log' to record a bug, or 'quit' to stop: ").lower()

        if choice == "quit":
            print("Bug log updated!")
            break

        elif choice == "log":
            # 1. Collect data
            file_name = input("File name: ")
            description = input("Description of error: ")
            priority = input("Priority (High, Medium, Low): ")

            # 2. Get timestamp
            current_time = datetime.datetime.now()
            timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

            # 3. Store in dictionary
            bug_dict[timestamp] = [file_name, description, priority]

            # 4. Append to file
            with open("bug_log.txt", "a") as file:
                file.write(f"[{timestamp}]\n")
                file.write(f"File: {file_name}\n")
                file.write(f"Status: {description}\n")
                file.write(f"Priority: {priority}\n")
                file.write("-" * 50 + "\n")

        else:
            print("Invalid option. Try again.")

# Run program
main()