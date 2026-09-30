from chronosmatch.integration.engine_pipeline import EnginePipeline
from chronosmatch.simulator.order import Order


def test_week2_order_to_trade_pipeline():
    pipeline = EnginePipeline()

    buy_order = Order(
        order_id=1,
        price=101.00,
        quantity=10,
        side="BUY",
    )
    sell_order = Order(
        order_id=2,
        price=100.00,
        quantity=10,
        side="SELL",
    )

    pipeline.submit_order(buy_order)
    pipeline.submit_order(sell_order)

    assert pipeline.process_next_order()
    assert pipeline.process_next_order()

    assert pipeline.dashboard.orders_processed == 2
    assert pipeline.dashboard.trades_executed == 1
    assert pipeline.dashboard.best_bid is None
    assert pipeline.dashboard.best_ask is None


def test_week2_partial_match_updates_dashboard():
    pipeline = EnginePipeline()

    buy_order = Order(
        order_id=1,
        price=101.00,
        quantity=10,
        side="BUY",
    )
    sell_order = Order(
        order_id=2,
        price=100.00,
        quantity=4,
        side="SELL",
    )

    pipeline.submit_order(buy_order)
    pipeline.submit_order(sell_order)

    pipeline.process_next_order()
    pipeline.process_next_order()

    assert pipeline.dashboard.orders_processed == 2
    assert pipeline.dashboard.trades_executed == 1
    assert pipeline.dashboard.best_bid == 101.00
    assert pipeline.dashboard.best_ask is None