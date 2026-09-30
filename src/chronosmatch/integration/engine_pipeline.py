from chronosmatch.dashboard.curses_dashboard import CursesDashboard
from chronosmatch.integration.ipc import OrderBuffer
from chronosmatch.matching.order_book import LimitOrderBook
from chronosmatch.simulator.order import Order


class EnginePipeline:
    """Connect the order buffer, matching engine, and dashboard."""

    def __init__(self) -> None:
        self.buffer = OrderBuffer()
        self.order_book = LimitOrderBook()
        self.dashboard = CursesDashboard()

    def submit_order(self, order: Order) -> None:
        """Submit an order to the IPC buffer."""
        self.buffer.write(order)

    def process_next_order(self) -> bool:
        """Move one buffered order into the matching engine."""
        order = self.buffer.read()

        if order is None:
            return False

        self.order_book.add_order(order)
        self.dashboard.record_order()

        match = self.order_book.match_with_quantity()

        if match is not None:
            self.dashboard.record_trade()

        self.dashboard.update_market(
            self.order_book.best_bid(),
            self.order_book.best_ask(),
        )

        return True