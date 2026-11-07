from chronosmatch.matching.order_book import LimitOrderBook
from chronosmatch.simulator.order import Order


def test_same_price_sell_orders_follow_fifo_priority():
    book = LimitOrderBook()

    buy = Order(
        order_id=1, price=101.0, quantity=2, side="BUY"
    )
    first_sell = Order(
        order_id=2, price=100.0, quantity=2, side="SELL"
    )
    second_sell = Order(
        order_id=3, price=100.0, quantity=3, side="SELL"
    )

    book.add_order(buy)
    book.add_order(first_sell)
    book.add_order(second_sell)

    result = book.match_with_quantity()

    assert result is not None
    matched_buy, matched_sell, traded_quantity = result

    assert matched_buy.order_id == 1
    assert matched_sell.order_id == 2
    assert traded_quantity == 2
    assert first_sell.quantity == 0
    assert second_sell.quantity == 3
    assert book.bid_count() == 0
    assert book.ask_count() == 1