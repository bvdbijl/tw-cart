from shopping_cart import Cart, STOCK_KEEPING_UNITS, DEFAULT_DISCOUNT


# Test add 2 of the same item
cart = None
cart = Cart()
cart.add_item("Oven")
cart.add_item("Oven")
print("Should be 2 Ovens:", cart.get_items())

# Test raise Exception if item amount is 999 and you try to add 1
cart = None
cart = Cart()
[cart.add_item("Oven") for x in range(999)]
try:
    cart.add_item("Oven")
except Exception as e:
    print(e)


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

# Test total order amount without discount
cart = None
cart = Cart()
[cart.add_item("Oven") for x in range(3)]
[cart.add_item("Grill") for x in range(2)]
print("Total should be 600:", cart.get_total_order_amount())

# Test total order amount with discount

cart = None
cart = Cart()
[cart.add_item("Oven") for x in range(3)]
[cart.add_item("Grill") for x in range(2)]
cart.apply_discount(DEFAULT_DISCOUNT)
print("Total should be 540:", cart.get_total_order_amount())

# Test record events

cart = None
cart = Cart()
[cart.add_item("Microwave") for x in range(2)]
cart.remove_item("Microwave")
cart.reset_cart()
print("Should have 4 events:", cart.events)