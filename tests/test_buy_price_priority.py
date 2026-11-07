from chronosmatch.matching.order_book import LimitOrderBook
from chronosmatch.simulator.order import Order


def test_highest_buy_price_has_priority():
    book = LimitOrderBook()

    lower_buy = Order(
        order_id=1, price=100.0, quantity=2, side="BUY"
    )
    higher_buy = Order(
        order_id=2, price=102.0, quantity=3, side="BUY"
    )
    sell = Order(
        order_id=3, price=101.0, quantity=2, side="SELL"
    )

    book.add_order(lower_buy)
    book.add_order(higher_buy)
    book.add_order(sell)

    result = book.match_with_quantity()

    assert result is not None
    matched_buy, matched_sell, traded_quantity = result

    assert matched_buy.order_id == 2
    assert matched_sell.order_id == 3
    assert traded_quantity == 2
    assert higher_buy.quantity == 1
    assert lower_buy.quantity == 2
    assert book.best_bid() == 102.0