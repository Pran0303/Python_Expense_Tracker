expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: R"))

        expenses.append((name, amount))

        print("Expense added successfully!")

    elif choice == "2":

        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            print("\nExpenses:")
            for expense in expenses:
                print(f"{expense[0]} - R{expense[1]:.2f}")

    elif choice == "3":

        total = sum(expense[1] for expense in expenses)

        print(f"\nTotal Expenses: R{total:.2f}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")