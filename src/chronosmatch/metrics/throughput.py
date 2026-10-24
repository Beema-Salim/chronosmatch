def calculate_throughput(
    processed_orders: int,
    elapsed_ns: int,
) -> float:
    """Calculate orders processed per second."""
    if processed_orders < 0:
        raise ValueError("Processed orders cannot be negative.")

    if elapsed_ns <= 0:
        raise ValueError("Elapsed time must be positive.")

    return processed_orders * 1_000_000_000 / elapsed_ns