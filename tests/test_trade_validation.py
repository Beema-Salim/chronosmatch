from chronosmatch.matching.order_book import LimitOrderBook
from chronosmatch.simulator.order import Order


def test_matching_executes_trade():
    book = LimitOrderBook()

    buy = Order(order_id=1, price=101.0, quantity=5, side="BUY")
    sell = Order(order_id=2, price=100.0, quantity=3, side="SELL")

    book.add_order(buy)
    book.add_order(sell)

    result = book.match_with_quantity()

    assert result is not None

    matched_buy, matched_sell, traded_quantity = result

    assert matched_buy.order_id == 1
    assert matched_sell.order_id == 2
    assert traded_quantity == 3
    assert buy.quantity == 2
    assert sell.quantity == 0
    assert book.bid_count() == 1
    assert book.ask_count() == 0


def test_orders_do_not_match_when_prices_do_not_cross():
    book = LimitOrderBook()

    book.add_order(
        Order(order_id=1, price=99.0, quantity=5, side="BUY")
    )
    book.add_order(
        Order(order_id=2, price=100.0, quantity=5, side="SELL")
    )

    assert book.match_with_quantity() is None
    assert book.bid_count() == 1
    assert book.ask_count() == 1