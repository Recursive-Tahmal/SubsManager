from datetime import datetime


class User:
    """Represents a user with basic information."""

    def __init__(self, name, email, phone, address, user_type, password):
        """Constructor for the User class.

        Args:
            name (str): User's name.
            email (str): User's email.
            phone (str): User's phone number.
            address (str): User's address.
            user_type (str): Type of user (student or tutor).
            password (str): User's password.
        """
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.user_type = user_type
        self.password = password


class RegistrationManager:
    """Manages user registration and login."""

    def __init__(self):
        """Constructor for the RegistrationManager class."""
        self.users = {}

    def register_user(self):
        """Registers a new user."""
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        address = input("Enter your address: ")
        user_type = input("Are you a student or a tutor? ")
        password = input("Create a password: ")

        user = User(name, email, phone, address, user_type, password)
        self.users[email] = user
        print(f"User {name} registered successfully as a {user_type}.\n")

    def login_user(self):
        """Logs in a user.

        Returns:
            bool: True if login is successful, False otherwise.
        """
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        user = self.users.get(email)
        if user and user.password == password:
            print(f"Welcome back, {user.name}!\n")
            return True
        else:
            print("Invalid email or password. Please try again.\n")
            return False

    def display_menu(self):
        """Displays the registration menu."""
        print("Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

    def user_registration(self):
        """Manages the user registration process."""
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                self.register_user()
            elif choice == "2":
                if self.login_user():
                    break
            elif choice == "3":
                print("Exiting User Registration.\n")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.\n")


class Subscription:
    """Represents a subscription with details."""

    def __init__(self, company_name, amount, start_date, subscription_type):
        """Constructor for the Subscription class.

        Args:
            company_name (str): Name of the subscribed company.
            amount (float): Subscription amount.
            start_date (datetime): Start date of the subscription.
            subscription_type (str): Type of subscription (Monthly, Yearly, One-Time).
        """
        self.company_name = company_name
        self.amount = amount
        self.start_date = start_date
        self.subscription_type = subscription_type


class SubsManager:
    """Manages subscription-related operations."""

    def __init__(self):
        """Constructor for the SubsManager class."""
        self.subscriptions = []

    def display_menu(self):
        """Displays the subscription management menu."""
        print("Menu:")
        print("1. Add Subscription")
        print("2. View Subscriptions")
        print("3. Delete Subscription")
        print("4. Set Reminder")
        print("5. Remove Reminder")
        print("6. Get Reminder")
        print("7. Calculate Average Spending")
        print("8. Exit")

    def add_subscription(self):
        """Adds a new subscription."""
        company_name = input("Enter company name: ")
        amount = 0
        start_date = None
        subscription_type = None

        while True:
            try:
                amount = float(input("Enter amount: "))
                break
            except ValueError:
                print("Invalid amount. Please enter a number.\n")

        while True:
            try:
                start_date = datetime.strptime(
                    input("Enter start date (DD-MM-YYYY): "), "%d-%m-%Y")
                break
            except ValueError:
                print("Invalid date. Please enter a date in the format DD-MM-YYYY.\n")

        while True:
            try:
                subscription_type = int(
                    input("Enter subscription type (1: Monthly, 2: Yearly, 3: One-Time): "))
                if subscription_type == 1:
                    subscription_type = "Monthly"
                elif subscription_type == 2:
                    subscription_type = "Yearly"
                elif subscription_type == 3:
                    subscription_type = "One-Time"
                else:
                    print(
                        "Invalid subscription type. Please enter a number between 1 and 3.\n")
                    continue
                break
            except ValueError:
                print(
                    "Invalid subscription type. Please enter a number between 1 and 3.\n")

        subscription = Subscription(
            company_name, amount, start_date, subscription_type)
        self.subscriptions.append(subscription)
        print("Subscription added successfully.\n")

    def view_subscriptions(self):
        """Displays existing subscriptions."""
        if not self.subscriptions:
            print("No subscriptions available.\n")
        else:
            print("Subscriptions:")
            for subscription in self.subscriptions:
                print(f"Company: {subscription.company_name}, Amount: {subscription.amount}, "
                      f"Start Date: {subscription.start_date}, Type: {subscription.subscription_type}")
            print()

    def delete_subscription(self):
        """Deletes a subscription."""
        self.view_subscriptions()
        company_name = input("Enter company name to delete: ")
        for subscription in self.subscriptions:
            if subscription.company_name == company_name:
                self.subscriptions.remove(subscription)
                print("Subscription deleted successfully.\n")
                return
        print("Subscription not found.\n")

    def set_reminder(self, due_date):
        """Sets a reminder for due date."""
        with open("due_date.txt", "a") as f:
            f.write(due_date + '\n')
        print("Reminder set successfully.\n")

    def remove_reminder(self, due_date):
        """Removes a reminder for a specific due date."""
        with open("due_date.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                if line.strip() != due_date:
                    f.write(line)
            f.truncate()
            f.write("\n")
        print(f"Reminder for {due_date} removed successfully.\n")

    def print_reminder(self):
        """Displays all reminders."""
        with open("due_date.txt", "r") as f:
            reminders = [line.strip()
                         for line in f.readlines() if line.strip()]
            if reminders:
                print("\n".join(reminders))
            else:
                print("No reminders available.")

    def calculate_average_spending(self):
        """Calculates and displays average spending."""
        if not self.subscriptions:
            print("No subscriptions available.\n")
        else:
            total_monthly_spending = 0
            total_yearly_spending = 0
            total_one_time_spending = 0

            for subscription in self.subscriptions:
                if subscription.subscription_type == "Monthly":
                    total_monthly_spending += subscription.amount
                elif subscription.subscription_type == "Yearly":
                    total_yearly_spending += subscription.amount
                elif subscription.subscription_type == "One-Time":
                    total_one_time_spending += subscription.amount

            print(
                f"Average monthly spending: {total_monthly_spending / len(self.subscriptions)}")
            print(
                f"Average yearly spending: {total_yearly_spending / len(self.subscriptions)}")
            print(
                f"Average one-time spending: {total_one_time_spending / len(self.subscriptions)}\n")


if __name__ == "__main__":
    registration_manager = RegistrationManager()
    subs_manager = SubsManager()
    print("Welcome to SubsManager!\n")

    while True:
        print("Main Menu:")
        print("1. User Registration")
        print("2. Subscription Management")
        print("3. Exit")

        main_choice = input("Enter your choice (1-3): ")
        print("\n")

        if main_choice == "1":
            registration_manager.user_registration()
        elif main_choice == "2":
            while True:
                subs_manager.display_menu()
                subs_choice = input("Enter your choice (1-8): ")
                print("\n")

                if subs_choice == "1":
                    subs_manager.add_subscription()
                elif subs_choice == "2":
                    subs_manager.view_subscriptions()
                elif subs_choice == "3":
                    subs_manager.delete_subscription()
                elif subs_choice == "4":
                    due_date = input(
                        "Enter due date for reminder (DD-MM-YYYY): ")
                    subs_manager.set_reminder(due_date)
                elif subs_choice == "5":
                    while True:
                        subs_manager.print_reminder()
                        due_date = input(
                            "Enter due date for reminder to remove (DD-MM-YYYY): ")
                        subs_manager.remove_reminder(due_date)
                        break
                elif subs_choice == "6":
                    subs_manager.print_reminder()
                elif subs_choice == "7":
                    subs_manager.calculate_average_spending()
                elif subs_choice == "8":
                    print("Exiting Subscription Management.\n")
                    break
                else:
                    print(
                        "Invalid choice. Please enter a number between 1 and 8.\n")
        elif main_choice == "3":
            print("Exiting Program. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.\n")
