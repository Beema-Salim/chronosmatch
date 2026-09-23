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

    def best_bid_orders(self) -> list[Order]:
        """Return BUY orders at the highest bid price."""
        if not self.bids:
            return []

        return list(self.bids[self.best_bid()])
    
    def pop_best_bid_order(self) -> Order | None:
        """Remove and return the oldest BUY order at the best bid."""
        if not self.bids:
            return None

        best_price = self.best_bid()
        orders = self.bids[best_price]

        order = orders.popleft()

        if not orders:
            del self.bids[best_price]

        return order


    def best_ask(self) -> float | None:
        """Return the lowest SELL price."""
        return min(self.asks) if self.asks else None

    def best_ask_orders(self) -> list[Order]:
        """Return SELL orders at the lowest ask price."""
        if not self.asks:
            return []

        return list(self.asks[self.best_ask()])