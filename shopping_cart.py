from utils import record_event

# Create some mock items to put in the shopping cart
STOCK_KEEPING_UNITS = {
    "Oven": {
        "display_name": "Oven",
        "price": 150.00,
    },
    "Microwave": {
        "display_name": "Microwave",
        "price": 100.00
    },
    "Grill": {
        "display_name": "Grill",
        "price": 75.00
    }
}
DEFAULT_DISCOUNT = 0.10

# Create a Cart class to keep track of current items in the cart and perform actions on it
class Cart:

    def __init__(self):
        """
        Initiate cart with a dictionary to put references to the items in
        ex. self.items = {
            "Oven": {"amount": 2}, 
            "Grill": {"amount": 1}
            }

        """
        self.items = {}
        self.discount = None
        self.events = []
    
    @record_event
    def add_item(self, item_id):
        # Adds the item to the cart if qunatity is below 999

        if item_id in self.items:
            if self.items[item_id]["amount"] < 999:
                self.items[item_id]["amount"] += 1
            else:
                raise Exception("Can't have more than 999 of the same item")
        else:
            self.items[item_id] = {"amount": 1}

    @record_event
    def remove_item(self, item_id):
        # Reduces the items' amount by one if it's already in the Cart
        # Removes completely if amount is zero

        if item_id in self.items:
            if self.items[item_id]["amount"] > 1:
                self.items[item_id]["amount"] -= 1
            else:
                del self.items[item_id]

    # @record_event
    # def set_item_amount(self, amount):
        # Sets amount of item in cart to amount (>= 1 < 999)

    def get_items(self):
        # Returns a list of items with their quantities and other data

        item_list = []
        for item_id, value in self.items.items():
            item = STOCK_KEEPING_UNITS[item_id]
            item["amount"] = value["amount"]
            item_list.append(item)
        return item_list

    @record_event
    def reset_cart(self):
        self.items = {}

    def apply_discount(self, discount):
        self.discount = discount

    def get_total_order_amount(self):
        total = sum([i["price"] * i["amount"] for i in self.get_items()])
        if self.discount is not None:
            total = total - self.discount * total
        return total