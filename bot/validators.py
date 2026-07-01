VALID_SIDES = ["BUY", "SELL"]

VALID_TYPES = [
    "MARKET",
    "LIMIT"
]

def validate_side(side):
    if side.upper() not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL")

def validate_type(order_type):
    if order_type.upper() not in VALID_TYPES:
        raise ValueError("Invalid order type")

def validate_quantity(qty):
    if float(qty) <= 0:
        raise ValueError("Quantity must be greater than zero")