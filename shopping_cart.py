# Create some mock items to put in the shopping cart
stock_keeping_units = {
    "Oven": {
        "display_name": "Oven",
        "Price": 150.00,
    },
    "Microwave": {
        "display_name": "Microwave",
        "Price": 100.00
    },
    "Grill": {
        "display_name": "Grill",
        "Price": 75.00
    }
}

# Create a Cart class to keep track of items in it and perform actions on them
class Cart:

    def __init__(self):
        """
        Initiate cart with a dictionary to put references to the items in
        ex. self.items = {
            "Oven": {
                "amount": 2
                }, 
            "Grill": {
                "amount": 1
                }
            }

        """
        self.items = {}
    
    # @record_event # check if self.items changed after calling the wrapped method
    def add_item(self, item_id):
        # item_id is a product id
        # check if item already in cart and doesn't exceed 999
        if item_id in self.items:
            if self.items[item_id]["amount"] < 999:
                self.items[item_id]["amount"] += 1
            else:
                print("Can't have more than 999 of the same item")
        else:
            self.items[item_id] = {"amount": 1}

    def remove_item(self, item_id):
        # Reduces the items' amount by one if it's already in the Cart
        # Removes completely if amount is zero
        if item_id in self.items:
            if self.items[item_id]["amount"] > 1:
                self.items[item_id]["amount"] -= 1
            else:
                del self.items[item_id]

    # def set_item_amount(self, amount):
        # Sets amount of item in cart to amount (>= 1 < 999)

    def get_items(self):
        # Returns a list of items with their quantities
        item_list = []
        for item_id, value in self.items.items():
            item = stock_keeping_units[item_id]
            item["amount"] = value["amount"]
            item_list.append(item)
        return item_list

    def reset_cart(self):
        self.items = {}

# Test add 2 of the same item
cart = None
cart = Cart()
cart.add_item("Oven")
cart.add_item("Oven")
print("Should be 2 Ovens:", cart.get_items())

# Test fail if item amount is 999 and you try to add 1

# Test remove item from 1 to 0
cart = None
cart = Cart()
cart.add_item("Oven")
cart.remove_item("Oven")
print("Should be empty Cart:", cart.get_items())

# Test remove item from 3 to 2
cart = None
cart = Cart()
[cart.add_item("Oven") for x in range(3)]
cart.remove_item("Oven")
print("Should be 2 Ovens:", cart.get_items())

# Test reset cart
cart = None
cart = Cart()
[cart.add_item("Oven") for x in range(3)]
[cart.add_item("Grill") for x in range(2)]
print("Should be 3 Ovens and 2 Grills:", cart.get_items())
cart.reset_cart()
print("Should be empty:" ,cart.get_items())