from bot.client import client
from bot.logging_config import logger
import time


def place_order(symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity,
        }

        if order_type.upper() == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Request: {params}")

        # Place the order
        response = client.futures_create_order(**params)

        logger.info(f"Initial Response: {response}")

        # Wait briefly for Binance to process it
        time.sleep(1)

        # Fetch the latest order status
        latest_order = client.futures_get_order(
            symbol=symbol.upper(),
            orderId=response["orderId"]
        )

        logger.info(f"Latest Response: {latest_order}")

        return latest_order

    except Exception as e:
        logger.exception(e)
        raise