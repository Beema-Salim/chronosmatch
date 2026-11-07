import time

from chronosmatch.matching.order_book import LimitOrderBook
from chronosmatch.simulator.order import Order


def test_matching_engine_benchmark():
    order_book = LimitOrderBook()

    orders = [
        Order(
            order_id=i,
            price=100.0 + (i % 10),
            quantity=1,
            side="BUY" if i % 2 == 0 else "SELL",
        )
        for i in range(1, 1001)
    ]

    start = time.perf_counter_ns()

    for order in orders:
        order_book.add_order(order)

    elapsed_ns = time.perf_counter_ns() - start

    assert elapsed_ns > 0
    assert len(orders) == 1000

    throughput = len(orders) * 1_000_000_000 / elapsed_ns

    print("\nOrder Book Benchmark")
    print(f"Orders submitted: {len(orders)}")
    print(f"Elapsed time: {elapsed_ns} ns")
    print(f"Throughput: {throughput:.2f} orders/second")