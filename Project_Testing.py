class BudgetCalculator:
    def __init__(self, user_code, gross_income):
        self.user_code = user_code
        self.gross_income = gross_income
        self.tax = 0.0
        self.after_tax_income = 0.0
        self.expenses = {
            'Utilities': 0.0,
            'Rent': 0.0,
            'Transport': 0.0,
            'Health': 0.0,
            'Groceries': 0.0,
            'Communication': 0.0
        }
        self.total_expenses = 0.0
        self.net_income = 0.0

    def calculate_tax(self):
        try:
            annual_income = self.gross_income * 12
            if annual_income <= 237100:
                self.tax = annual_income * 0.18
            elif 237101 <= annual_income <= 370500:
                self.tax = 42678 + (annual_income - 237100) * 0.26
            elif 370501 <= annual_income <= 512800:
                self.tax = 77362 + (annual_income - 370500) * 0.31
            elif 512801 <= annual_income <= 673000:
                self.tax = 121475 + (annual_income - 512800) * 0.36
            elif 673001 <= annual_income <= 857900:
                self.tax = 179147 + (annual_income - 673000) * 0.39
            elif 857901 <= annual_income <= 1817000:
                self.tax = 251258 + (annual_income - 857900) * 0.41
            else:
                self.tax = 644489 + (annual_income - 1817000) * 0.45
            self.tax /= 12
            self.after_tax_income = self.gross_income - self.tax
        except TypeError:
            print("Error: Income must be a numeric value.")

    def calculate_expenses(self):
        try:
            self.expenses['Utilities'] = self.after_tax_income * 0.05
            self.expenses['Rent'] = self.after_tax_income * 0.15
            self.expenses['Transport'] = self.after_tax_income * 0.30
            self.expenses['Health'] = self.after_tax_income * 0.03
            self.expenses['Groceries'] = self.after_tax_income * 0.10
            self.expenses['Communication'] = self.after_tax_income * 0.02
            self.total_expenses = sum(self.expenses.values())
            self.net_income = self.after_tax_income - self.total_expenses
        except KeyError:
            print("Error: Missing expense category.")

    def display_budget(self):
        line = "-" * 50
        print("\n" + line)
        print(" " * 15 + "Monthly Budget")
        print(line)

        print("\nIncome")
        print(line)
        print(f"Gross Monthly Income (Before Tax): R{self.gross_income:,.2f}")
        print(f"Gross Monthly Income (After Tax): R{self.after_tax_income:,.2f}")

        print("\nExpenses")
        print(line)
        for category, amount in self.expenses.items():
            print(f"{category:<20} R{amount:,.10f}")

        print(line)
        print(f"Total Expenses:              R{self.total_expenses:,.10f}")
        print(line)
        print(f"\nNet Income:                 R{self.net_income:,.10f}")
        print(line + "\n")


def main():
    while True:
        print("Budget Portal\n")
        print("1. Create New Entry")
        print("0. Exit\n")
        choice = input("Select an option: ").strip()
        if choice == '0':
            print("Exiting program. Goodbye!")
            break
        elif choice == '1':
            user_code = input("Enter user code: ").strip()
            try:
                gross_income = float(input("Enter gross income before tax: "))
                if gross_income < 0:
                    raise ValueError("Income cannot be negative.")
            except ValueError as e:
                print(f"Invalid input: {e}\n")
                continue
            
            budget = BudgetCalculator(user_code, gross_income)
            try:
                budget.calculate_tax()
                budget.calculate_expenses()
            except Exception as e:
                print(f"Error calculating budget: {e}")
                continue

            budget.display_budget()
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
