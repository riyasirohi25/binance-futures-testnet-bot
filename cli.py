import click

from bot.client import get_client
from bot.orders import place_order

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.logging_config import setup_logger

setup_logger()


@click.command()
@click.option("--symbol", required=True)
@click.option("--side", required=True)
@click.option("--order_type", required=True)
@click.option("--quantity", required=True, type=float)
@click.option("--price", type=float)

def main(
    symbol,
    side,
    order_type,
    quantity,
    price
):
    try:
        # Validation
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(order_type, price)

        client = get_client()

        response = place_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        print("\nOrder Request Summary")
        print("----------------------")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")

        if price:
            print(f"Price: {price}")

        print("\nOrder Response")
        print("----------------------")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print("\nSUCCESS")

    except Exception as e:
        print(f"\nERROR: {e}")


if __name__ == "__main__":
    main()