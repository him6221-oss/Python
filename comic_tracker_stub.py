"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Comic Book Collection Tracker
Developer: Robert Romanowski
"""

# GLOBAL CONSTANTS
DATA_FILE = "collection.txt"
PUBLISHER_FILE = "publishers.txt"


def get_user_info():
    """Ask the collector for their name."""
    # TODO: Ask user for name
    return "Robert"


def collect_comic_data():
    """Collect comic information from the user."""
    # TODO: Ask for title
    # TODO: Ask for issue number
    # TODO: Load publisher list from publishers.txt
    # TODO: Ask for condition
    pass


def calculate_value(comic_data):
    """Estimate the value of the comic."""
    # TODO: Create logic to estimate comic value
    return 0.0


def save_collection(user, comic_value):
    """Save the comic entry and print a formatted collection label."""
    # TODO: Append entry to collection.txt
    # TODO: Print formatted comic entry
    pass


def main():

    # 1 Identity Phase
    name = get_user_info()
    print(f"Collector: {name}")

    # 2 Data Collection Phase
    current_comic = collect_comic_data()

    # 3 Processing Phase
    value = calculate_value(current_comic)

    # 4 Storage Phase
    save_collection(name, value)


main()