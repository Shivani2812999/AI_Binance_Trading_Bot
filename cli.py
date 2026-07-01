import argparse

from bot.orders import place_order
from bot.validators import *

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price")

args = parser.parse_args()

try:

    validate_side(args.side)
    validate_type(args.type)
    validate_quantity(args.quantity)

    if args.type.upper() == "LIMIT" and args.price is None:
        raise ValueError("Price required for LIMIT")

    response = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\n========== ORDER SUMMARY ==========")
    print(f"Symbol          : {response.get('symbol')}")
    print(f"Order ID        : {response.get('orderId')}")
    print(f"Side            : {response.get('side')}")
    print(f"Order Type      : {response.get('type')}")
    print(f"Status          : {response.get('status')}")
    print(f"Original Qty    : {response.get('origQty')}")
    print(f"Executed Qty    : {response.get('executedQty')}")
    print(f"Price           : {response.get('price')}")

    avg_price = response.get("avgPrice", "N/A")
    print(f"Average Price   : {avg_price}")

    print("\n✅ Order placed successfully!")

   

except Exception as e:

    print("Failed:", e)