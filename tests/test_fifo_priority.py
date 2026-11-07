from chronosmatch.matching.order_book import LimitOrderBook
from chronosmatch.simulator.order import Order


def test_same_price_orders_follow_fifo_priority():
    book = LimitOrderBook()

    first_buy = Order(
        order_id=1, price=101.0, quantity=2, side="BUY"
    )
    second_buy = Order(
        order_id=2, price=101.0, quantity=3, side="BUY"
    )
    sell = Order(
        order_id=3, price=100.0, quantity=2, side="SELL"
    )

    book.add_order(first_buy)
    book.add_order(second_buy)
    book.add_order(sell)

    result = book.match_with_quantity()

    assert result is not None
    matched_buy, matched_sell, traded_quantity = result

    assert matched_buy.order_id == 1
    assert matched_sell.order_id == 3
    assert traded_quantity == 2
    assert first_buy.quantity == 0
    assert second_buy.quantity == 3
    assert book.bid_count() == 1
    assert book.ask_count() == 0