from datetime import datetime


class Subscription:
    def __init__(self, company_name, amount, start_date, subscription_type):
        self.company_name = company_name
        self.amount = amount
        self.start_date = start_date
        self.subscription_type = subscription_type


class SubsManager:
    def __init__(self):
        self.subscriptions = []

    def display_menu(self):
        print("Menu:")
        print("1. Add Subscription")
        print("2. View Subscriptions")
        print("3. Delete Subscription")
        print("4. Set Reminder")
        print("5. Calculate Average Spending")
        print("6. Exit")

    def add_subscription(self):
        company_name = input("Enter company name: ")
        amount = float(input("Enter amount: "))
        start_date = input("Enter start date (YYYY-MM-DD): ")
        subscription_type = input("Enter subscription type: ")
        subscription = Subscription(
            company_name, amount, start_date, subscription_type)
        self.subscriptions.append(subscription)
        print("Subscription added successfully.")

    def view_subscriptions(self):
        if not self.subscriptions:
            print("No subscriptions available.")
        else:
            print("Subscriptions:")
            for subscription in self.subscriptions:
                print(f"Company: {subscription.company_name}, Amount: {subscription.amount}, "
                      f"Start Date: {subscription.start_date}, Type: {subscription.subscription_type}")

    def delete_subscription(self):
        company_name = input("Enter company name to delete: ")
        for subscription in self.subscriptions:
            if subscription.company_name == company_name:
                self.subscriptions.remove(subscription)
                print("Subscription deleted successfully.")
                return
        print("Subscription not found.")

    def set_reminder(self, due_date):  # TODO Not complete yet
        print(f"Reminder set for due date: {due_date}")

    def calculate_average_spending(self):
        if not self.subscriptions:
            print("No subscriptions available.")
        else:
            total_spending = sum(
                subscription.amount for subscription in self.subscriptions)
            average_spending = total_spending / len(self.subscriptions)
            print(f"Average spending: {average_spending}")

    def user_authentication(self):  # TODO Not complete yet
        username = input("Enter username: ")
        password = input("Enter password: ")
        print("User authenticated successfully.")


if __name__ == "__main__":
    subs_manager = SubsManager()

    while True:
        subs_manager.display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            subs_manager.add_subscription()
        elif choice == "2":
            subs_manager.view_subscriptions()
        elif choice == "3":
            subs_manager.delete_subscription()
        elif choice == "4":
            due_date = input("Enter due date for reminder (YYYY-MM-DD): ")
            subs_manager.set_reminder(due_date)
        elif choice == "5":
            subs_manager.calculate_average_spending()
        elif choice == "6":
            print("Exiting SubsManager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
