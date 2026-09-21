from pathlib import Path

from chronosmatch.simulator.order import Order

from .mmap_buffer import MMapBuffer
from .serializer import OrderSerializer


class MMapOrderChannel:
    """Store serialized orders inside a memory-mapped buffer."""

    def __init__(
        self,
        file_path: str | Path,
        capacity: int = 100,
    ) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be greater than zero")

        self.capacity = capacity
        self._buffer = MMapBuffer(
            file_path,
            size=capacity * OrderSerializer.SIZE,
        )

    def write(self, order: Order, index: int = 0) -> None:
        """Serialize and write an order at a fixed slot."""
        if index < 0 or index >= self.capacity:
            raise IndexError("Order index is outside channel capacity")

        data = OrderSerializer.serialize(order)
        offset = index * OrderSerializer.SIZE

        self._buffer.write(data, offset=offset)

    def read(self, index: int = 0) -> Order:
        """Read and deserialize an order from a fixed slot."""
        if index < 0 or index >= self.capacity:
            raise IndexError("Order index is outside channel capacity")

        offset = index * OrderSerializer.SIZE

        data = self._buffer.read(
            OrderSerializer.SIZE,
            offset=offset,
        )

        return OrderSerializer.deserialize(data)

    def close(self) -> None:
        """Close the underlying memory-mapped buffer."""
        self._buffer.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()