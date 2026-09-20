from collections import deque

from chronosmatch.simulator.order import Order


class OrderBuffer:
    """Simple order buffer for simulator-to-engine integration."""

    def __init__(self) -> None:
        self._orders = deque()

    def write(self, order: Order) -> None:
        """Add an order to the buffer."""
        if not order.is_valid():
            raise ValueError("Invalid order")

        self._orders.append(order)

    def read(self) -> Order | None:
        """Read the next available order."""
        if not self._orders:
            return None

        return self._orders.popleft()

    def size(self) -> int:
        """Return the number of orders waiting in the buffer."""
        return len(self._orders)