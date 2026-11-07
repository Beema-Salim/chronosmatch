from chronosmatch.matching.order_book import LimitOrderBook
from chronosmatch.simulator.order import Order


def test_orders_match_when_prices_are_equal():
    book = LimitOrderBook()

    buy = Order(
        order_id=1, price=100.0, quantity=3, side="BUY"
    )
    sell = Order(
        order_id=2, price=100.0, quantity=3, side="SELL"
    )

    book.add_order(buy)
    book.add_order(sell)

    result = book.match_with_quantity()

    assert result is not None
    assert result[2] == 3
    assert buy.quantity == 0
    assert sell.quantity == 0
    assert book.bid_count() == 0
    assert book.ask_count() == 0