from chronosmatch.integration.ipc import OrderBuffer
from chronosmatch.simulator.order import Order


def test_order_buffer_write_and_read():
    buffer = OrderBuffer()

    order = Order(
        order_id=1,
        price=100.50,
        quantity=10,
        side="BUY",
    )

    buffer.write(order)

    assert buffer.size() == 1
    assert buffer.read() == order
    assert buffer.size() == 0


def test_empty_buffer_returns_none():
    buffer = OrderBuffer()

    assert buffer.read() is None
    assert buffer.size() == 0


def test_buffer_rejects_invalid_order():
    buffer = OrderBuffer()

    invalid_order = Order(
        order_id=0,
        price=100.50,
        quantity=10,
        side="BUY",
    )

    try:
        buffer.write(invalid_order)
    except ValueError:
        assert True
    else:
        assert False

def test_buffer_rejects_invalid_max_size():
    try:
        OrderBuffer(max_size=0)
    except ValueError:
        assert True
    else:
        assert False


def test_buffer_detects_full_state():
    buffer = OrderBuffer(max_size=2)

    order1 = Order(order_id=1, price=100.0, quantity=10, side="BUY")
    order2 = Order(order_id=2, price=101.0, quantity=5, side="SELL")

    buffer.write(order1)
    buffer.write(order2)

    assert buffer.is_full()
    assert buffer.size() == 2


def test_buffer_rejects_order_when_full():
    buffer = OrderBuffer(max_size=1)

    order1 = Order(order_id=1, price=100.0, quantity=10, side="BUY")
    order2 = Order(order_id=2, price=101.0, quantity=5, side="SELL")

    buffer.write(order1)

    try:
        buffer.write(order2)
    except BufferError:
        assert True
    else:
        assert False