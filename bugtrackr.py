import os
from datetime import datetime

class Bug:
    def __init__(self, title, description, severity, priority, assignee, file_path=None):
        self.title = title
        self.description = description
        self.severity = severity
        self.priority = priority
        self.assignee = assignee
        self.status = "New"
        self.file_path = file_path
        self.created_at = datetime.now()

    def __str__(self):
        return f"{self.title} ({self.status})"

    def read_file(self):
        if not self.file_path:
            print("No file path provided for this bug.")
            return

        try:
            with open(os.path.join(os.path.dirname(__file__), self.file_path), "r") as f:
                content = f.read()
                print(f"Content of {self.file_path}:\n{content}")
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")

class BugTracker:
    def __init__(self):
        self.bugs = []

    def create_bug(self):
        title = input("Enter bug title: ")
        description = input("Enter bug description: ")
        severity = input("Enter bug severity (Low/Medium/High): ")
        priority = input("Enter bug priority (Low/Medium/High/Urgent): ")
        assignee = input("Enter bug assignee: ")
        file_path = input("Enter file path (optional): ")

        bug = Bug(title, description, severity, priority, assignee, file_path)
        self.bugs.append(bug)
        print(f"Bug {bug} created successfully at {bug.created_at}!")

    # rest of the code stays the same

    def view_bugs(self):
        if not self.bugs:
            print("No bugs found.")
        else:
            for i, bug in enumerate(self.bugs):
                print(f"{i+1}. {bug}")

    def update_status(self, index):
        if index > len(self.bugs):
            print(f"Invalid bug index: {index}")
            return

        bug = self.bugs[index-1]
        status = input(f"Enter new status for bug {bug}: ")
        bug.status = status
        print(f"Bug {bug} status updated to {status}.")

    def delete_bug(self, index):
        if index > len(self.bugs):
            print(f"Invalid bug index: {index}")
            return

        bug = self.bugs.pop(index-1)
        print(f"Bug {bug} deleted successfully!")

    def option_menu(self):
        while True:
            print("\nSelect an option:")
            print("1. Create bug")
            print("2. View bugs")
            print("3. Update bug status")
            print("4. Delete bug")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_bug()
            elif choice == "2":
                self.view_bugs()
            elif choice == "3":
                index = int(input("Enter bug index to update status: "))
                self.update_status(index)
            elif choice == "4":
                index = int(input("Enter bug index to delete: "))
                self.delete_bug(index)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

# sample usage
tracker = BugTracker()
tracker.option_menu()