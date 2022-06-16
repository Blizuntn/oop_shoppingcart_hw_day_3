class ShoppingCart:
    
    def __init__(self) -> None:
        self.shopping_cart = []


    def add_items(self):
        self.item = input("What do you want to add to your shopping cart? ")
        self.shopping_cart.append(self.item)


    def remove_items(self):
        self.item = input("What would you like to remove from your shopping cart? ")
        self.shopping_cart.remove(self.item)


    def view_items(self):
        if len(self.shopping_cart) < 1:
            print("There is nothing in your cart. What are you waiting for? You can have anything you want.")
        else:
            print(self.shopping_cart)


    def show_instructions(self):
        print("""
        Welcome to the best shopping cart
        Below are some instructions to help you navigate through the entire process.
    
            To add items to your cart: type add
          
            To remove items from your cart: type remove
          
            To take a look at your inventory: type view
          
            To stop shopping: type no
        """)

cart1 = ShoppingCart()

shopping_is_on = True
cart1.show_instructions()

while shopping_is_on:
    should_continue = input("Do you want to shop: yes or no? ")
    if should_continue == "no":
        break
    user_input = input("What would u like to do with your shopping cart? add, remove, or view?  ")
    if user_input == "add":
        cart1.add_items()
    elif user_input == "remove":
        cart1.remove_items()
    elif user_input == "view":
        cart1.view_items()
    else:
        print("I am sorry but that is not one of the selections please enter the right word to continue shopping.")
