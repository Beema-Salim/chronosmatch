from collections import defaultdict, deque

from chronosmatch.simulator.order import Order


class LimitOrderBook:
    """Basic price-level order book for BUY and SELL orders."""

    def __init__(self) -> None:
        self.bids = defaultdict(deque)
        self.asks = defaultdict(deque)

    def add_order(self, order: Order) -> None:
        """Add a valid order to the appropriate price level."""
        if not order.is_valid():
            raise ValueError("Invalid order")

        if order.side == "BUY":
            self.bids[order.price].append(order)
        else:
            self.asks[order.price].append(order)

    def bid_count(self) -> int:
        """Return the total number of BUY orders."""
        return sum(len(orders) for orders in self.bids.values())

    def ask_count(self) -> int:
        """Return the total number of SELL orders."""
        return sum(len(orders) for orders in self.asks.values())

    def best_bid(self) -> float | None:
        """Return the highest BUY price."""
        return max(self.bids) if self.bids else None

    def best_ask(self) -> float | None:
        """Return the lowest SELL price."""
        return min(self.asks) if self.asks else None