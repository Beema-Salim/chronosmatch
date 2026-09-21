from collections import deque

from chronosmatch.simulator.order import Order


class OrderBuffer:
    """Simple order buffer for simulator-to-engine integration."""

    def __init__(self, max_size: int = 1000) -> None:
        if max_size <= 0:
            raise ValueError("max_size must be greater than zero")

        self._orders = deque()
        self.max_size = max_size

    def write(self, order: Order) -> None:
        """Add a valid order to the buffer."""
        if not order.is_valid():
            raise ValueError("Invalid order")

        if self.is_full():
            raise BufferError("Order buffer is full")

        self._orders.append(order)

    def read(self) -> Order | None:
        """Read the next available order."""
        if not self._orders:
            return None

        return self._orders.popleft()

    def size(self) -> int:
        """Return the number of orders waiting in the buffer."""
        return len(self._orders)

    def is_full(self) -> bool:
        """Return whether the buffer has reached its maximum size."""
        return self.size() >= self.max_size