from statistics import mean, median


def calculate_latency_stats(latencies: list[int]) -> dict[str, float]:
    """Calculate latency statistics in nanoseconds."""
    if not latencies:
        return {
            "min": 0,
            "max": 0,
            "mean": 0,
            "median": 0,
            "p95": 0,
            "p99": 0,
        }

    ordered = sorted(latencies)

    def percentile(p: float) -> int:
        index = max(0, int((p / 100) * len(ordered) + 0.999999) - 1)
        return ordered[min(index, len(ordered) - 1)]

    return {
        "min": min(ordered),
        "max": max(ordered),
        "mean": mean(ordered),
        "median": median(ordered),
        "p95": percentile(95),
        "p99": percentile(99),
    }