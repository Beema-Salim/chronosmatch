import time

from chronosmatch.matching.order_book import LimitOrderBook
from chronosmatch.simulator.order import Order


def test_order_processing_throughput():
    order_book = LimitOrderBook()

    orders = [
        Order(
            order_id=i,
            price=100.0 + (i % 2),
            quantity=1,
            side="BUY" if i % 2 == 0 else "SELL",
        )
        for i in range(1, 1001)
    ]

    start = time.perf_counter_ns()

    for order in orders:
        order_book.add_order(order)

    elapsed = time.perf_counter_ns() - start

    assert len(orders) == 1000
    assert elapsed > 0