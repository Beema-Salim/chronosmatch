from statistics import mean, median


def calculate_latency_stats(latencies: list[int]) -> dict[str, float]:
    """Calculate basic latency statistics in nanoseconds."""
    if not latencies:
        return {
            "min": 0,
            "max": 0,
            "mean": 0,
            "median": 0,
        }

    return {
        "min": min(latencies),
        "max": max(latencies),
        "mean": mean(latencies),
        "median": median(latencies),
    }