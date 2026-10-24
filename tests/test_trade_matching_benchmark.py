import time

from chronosmatch.matching.order_book import LimitOrderBook
from chronosmatch.simulator.order import Order


def test_trade_matching_benchmark():
    order_book = LimitOrderBook()
    total_orders = 1000

    start = time.perf_counter_ns()

    for i in range(1, total_orders + 1):
        if i % 2 == 1:
            order_book.add_order(
                Order(
                    order_id=i,
                    price=100.0,
                    quantity=1,
                    side="BUY",
                )
            )
        else:
            order_book.add_order(
                Order(
                    order_id=i,
                    price=100.0,
                    quantity=1,
                    side="SELL",
                )
            )

    elapsed_ns = time.perf_counter_ns() - start

    assert elapsed_ns > 0
    assert order_book.best_bid() is None or order_book.best_bid() <= 100.0
    assert order_book.best_ask() is None or order_book.best_ask() >= 100.0

    throughput = total_orders * 1_000_000_000 / elapsed_ns

    print("\nTrade Matching Benchmark")
    print(f"Orders submitted: {total_orders}")
    print(f"Elapsed time: {elapsed_ns} ns")
    print(f"Throughput: {throughput:.2f} orders/second")