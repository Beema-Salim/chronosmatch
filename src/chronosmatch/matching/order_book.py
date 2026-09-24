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

    def match_orders(self) -> tuple[Order, Order] | None:
        """Match the best BUY and SELL orders when prices cross."""
        if not self.bids or not self.asks:
            return None

        best_bid = self.best_bid()
        best_ask = self.best_ask()

        if best_bid < best_ask:
            return None

        buy_order = self.pop_best_bid_order()

        sell_orders = self.asks[best_ask]
        sell_order = sell_orders.popleft()

        if not sell_orders:
            del self.asks[best_ask]

        return buy_order, sell_order

    def match_with_quantity(self) -> tuple[Order, Order, int] | None:
        """Match the best BUY and SELL orders and return traded quantity."""
        if not self.bids or not self.asks:
            return None

        best_bid = self.best_bid()
        best_ask = self.best_ask()

        if best_bid < best_ask:
            return None

        buy_order = self.bids[best_bid][0]
        sell_order = self.asks[best_ask][0]

        traded_quantity = min(
            buy_order.quantity,
            sell_order.quantity,
        )

        buy_order.quantity -= traded_quantity
        sell_order.quantity -= traded_quantity

        if buy_order.quantity == 0:
            self.bids[best_bid].popleft()

            if not self.bids[best_bid]:
                del self.bids[best_bid]

        if sell_order.quantity == 0:
            self.asks[best_ask].popleft()

            if not self.asks[best_ask]:
                del self.asks[best_ask]

        return buy_order, sell_order, traded_quantity
    
    def best_ask(self) -> float | None:
        """Return the lowest SELL price."""
        return min(self.asks) if self.asks else None

    def best_ask_orders(self) -> list[Order]:
        """Return SELL orders at the lowest ask price."""
        if not self.asks:
            return []

        return list(self.asks[self.best_ask()])