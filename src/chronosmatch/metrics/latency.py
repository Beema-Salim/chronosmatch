import time


class LatencyTimer:
    """Measure operation latency in nanoseconds."""

    def start(self) -> int:
        return time.perf_counter_ns()

    def stop(self, start_time: int) -> int:
        return time.perf_counter_ns() - start_time
