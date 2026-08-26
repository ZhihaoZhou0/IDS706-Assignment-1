# Return a welcome message using the provided name.
def welcome_message(name):
    return f"{name}, welcome to the Data Engineering course."


if __name__ == "__main__":
    # Ask the user for their name and remove extra whitespace.
    name = input("Enter your name: ").strip()

    # Use a default name if the user enters nothing.
    if not name:
        name = "friend"

    print(welcome_message(name))
