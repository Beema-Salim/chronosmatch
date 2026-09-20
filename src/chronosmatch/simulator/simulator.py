import asyncio

from .order_generator import OrderGenerator


class MarketSimulator:
    """Asynchronous market order simulator."""

    def __init__(self, order_interval: float = 0.01) -> None:
        self.order_interval = order_interval
        self.generator = OrderGenerator()

    def set_order_rate(self, orders_per_second: int) -> None:
        """Set the simulator rate using orders per second."""
        if orders_per_second <= 0:
            raise ValueError("orders_per_second must be greater than zero")

        self.order_interval = 1 / orders_per_second

    async def generate_orders(self, count: int):
        """Generate a fixed number of mock market orders."""
        for _ in range(count):
            yield self.generator.generate()
            await asyncio.sleep(self.order_interval)