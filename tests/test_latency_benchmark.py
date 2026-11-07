from chronosmatch.metrics.latency import LatencyTimer


def test_order_processing_latency():
    timer = LatencyTimer()

    start = timer.start()

    total = sum(range(100))

    elapsed = timer.stop(start)

    assert total == 4950
    assert elapsed > 0