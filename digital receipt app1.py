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





