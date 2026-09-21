from chronosmatch.integration.serializer import OrderSerializer
from chronosmatch.simulator.order import Order


def test_order_serialization_and_deserialization():
    order = Order(
        order_id=101,
        price=100.50,
        quantity=25,
        side="BUY",
    )

    data = OrderSerializer.serialize(order)
    restored_order = OrderSerializer.deserialize(data)

    assert isinstance(data, bytes)
    assert len(data) == OrderSerializer.SIZE
    assert restored_order == order


def test_sell_order_serialization():
    order = Order(
        order_id=202,
        price=101.25,
        quantity=50,
        side="SELL",
    )

    data = OrderSerializer.serialize(order)
    restored_order = OrderSerializer.deserialize(data)

    assert restored_order == order


def test_invalid_data_size_is_rejected():
    try:
        OrderSerializer.deserialize(b"invalid")
    except ValueError:
        assert True
    else:
        assert False