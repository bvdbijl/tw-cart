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

    def get_items(self):
        # Returns a list of items with their quantities
        item_list = []
        for key, v in self.items.items():
            i = stock_keeping_units[key]
            i["amount"] = v["amount"]
            item_list.append(i)
        return item_list

cart = Cart()
cart.add_item("Oven")
cart.add_item("Oven")
print(cart.get_items())
cart = None
cart = Cart()
print(cart.items)