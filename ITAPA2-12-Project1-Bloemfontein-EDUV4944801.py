#Question 1

class BudgetCalculator:
    def __init__(self, user_code, gross_income):
        # Initializing the budget calculator with user details and income.
        self.user_code = user_code  
        self.gross_income = gross_income  
        self.tax = 0.0  
        self.after_tax_income = 0.0  

        # Defining a dictionary to store different expense categories.
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
            # Converting gross monthly income to annual income.
            annual_income = self.gross_income * 12  

            # Determining tax based on South African tax brackets.
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

            # Converting annual tax to monthly tax.
            self.tax /= 12  
            # Calculating after-tax income.
            self.after_tax_income = self.gross_income - self.tax  
        except TypeError:
            print("Error: Income must be a numeric value.")  

    def calculate_expenses(self):
        try:
            # Allocating fixed percentages of after-tax income to different expenses.
            self.expenses['Utilities'] = self.after_tax_income * 0.05  
            self.expenses['Rent'] = self.after_tax_income * 0.15  
            self.expenses['Transport'] = self.after_tax_income * 0.30  
            self.expenses['Health'] = self.after_tax_income * 0.03  
            self.expenses['Groceries'] = self.after_tax_income * 0.10  
            self.expenses['Communication'] = self.after_tax_income * 0.02  

            # Calculating total monthly expenses.
            self.total_expenses = sum(self.expenses.values())  
            # Calculating remaining net income after expenses.
            self.net_income = self.after_tax_income - self.total_expenses  
        except KeyError:
            print("Error: Missing expense category.")  

    def display_budget(self):
        line = "-" * 50  # Creating a horizontal separator.
        print("\n" + line)
        print(" " * 15 + "Monthly Budget")  # Centering heading.
        print(line)

        # Displaying income details.
        print("\nIncome")
        print(line)
        print(f"Gross Monthly Income (Before Tax): R{self.gross_income:,.2f}")  
        print(f"Gross Monthly Income (After Tax): R{self.after_tax_income:,.2f}")  

        # Displaying categorized expenses.
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
        # Displaying menu options.
        print("Budget Portal\n")
        print("1. Create New Entry")
        print("0. Exit\n")
        choice = input("Select an option: ").strip()  

        # Exiting the program if the user chooses option 0.
        if choice == '0':
            print("Exiting program. Goodbye!")
            break  
        elif choice == '1':
            # Prompting user for input.
            user_code = input("Enter user code: ").strip()  
            try:
                gross_income = float(input("Enter gross income before tax: "))  
                if gross_income < 0:
                    raise ValueError("Income cannot be negative.")  
            except ValueError as e:
                print(f"Invalid input: {e}\n")  
                continue  

            # Creating a BudgetCalculator object.
            budget = BudgetCalculator(user_code, gross_income)  

            try:
                # Performing calculations.
                budget.calculate_tax()  
                budget.calculate_expenses()  
            except Exception as e:
                print(f"Error calculating budget: {e}")  
                continue  

            # Displaying the final budget summary.
            budget.display_budget()  
        else:
            print("Invalid option. Please try again.\n")  


if __name__ == "__main__":
    # Running the main function when the script is executed.
    main()  



#Question 2

# Importing SQLite library for database management
import sqlite3  

