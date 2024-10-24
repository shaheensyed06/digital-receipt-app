class Receiptapp:
    def __init__(self):
        self.items=[]
    def show_menu(self):
        print("1.Add item")
        print("2.View Receipt")
        print("3.calculator total")
        print("4.exit")
        print("-----------------------------")
    def add_item(self):
        item_name=input("enter the item name:")
        while True:
            try:
                item_price=float(input(f"enter the price of'{item_name}':"))
                break
            except valueError:
                print("please enter avalid price.")
        self.items.append({"name":item_name,"price":item_price})
        print(f"'{item_name}'added to the receipt.\n")
    
    def view_receipt(self):
        if not self.items:
            print("\n The receipt is empty.")
        else:
            print("\n----Recepit ----")
            for idx,item in enumerate(self.items,start=1):
                print(f"{idx}.{item['name']}:${item['price']:.2f}")
            print("-----------------------\n")
    def calculate_total(self):
         if not self.items:
              print("The receipt is empty,no total to calculate.")
         else:
             total=sum(item["price"] for item in self.items)
             print(f"\nTotal amount:${total:.2f}\n")
    def run(self):
        while True:
            self.show_menu()
            choice=input("Enter your choice(1-4):")
            if choice=='1':
                self.add_item()
            elif choice=='2':
                self.view_receipt()
            elif choice=='3':
                self.calculate_total()
            elif choice=='4':
                print("Exiting the app. Thank you!")
                break
            else:
                print("Invalid choice,Please try again.\n")
if __name__=="__main__":
    app=Receiptapp()
    app.run()





'''Certainly! Let me explain the code step by step:

Code Overview
This code defines a class Receiptapp which simulates a simple receipt app. The app allows users to:

Add items (with their name and price).
View the receipt (list of items with their prices).
Calculate the total of all items in the receipt.
Exit the app.
Class: Receiptapp
This class encapsulates the entire functionality of the receipt app. Let's go through its components:

__init__(self)
python
Copy code
def __init__(self):
    self.items = []
Purpose: Initializes the Receiptapp instance.
Explanation:
self.items: A list that will store the items added to the receipt. Each item will be represented as a dictionary with keys "name" (item name) and "price" (item price).
show_menu(self)
python
Copy code
def show_menu(self):
    print("1.Add item")
    print("2.View Receipt")
    print("3.calculator total")
    print("4.exit")
    print("-----------------------------")
Purpose: Displays the main menu options of the app.
Explanation: This method prints the options the user can choose from. It prints 4 options:
Add an item.
View the receipt (list of items).
Calculate the total.
Exit the app.
add_item(self)
python
Copy code
def add_item(self):
    item_name = input("enter the item name:")
    while True:
        try:
            item_price = float(input(f"enter the price of'{item_name}':"))
            break
        except ValueError:
            print("please enter a valid price.")
    self.items.append({"name": item_name, "price": item_price})
    print(f"'{item_name}' added to the receipt.\n")
Purpose: Adds a new item (with its name and price) to the receipt.
Explanation:
It prompts the user to enter an item_name.
Then, it asks for the item_price in a while loop. The loop ensures that the price entered is valid (a float). If the input isn't a valid float, an exception (ValueError) is raised and the user is prompted to enter the price again.
After a valid price is entered, the item (with its name and price) is added to the self.items list as a dictionary.
The program then prints a confirmation message that the item has been added.
view_receipt(self)
python
Copy code
def view_receipt(self):
    if not self.items:
        print("\n The receipt is empty.")
    else:
        print("\n----Receipt ----")
        for idx, item in enumerate(self.items, start=1):
            print(f"{idx}.{item['name']}:${item['price']:.2f}")
        print("-----------------------\n")
Purpose: Displays all the items in the receipt (name and price).
Explanation:
If the receipt is empty (i.e., no items have been added), the program prints "The receipt is empty.".
Otherwise, it prints each item in the self.items list in a formatted way. It uses enumerate() to get both the index (idx) and the item dictionary. start=1 ensures the item list starts from 1 (not 0).
The item['name'] accesses the item's name, and item['price']:.2f ensures that the price is formatted to two decimal places.
calculate_total(self)
python
Copy code
def calculate_total(self):
    if not self.items:
        print("The receipt is empty, no total to calculate.")
    else:
        total = sum(item["price"] for item in self.items)
        print(f"\nTotal amount: ${total:.2f}\n")
Purpose: Calculates and displays the total price of all items on the receipt.
Explanation:
If the receipt is empty, the method prints that there is no total to calculate.
If there are items in the receipt, it calculates the total by summing the price of each item in the self.items list using a generator expression.
The :.2f ensures the total is formatted with two decimal places.
run(self)
python
Copy code
def run(self):
    while True:
        self.show_menu()
        choice = input("Enter your choice(1-4):")
        if choice == '1':
            self.add_item()
        elif choice == '2':
            self.view_receipt()
        elif choice == '3':
            self.calculate_total()
        elif choice == '4':
            print("Exiting the app. Thank you!")
            break
        else:
            print("Invalid choice, please try again.\n")
Purpose: Main loop of the application that repeatedly displays the menu and handles user input.
Explanation:
The while True: loop keeps the app running until the user chooses to exit (option 4).
The show_menu() method is called to display the options.
Based on the user's choice (choice), the corresponding method is called:
If the user selects '1', add_item() is called to add an item.
If the user selects '2', view_receipt() is called to display the receipt.
If the user selects '3', calculate_total() is called to compute and display the total price.
If the user selects '4', the app prints a farewell message and breaks out of the loop, terminating the program.
If the user enters an invalid choice, an error message is displayed and the loop continues.
Code Execution
python
Copy code
if __name__ == "__main__":
    app = Receiptapp()
    app.run()
Purpose: This block is executed when the script is run directly (i.e., not imported as a module).
Explanation:
app = Receiptapp() creates an instance of the Receiptapp class.
app.run() starts the main loop of the application.
Fixes
There is a small typo in your code that will cause an error:

python
Copy code
except valueError:
Should be:

python
Copy code
except ValueError:
ValueError should be capitalized.

Example Run
Here’s an example interaction with the app:

markdown
Copy code
1.Add item
2.View Receipt
3.calculator total
4.exit
-----------------------------
Enter your choice(1-4): 1
enter the item name: Apple
enter the price of 'Apple': 1.50
'Apple' added to the receipt.

1.Add item
2.View Receipt
3.calculator total
4.exit
-----------------------------
Enter your choice(1-4): 2

----Receipt ----
1.Apple:$1.50
-----------------------

1.Add item
2.View Receipt
3.calculator total
4.exit
-----------------------------
Enter your choice(1-4): 3

Total amount:$1.50

1.Add item
2.View Receipt
3.calculator total
4.exit
-----------------------------
Enter your choice(1-4): 4
Exiting the app. Thank you!
Summary
This class simulates a simple receipt system where items can be added, viewed, and the total can be calculated. The app keeps running in a loop until the user chooses to exit. Each of the methods is well-defined and does specific tasks such as adding items, viewing the receipt, and calculating the total price.

Let me know if anything is unclear or if you need further clarification!'''






