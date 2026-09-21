from chronosmatch.integration.mmap_order_channel import MMapOrderChannel
from chronosmatch.simulator.order import Order


def test_mmap_order_channel_writes_and_reads_order(tmp_path):
    file_path = tmp_path / "orders.mmap"

    order = Order(
        order_id=501,
        price=100.25,
        quantity=20,
        side="BUY",
    )

    with MMapOrderChannel(file_path, capacity=10) as channel:
        channel.write(order, index=0)

        restored_order = channel.read(index=0)

        assert restored_order == order


def test_mmap_order_channel_supports_multiple_slots(tmp_path):
    file_path = tmp_path / "orders.mmap"

    order1 = Order(
        order_id=601,
        price=99.75,
        quantity=15,
        side="BUY",
    )

    order2 = Order(
        order_id=602,
        price=101.50,
        quantity=30,
        side="SELL",
    )

    with MMapOrderChannel(file_path, capacity=10) as channel:
        channel.write(order1, index=0)
        channel.write(order2, index=1)

        assert channel.read(index=0) == order1
        assert channel.read(index=1) == order2


def test_mmap_order_channel_rejects_invalid_index(tmp_path):
    file_path = tmp_path / "orders.mmap"

    order = Order(
        order_id=701,
        price=100.00,
        quantity=10,
        side="BUY",
    )

    with MMapOrderChannel(file_path, capacity=2) as channel:
        try:
            channel.write(order, index=2)
        except IndexError:
            assert True
        else:
            assert False


def test_mmap_order_channel_rejects_invalid_capacity(tmp_path):
    file_path = tmp_path / "orders.mmap"

    try:
        MMapOrderChannel(file_path, capacity=0)
    except ValueError:
        assert True
    else:
        assert False