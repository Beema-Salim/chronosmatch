import asyncio
import logging

from .order_generator import OrderGenerator


logger = logging.getLogger(__name__)


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
            order = self.generator.generate()
            logger.info(
                "Generated order: id=%s side=%s price=%.2f quantity=%s",
                order.order_id,
                order.side,
                order.price,
                order.quantity,
            )
            yield order
            await asyncio.sleep(self.order_interval)