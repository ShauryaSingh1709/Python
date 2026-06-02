#Make an online shopping application:
#Create a class called ShoppingCard.
#Requirements:- 
#1. class member :- Platform name
#Constructor should initialize, customer name, product list, total amount.
#Create object method ---> add product method , remove product, update product, display method
#Display the cart



class ShoppingCard:
    Platform = "Amazon"
    def __init__(self, customer_name, product_list, total_amount):
        self.customer_name = customer_name
        self.product_list = []
        self.total_amount = 0
        
    def add_product(self, product_name, price):
        self.product_list.append(product_name)
        self.total_amount += price
        print(product_name, "added succesfully")
        
    def remove_product(self, product_name, price):
        if product_name in self.product_list:
            self.product_list.remove(product_name)
            self.total_amount -= price
            print(product_name,"Removed")
        else:
            print(product_name,"Not found")
            
    def display_cart(self):
        print("Platform Name:", ShoppingCard.Platform)
        print("Customer Name:", self.customer_name)
        print("Products:", self.product_list)
        print("Amount:", self.total_amount)
        
    @classmethod
    def update_platform_name(cls, new_name):
        cls.Platform = new_name
        print("Name Updated Successfully")
        
    @staticmethod
    def shopping_rules():
        print("1. No return after 7 days")
        
s1 = ShoppingCard("Honey", [], 100000)
s1.add_product("Laptop", 50000)
s1.add_product("Mouse", 1000)
s1.add_product("Keyboard", 2000)

s1.remove_product("Mouse", 1000)

s1.display_cart()

ShoppingCard.update_platform_name("Flipkart")
ShoppingCard.shopping_rules()
s1.display_cart()