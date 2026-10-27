from chronosmatch.matching.order_book import LimitOrderBook
from chronosmatch.simulator.order import Order


def test_lowest_sell_price_is_selected_across_price_levels():
    book = LimitOrderBook()

    book.add_order(
        Order(order_id=1, price=103.0, quantity=2, side="SELL")
    )
    book.add_order(
        Order(order_id=2, price=100.0, quantity=3, side="SELL")
    )
    book.add_order(
        Order(order_id=3, price=101.0, quantity=2, side="BUY")
    )

    result = book.match_with_quantity()

    assert result is not None
    matched_buy, matched_sell, traded_quantity = result

    assert matched_buy.order_id == 3
    assert matched_sell.order_id == 2
    assert traded_quantity == 2
    assert book.best_ask() == 100.0
    assert book.ask_count() == 2
    assert book.bid_count() == 0