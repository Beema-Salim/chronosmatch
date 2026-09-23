from chronosmatch.matching.order_book import LimitOrderBook
from chronosmatch.simulator.order import Order


def test_order_book_adds_buy_order():
    book = LimitOrderBook()

    order = Order(
        order_id=1,
        price=100.50,
        quantity=10,
        side="BUY",
    )

    book.add_order(order)

    assert book.bid_count() == 1
    assert book.ask_count() == 0
    assert book.best_bid() == 100.50


def test_order_book_adds_sell_order():
    book = LimitOrderBook()

    order = Order(
        order_id=2,
        price=101.00,
        quantity=5,
        side="SELL",
    )

    book.add_order(order)

    assert book.bid_count() == 0
    assert book.ask_count() == 1
    assert book.best_ask() == 101.00


def test_order_book_tracks_multiple_price_levels():
    book = LimitOrderBook()

    book.add_order(
        Order(order_id=1, price=100.00, quantity=10, side="BUY")
    )
    book.add_order(
        Order(order_id=2, price=101.00, quantity=20, side="BUY")
    )
    book.add_order(
        Order(order_id=3, price=102.00, quantity=15, side="SELL")
    )
    book.add_order(
        Order(order_id=4, price=101.50, quantity=5, side="SELL")
    )

    assert book.bid_count() == 2
    assert book.ask_count() == 2
    assert book.best_bid() == 101.00
    assert book.best_ask() == 101.50


def test_empty_order_book_has_no_best_prices():
    book = LimitOrderBook()

    assert book.best_bid() is None
    assert book.best_ask() is None

def test_best_bid_orders_returns_orders_at_highest_price():
    book = LimitOrderBook()

    first_order = Order(
        order_id=1,
        price=100.00,
        quantity=10,
        side="BUY",
    )

    best_order = Order(
        order_id=2,
        price=101.00,
        quantity=20,
        side="BUY",
    )

    book.add_order(first_order)
    book.add_order(best_order)

    orders = book.best_bid_orders()

    assert orders == [best_order]


def test_best_bid_orders_returns_multiple_orders_at_same_price():
    book = LimitOrderBook()

    first_order = Order(
        order_id=1,
        price=101.00,
        quantity=10,
        side="BUY",
    )

    second_order = Order(
        order_id=2,
        price=101.00,
        quantity=20,
        side="BUY",
    )

    book.add_order(first_order)
    book.add_order(second_order)

    orders = book.best_bid_orders()

    assert orders == [first_order, second_order]