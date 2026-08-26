# Return a welcome message using the provided name.
def welcome_message(name):
    return f"{name}, welcome to the Data Engineering course."


if __name__ == "__main__":
    # Ask the user for their name and display the welcome message.
    name = input("Enter your name: ")
    print(welcome_message(name))
