#Question 1

"""class BudgetCalculator:
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

    def calculate_expenses(self):
        self.expenses['Utilities'] = self.after_tax_income * 0.05
        self.expenses['Rent'] = self.after_tax_income * 0.15
        self.expenses['Transport'] = self.after_tax_income * 0.30
        self.expenses['Health'] = self.after_tax_income * 0.03
        self.expenses['Groceries'] = self.after_tax_income * 0.10
        self.expenses['Communication'] = self.after_tax_income * 0.02
        self.total_expenses = sum(self.expenses.values())
        self.net_income = self.after_tax_income - self.total_expenses

    def display_budget(self):
        print("\nMonthly Budget\n")
        print("Income\n")
        print(f"Gross Monthly Income (Before Tax): R{self.gross_income:.2f}")
        print(f"Gross Monthly Income (After Tax): R{self.after_tax_income:.2f}\n")
        print("Expenses\n")
        for category, amount in self.expenses.items():
            print(f"{category}: R{amount:.2f}")
        print(f"\nTotal Expenses: R{self.total_expenses:.2f}")
        print(f"\nNet Income: R{self.net_income:.2f}\n")

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
                    print("Income cannot be negative. Please try again.\n")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
                continue
            budget = BudgetCalculator(user_code, gross_income)
            budget.calculate_tax()
            budget.calculate_expenses()
            budget.display_budget()
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()"""


#Question 2

import sqlite3

class Store:
    def __init__(self):
        self.initialize_database()

    def initialize_database(self):
        conn = sqlite3.connect('store_database.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Products
                         (prodID INTEGER PRIMARY KEY AUTOINCREMENT,
                          prodName TEXT,
                          prodPrice REAL,
                          prodQuantity INTEGER)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS Sales
                         (saleID INTEGER PRIMARY KEY AUTOINCREMENT,
                          saleDate TEXT,
                          productName TEXT,
                          saleTotal REAL)''')
        conn.commit()
        conn.close()

    def add_product(self, name, price, quantity):
        with sqlite3.connect('store_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Products (prodName, prodPrice, prodQuantity) VALUES (?, ?, ?)",
                           (name, price, quantity))
            conn.commit()
            print("Product added successfully.")

    def remove_product(self, product_id):
        with sqlite3.connect('store_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Products WHERE prodID=?", (product_id,))
            conn.commit()
            if cursor.rowcount == 0:
                print("Product not found.")
            else:
                print("Data deleted successfully.")

    def update_product(self, product_id, new_name, new_price, new_quantity):
        with sqlite3.connect('store_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Products SET prodName=?, prodPrice=?, prodQuantity=? WHERE prodID=?",
                           (new_name, new_price, new_quantity, product_id))
            conn.commit()
            if cursor.rowcount == 0:
                print("Product not found.")
            else:
                print("Data updated successfully.")

    def display_products(self):
        with sqlite3.connect('store_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Products")
            rows = cursor.fetchall()
            if not rows:
                print("No products found.")
                return
            print("prodID\tprodName\tprodPrice\tprodQuantity")
            for row in rows:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")

    def sell_product(self, product_id, sale_date, sale_quantity):
        with sqlite3.connect('store_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT prodName, prodPrice, prodQuantity FROM Products WHERE prodID=?", (product_id,))
            product = cursor.fetchone()
            if not product:
                print("Product not found.")
                return
            product_name, product_price, current_quantity = product
            if current_quantity < sale_quantity:
                print("Insufficient quantity available.")
                return
            if sale_quantity <= 0:
                print("Invalid sale quantity.")
                return
            new_quantity = current_quantity - sale_quantity
            cursor.execute("UPDATE Products SET prodQuantity=? WHERE prodID=?", (new_quantity, product_id))
            sale_total = product_price * sale_quantity
            cursor.execute("INSERT INTO Sales (saleDate, productName, saleTotal) VALUES (?, ?, ?)",
                           (sale_date, product_name, sale_total))
            conn.commit()
            print("Sale completed successfully.")

def main():
    store = Store()
    while True:
        print("\nWelcome to the Store Management System!")
        print("1. Add a product")
        print("2. Remove a product")
        print("3. Update a product")
        print("4. Display all products")
        print("5. Sell a product")
        print("6. Exit")
        choice = input("Select an option: ").strip()
        
        if choice == '6':
            print("Exiting the system. Goodbye!")
            break
        elif choice == '1':
            try:
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                store.add_product(name, price, quantity)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        elif choice == '2':
            try:
                product_id = int(input("Enter ID of product to remove: "))
                store.remove_product(product_id)
            except ValueError:
                print("Invalid product ID. Please enter a number.")
        elif choice == '3':
            try:
                product_id = int(input("Enter ID of product to update: "))
                new_name = input("Enter new product name: ")
                new_price = float(input("Enter new product price: "))
                new_quantity = int(input("Enter new product quantity: "))
                store.update_product(product_id, new_name, new_price, new_quantity)
            except ValueError:
                print("Invalid input. Please enter valid values.")
        elif choice == '4':
            store.display_products()
        elif choice == '5':
            try:
                product_id = int(input("Enter product ID: "))
                sale_date = input("Enter sale date (MM/DD/YYYY): ")
                sale_quantity = int(input("Enter sale quantity: "))
                store.sell_product(product_id, sale_date, sale_quantity)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        else:
            print("Invalid option. Please select a valid option (1-6).")

if __name__ == "__main__":
    main()


#This has to be done using the real SQL Database and I am exited. 

#This will be tackeled tommorw though. Tomorrow is the the best and most productie dat ever, I swear.


#Monday [18:03]
#10 March 2025

#Note taking 
#I will be required to use the real version of SQL and not the imported version.

#I am going to have to create a database and connect to it using "mysql.connector".

#After connecting to the database that is when I will have the privilege of creating tables and manipulating them how I see fit.

#My project requires this way of answering the second question and not use the method stipulated in the book.

#Basically I am done with this project, I just need to complete everything by tomorrow.   