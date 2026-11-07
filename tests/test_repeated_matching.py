from chronosmatch.matching.order_book import LimitOrderBook
from chronosmatch.simulator.order import Order


def test_repeated_matching_consumes_orders_correctly():
    book = LimitOrderBook()

    book.add_order(
        Order(order_id=1, price=101.0, quantity=5, side="BUY")
    )
    book.add_order(
        Order(order_id=2, price=100.0, quantity=2, side="SELL")
    )
    book.add_order(
        Order(order_id=3, price=101.0, quantity=2, side="SELL")
    )

    first = book.match_with_quantity()

    assert first is not None
    assert first[2] == 2
    assert book.bid_count() == 1
    assert book.ask_count() == 1

    second = book.match_with_quantity()

    assert second is not None
    assert second[2] == 2
    assert book.bid_count() == 1
    assert book.ask_count() == 0
    assert book.bids[101.0][0].quantity == 1