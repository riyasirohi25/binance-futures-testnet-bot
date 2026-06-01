import logging

def place_order(
    client,
    symbol,
    side,
    order_type,
    quantity,
    price=None
):

    try:

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":

            if price is None:
                raise ValueError(
                    "Price required for LIMIT order"
                )

            params["price"] = price
            params["timeInForce"] = "GTC"

        logging.info(f"REQUEST: {params}")

        response = client.futures_create_order(
            **params
        )

        logging.info(
            f"RESPONSE: {response}"
        )

        return response

    except Exception as e:

        logging.error(str(e))
        raise