class Store:
    def __init__(self):
        # Initializing the database when the store object is created
        self.initialize_database()  

    def initialize_database(self):
        """Creates the database and tables if they do not exist."""
        try:
            # Connecting to the SQLite database.
            conn = sqlite3.connect('store_database.db')  
            cursor = conn.cursor()
            # Creating Products table if it does not exist.
            cursor.execute('''CREATE TABLE IF NOT EXISTS Products
                             (prodID INTEGER PRIMARY KEY AUTOINCREMENT,
                              prodName TEXT,
                              prodPrice REAL,
                              prodQuantity INTEGER)''')
            # Creating Sales table if it does not exist.
            cursor.execute('''CREATE TABLE IF NOT EXISTS Sales
                             (saleID INTEGER PRIMARY KEY AUTOINCREMENT,
                              saleDate TEXT,
                              productName TEXT,
                              saleTotal REAL)''')
            # Saving changes.
            conn.commit()  
        except sqlite3.Error as e:
            # Printing database errors if any occur.
            print(f"Database error: {e}")  
        finally:
            # Closing the database connection.
            conn.close()  

    def add_product(self, name, price, quantity):
        """Adds a new product to the Products table."""
        try:
            with sqlite3.connect('store_database.db') as conn:
                cursor = conn.cursor()
                # Inserting product details into the Products table.
                cursor.execute("INSERT INTO Products (prodName, prodPrice, prodQuantity) VALUES (?, ?, ?)",
                               (name, price, quantity))
                conn.commit()
                print("Product added successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def remove_product(self, product_id):
        """Removes a product from the Products table based on the product ID."""
        try:
            with sqlite3.connect('store_database.db') as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Products WHERE prodID=?", (product_id,))
                conn.commit()
                if cursor.rowcount == 0:
                    # If no rows are affected, product doesn't exist.
                    print("Product not found.")  
                else:
                    print("Data deleted successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def update_product(self, product_id, new_name, new_price, new_quantity):
        """Updates an existing product's details in the database."""
        try:
            with sqlite3.connect('store_database.db') as conn:
                cursor = conn.cursor()
                # Updating product details using the given product ID.
                cursor.execute("UPDATE Products SET prodName=?, prodPrice=?, prodQuantity=? WHERE prodID=?",
                               (new_name, new_price, new_quantity, product_id))
                conn.commit()
                if cursor.rowcount == 0:
                    print("Product not found.")
                else:
                    print("Data updated successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def display_products(self):
        """Displays all products available in the database."""
        try:
            with sqlite3.connect('store_database.db') as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Products")
                # Fetching all products.
                rows = cursor.fetchall()  
                if not rows:
                    # If no products are in the database display.
                    print("No products found.")  
                    return
                print("prodID\tprodName\tprodPrice\tprodQuantity")
                for row in rows:
                    # Displaying product details.
                    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")  
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def sell_product(self, product_id, sale_date, sale_quantity):
        """Processes a product sale by reducing stock and adding a sale record."""
        try:
            with sqlite3.connect('store_database.db') as conn:
                cursor = conn.cursor()
                # Fetching product details by ID.
                cursor.execute("SELECT prodName, prodPrice, prodQuantity FROM Products WHERE prodID=?", (product_id,))
                product = cursor.fetchone()
                if not product:
                    print("Product not found.")
                    return
                product_name, product_price, current_quantity = product
                if sale_quantity <= 0:
                    # Ensuring sale quantity is positive.
                    print("Invalid sale quantity.")  
                    return
                if current_quantity < sale_quantity:
                    # Checking if stock is available.
                    print("Insufficient quantity available.")  
                    return
                new_quantity = current_quantity - sale_quantity
                # Updating product quantity in the database.
                cursor.execute("UPDATE Products SET prodQuantity=? WHERE prodID=?", (new_quantity, product_id))
                # Calculating total sale amount.
                sale_total = product_price * sale_quantity  
                # Recording the sale in the Sales table.
                cursor.execute("INSERT INTO Sales (saleDate, productName, saleTotal) VALUES (?, ?, ?)",
                               (sale_date, product_name, sale_total))
                conn.commit()
                print("Sale completed successfully.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

def main():
    """Main function to interact with the user via a menu-driven interface."""
    # Creating an instance of the Store class.
    store = Store()  
    while True:
        # Displaying menu options.
        print("\nWelcome to the Store Management System!")
        print("1. Add a product")
        print("2. Remove a product")
        print("3. Update a product")
        print("4. Display all products")
        print("5. Sell a product")
        print("6. Exit")
        choice = input("Select an option: ").strip()
        
        # Exiting option.
        if choice == '6':  
            print("Exiting the system. Goodbye!")
            break
        # Adding a product.
        elif choice == '1':  
            try:
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                store.add_product(name, price, quantity)
            # Handling invalid inputs.
            except ValueError:
                
                print("Invalid input. Please enter valid numbers.")  
        # Removing a product.
        elif choice == '2':  
            try:
                product_id = int(input("Enter ID of product to remove: "))
                store.remove_product(product_id)
            except ValueError:
                print("Invalid product ID. Please enter a number.")
        # Updating a product.
        elif choice == '3':  
            try:
                product_id = int(input("Enter ID of product to update: "))
                new_name = input("Enter new product name: ")
                new_price = float(input("Enter new product price: "))
                new_quantity = int(input("Enter new product quantity: "))
                store.update_product(product_id, new_name, new_price, new_quantity)
            except ValueError:
                print("Invalid input. Please enter valid values.")
        # Displaying all products.
        elif choice == '4':  
            store.display_products()
        # Selling a product.
        elif choice == '5':  
            try:
                product_id = int(input("Enter product ID: "))
                sale_date = input("Enter sale date (MM/DD/YYYY): ")
                sale_quantity = int(input("Enter sale quantity: "))
                store.sell_product(product_id, sale_date, sale_quantity)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        else:
            # Handling invalid menu options.
            print("Invalid option. Please select a valid option (1-6).")  

if __name__ == "__main__":
    # Running the program when executed directly.
    main()

