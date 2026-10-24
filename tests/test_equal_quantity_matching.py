from chronosmatch.matching.order_book import LimitOrderBook
from chronosmatch.simulator.order import Order


def test_equal_quantity_orders_match_completely():
    book = LimitOrderBook()

    buy = Order(
        order_id=1, price=101.0, quantity=4, side="BUY"
    )
    sell = Order(
        order_id=2, price=100.0, quantity=4, side="SELL"
    )

    book.add_order(buy)
    book.add_order(sell)

    result = book.match_with_quantity()

    assert result is not None
    assert result[2] == 4
    assert buy.quantity == 0
    assert sell.quantity == 0
    assert book.bid_count() == 0
    assert book.ask_count() == 0