from chronosmatch.simulator.order import Order


def test_valid_buy_order():
    order = Order(
        order_id=1,
        price=100.50,
        quantity=10,
        side="BUY",
    )

    assert order.is_valid()


def test_valid_sell_order():
    order = Order(
        order_id=2,
        price=101.00,
        quantity=5,
        side="SELL",
    )

    assert order.is_valid()