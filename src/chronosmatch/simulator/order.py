from dataclasses import dataclass
from typing import Literal


OrderSide = Literal["BUY", "SELL"]


@dataclass
class Order:
    order_id: int
    price: float
    quantity: int
    side: OrderSide

    def is_valid(self) -> bool:
        return (
            self.order_id > 0
            and self.price > 0
            and self.quantity > 0
            and self.side in ("BUY", "SELL")
        )