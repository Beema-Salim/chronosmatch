import asyncio

from .order_generator import OrderGenerator


class MarketSimulator:
    """Asynchronous market order simulator."""

    def __init__(self, order_interval: float = 0.01) -> None:
        self.order_interval = order_interval
        self.generator = OrderGenerator()

    async def generate_orders(self, count: int):
        """Generate a fixed number of mock market orders."""
        for _ in range(count):
            yield self.generator.generate()
            await asyncio.sleep(self.order_interval)