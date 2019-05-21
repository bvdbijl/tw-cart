import copy
from datetime import datetime
from functools import wraps

def record_event(func):
    # Logs the event if the Carts' items are mutated

    # Use functools.wraps to extract the correct method name for logging
    @wraps(func)
    def wrapper(*args, **kwargs):

        # the Cart instance (self) is passed as first argument to the method
        cart = args[0]

        # Use deepcopy because otherwise it's just the reference and we'll not be able to detect changes
        prev_items = copy.deepcopy(cart.items)

        # Run the wrapped method
        value = func(*args, **kwargs)

        current_items = cart.items

        if prev_items != current_items:
            event = {
                "type": func.__name__,
                "args": args[1:], # Weed out the Cart instance object
                "kwargs": kwargs,
                "timestamp": datetime.now().timestamp()
            }
            cart.events.append(event)
        return value
    return wrapper
