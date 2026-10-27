from chronosmatch.matching.order_book import LimitOrderBook
from chronosmatch.simulator.order import Order


def test_lowest_sell_price_has_priority():
    book = LimitOrderBook()

    higher_sell = Order(
        order_id=1, price=102.0, quantity=2, side="SELL"
    )
    lower_sell = Order(
        order_id=2, price=100.0, quantity=3, side="SELL"
    )
    buy = Order(
        order_id=3, price=101.0, quantity=2, side="BUY"
    )

    book.add_order(higher_sell)
    book.add_order(lower_sell)
    book.add_order(buy)

    result = book.match_with_quantity()

    assert result is not None
    matched_buy, matched_sell, traded_quantity = result

    assert matched_buy.order_id == 3
    assert matched_sell.order_id == 2
    assert traded_quantity == 2
    assert lower_sell.quantity == 1
    assert higher_sell.quantity == 2
    assert book.best_ask() == 100.0