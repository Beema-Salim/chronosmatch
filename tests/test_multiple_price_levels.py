from chronosmatch.matching.order_book import LimitOrderBook
from chronosmatch.simulator.order import Order


def test_best_buy_price_is_selected_across_price_levels():
    book = LimitOrderBook()

    book.add_order(
        Order(order_id=1, price=99.0, quantity=2, side="BUY")
    )
    book.add_order(
        Order(order_id=2, price=102.0, quantity=3, side="BUY")
    )
    book.add_order(
        Order(order_id=3, price=101.0, quantity=2, side="SELL")
    )

    result = book.match_with_quantity()

    assert result is not None
    matched_buy, matched_sell, traded_quantity = result

    assert matched_buy.order_id == 2
    assert matched_sell.order_id == 3
    assert traded_quantity == 2
    assert book.best_bid() == 102.0
    assert book.bid_count() == 2
    assert book.ask_count() == 0