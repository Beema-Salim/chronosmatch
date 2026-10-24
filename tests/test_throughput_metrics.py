import pytest

from chronosmatch.metrics.throughput import calculate_throughput


def test_calculate_throughput():
    result = calculate_throughput(1000, 1_000_000_000)
    assert result == 1000.0


def test_zero_processed_orders():
    result = calculate_throughput(0, 1_000_000_000)
    assert result == 0.0


def test_negative_processed_orders():
    with pytest.raises(ValueError):
        calculate_throughput(-1, 1_000_000_000)


def test_zero_elapsed_time():
    with pytest.raises(ValueError):
        calculate_throughput(100, 0)