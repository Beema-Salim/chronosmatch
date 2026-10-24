from chronosmatch.matching.order_book import LimitOrderBook
from chronosmatch.simulator.order import Order


def test_multiple_orders_match_in_price_priority():
    book = LimitOrderBook()

    book.add_order(
        Order(order_id=1, price=100.0, quantity=2, side="BUY")
    )
    book.add_order(
        Order(order_id=2, price=101.0, quantity=3, side="BUY")
    )
    book.add_order(
        Order(order_id=3, price=99.0, quantity=2, side="SELL")
    )

    result = book.match_with_quantity()

    assert result is not None
    matched_buy, matched_sell, traded_quantity = result

    assert matched_buy.order_id == 2
    assert matched_sell.order_id == 3
    assert traded_quantity == 2
    assert matched_buy.quantity == 1
    assert matched_sell.quantity == 0