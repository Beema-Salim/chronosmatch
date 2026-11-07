from chronosmatch.matching.order_book import LimitOrderBook
from chronosmatch.simulator.order import Order


def test_smaller_buy_quantity_leaves_sell_remainder():
    book = LimitOrderBook()

    buy = Order(
        order_id=1, price=101.0, quantity=2, side="BUY"
    )
    sell = Order(
        order_id=2, price=100.0, quantity=5, side="SELL"
    )

    book.add_order(buy)
    book.add_order(sell)

    result = book.match_with_quantity()

    assert result is not None
    assert result[2] == 2
    assert buy.quantity == 0
    assert sell.quantity == 3
    assert book.bid_count() == 0
    assert book.ask_count() == 1