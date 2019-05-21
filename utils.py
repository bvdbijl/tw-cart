import copy
from datetime import datetime
from functools import wraps

def record_event(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cart = args[0]
        prev_items = copy.deepcopy(cart.items)
        value = func(*args, **kwargs)
        current_items = cart.items
        if prev_items != current_items:
            event = {
                "type": func.__name__,
                "args": args[1:],
                "kwargs": kwargs,
                "timestamp": datetime.now().timestamp()
            }
            cart.events.append(event)
        return value
    return wrapper
