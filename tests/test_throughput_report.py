import time

from chronosmatch.metrics.throughput import calculate_throughput


def test_throughput_benchmark_report():
    total_orders = 1000

    start = time.perf_counter_ns()

    # Simulate processing a simple batch of orders.
    processed_orders = sum(1 for _ in range(total_orders))

    elapsed_ns = time.perf_counter_ns() - start
    throughput = calculate_throughput(processed_orders, elapsed_ns)

    assert processed_orders == total_orders
    assert elapsed_ns > 0
    assert throughput > 0

    print("\nThroughput Benchmark Report")
    print(f"Orders processed: {processed_orders}")
    print(f"Elapsed time: {elapsed_ns} ns")
    print(f"Throughput: {throughput:.2f} orders/second")