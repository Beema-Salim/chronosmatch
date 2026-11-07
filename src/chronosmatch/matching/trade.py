from dataclasses import dataclass

@dataclass(frozen=True)
class Trade:
    """Represents an executed trade between a BUY and SELL order."""

    buy_order_id: int
    sell_order_id: int
    price: float
    quantity: int

    def is_valid(self) -> bool:
        """Return whether the trade contains valid execution data."""
        return (
            self.buy_order_id > 0
            and self.sell_order_id > 0
            and self.price > 0
            and self.quantity > 0
        )