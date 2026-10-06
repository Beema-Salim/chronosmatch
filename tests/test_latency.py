import time

from chronosmatch.metrics.latency import LatencyTimer


def test_latency_timer_measures_elapsed_time():
    timer = LatencyTimer()

    start = timer.start()
    time.sleep(0.001)
    elapsed = timer.stop(start)

    assert elapsed > 0
