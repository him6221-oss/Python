"""
ASSIGNMENT 10B: SPRINT 3 - REFACTORING & DATA ACCOUNTABILITY
Project: Comic Book Collection Tracker (V3.0)
Developer: Robert Romanowski
"""

# GLOBAL CONSTANTS
DATA_FILE = "collection.txt"
PUBLISHERS = ("DC", "Marvel", "Image", "Dark Horse")


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


def calculate_value(comic_data, base_value=10.0):
    """Estimate comic value (default base value)."""
    # simple beginner logic
    if comic_data["condition"].lower() == "mint":
        return base_value * 2
    else:
        return base_value


def save_collection(user, value):
    """Display comic entry (file saving later)."""
    print("\n--- COMIC ENTRY ---")
    print(f"Collector: {user}")
    print(f"Estimated Value: ${value:.2f}")


def main():
    # 1 User Phase
    name = get_user_info()

    # 2 Data Collection
    comic = collect_comic_data()

    # 3 Processing
    value = calculate_value(comic)

    # 4 Output (KEYWORD ARGUMENTS)
    save_collection(user=name, value=value)


main()