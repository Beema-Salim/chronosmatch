from chronosmatch.matching.order_book import LimitOrderBook
from chronosmatch.simulator.order import Order


def test_unmatched_orders_remain_in_book():
    book = LimitOrderBook()

    buy = Order(order_id=1, price=99.0, quantity=5, side="BUY")
    sell = Order(order_id=2, price=100.0, quantity=3, side="SELL")

    book.add_order(buy)
    book.add_order(sell)

    result = book.match_with_quantity()

    assert result is None
    assert book.bid_count() == 1
    assert book.ask_count() == 1
    assert book.best_bid() == 99.0
    assert book.best_ask() == 100.0
    assert buy.quantity == 5
    assert sell.quantity == 3