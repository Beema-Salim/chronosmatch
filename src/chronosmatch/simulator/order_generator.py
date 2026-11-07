import random

from .order import Order


class OrderGenerator:
    """Generates mock BUY and SELL market orders."""

    def __init__(self, start_order_id: int = 1) -> None:
        self._next_order_id = start_order_id

    def generate(self, side: str | None = None) -> Order:
        if side is None:
            side = random.choice(["BUY", "SELL"])

        order = Order(
            order_id=self._next_order_id,
            price=round(random.uniform(99.0, 101.0), 2),
            quantity=random.randint(1, 100),
            side=side,
        )

        self._next_order_id += 1
        return order