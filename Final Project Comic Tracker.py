"""
ASSIGNMENT 11B: SPRINT 4 - COMIC BOOK COLLECTION TRACKER
Developer: Robert Romanowski
"""

import datetime

# GLOBAL CONSTANTS
DATA_FILE = "collection.txt"
PUBLISHERS = ("DC", "Marvel", "Image", "Dark Horse")
BASE_COMIC_PRICE = 10.0  # Magic number moved to constant

def get_user_info():
    """Ask for user name."""
    name = input("Enter your name: ").title()
    return name

def collect_comic_data():
    """Collect comic details from user."""
    title = input("Enter comic title: ")
    issue = input("Enter issue number: ")

    print("Available publishers:", PUBLISHERS)
    publisher = input("Choose publisher: ")

    condition = input("Enter condition (Mint/Good/Fair/Poor): ")

    return {
        "title": title,
        "issue": issue,
        "publisher": publisher,
        "condition": condition
    }

def calculate_value(comic_data, base_value=BASE_COMIC_PRICE):
    """Estimate comic value (default base value)."""
    if comic_data["condition"].lower() == "mint":
        return base_value * 2
    else:
        return base_value

def save_collection(user, comic_data, value):
    """Save comic entry to a persistent text file with timestamp."""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(DATA_FILE, "a") as file:  # append mode inside loop
        file.write(f"[{current_time}] Collector: {user}\n")
        file.write(f"Title: {comic_data['title']}\n")
        file.write(f"Issue: {comic_data['issue']}\n")
        file.write(f"Publisher: {comic_data['publisher']}\n")
        file.write(f"Condition: {comic_data['condition']}\n")
        file.write(f"Estimated Value: ${value:.2f}\n")
        file.write("----------------------\n")
    
    print("Comic entry successfully logged!\n")

def main():
    name = get_user_info()
    
    while True:
        comic = collect_comic_data()
        value = calculate_value(comic)
        save_collection(user=name, comic_data=comic, value=value)
        
        cont = input("Do you want to enter another comic? (yes/no): ")
        if cont.lower() != "yes":
            break

    print("All entries saved. Goodbye!")

main()