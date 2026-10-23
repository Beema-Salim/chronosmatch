from chronosmatch.metrics.statistics import calculate_latency_stats


def test_latency_statistics():
    result = calculate_latency_stats([100, 200, 300, 400, 500])

    assert result["min"] == 100
    assert result["max"] == 500
    assert result["mean"] == 300
    assert result["median"] == 300


def test_empty_latency_statistics():
    result = calculate_latency_stats([])

    assert result == {
        "min": 0,
        "max": 0,
        "mean": 0,
        "median": 0,
    }