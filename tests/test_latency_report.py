from chronosmatch.metrics.statistics import calculate_latency_stats


def test_latency_report_contains_all_metrics():
    latencies = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]

    report = calculate_latency_stats(latencies)

    assert "min" in report
    assert "max" in report
    assert "mean" in report
    assert "median" in report
    assert "p95" in report
    assert "p99" in report

    print("Latency Benchmark Report")
    for metric, value in report.items():
        print(f"{metric}: {value} ns")