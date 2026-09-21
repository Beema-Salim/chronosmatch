import struct

from chronosmatch.simulator.order import Order


class OrderSerializer:
    """Serialize and deserialize orders using struct."""

    FORMAT = "<QdIB"
    SIZE = struct.calcsize(FORMAT)

    SIDE_TO_CODE = {
        "BUY": 1,
        "SELL": 2,
    }

    CODE_TO_SIDE = {
        1: "BUY",
        2: "SELL",
    }

    @classmethod
    def serialize(cls, order: Order) -> bytes:
        """Convert an Order into compact binary data."""
        if not order.is_valid():
            raise ValueError("Invalid order")

        return struct.pack(
            cls.FORMAT,
            order.order_id,
            order.price,
            order.quantity,
            cls.SIDE_TO_CODE[order.side],
        )

    @classmethod
    def deserialize(cls, data: bytes) -> Order:
        """Convert binary data back into an Order."""
        if len(data) != cls.SIZE:
            raise ValueError("Invalid order data size")

        order_id, price, quantity, side_code = struct.unpack(
            cls.FORMAT,
            data,
        )

        if side_code not in cls.CODE_TO_SIDE:
            raise ValueError("Invalid order side code")

        return Order(
            order_id=order_id,
            price=price,
            quantity=quantity,
            side=cls.CODE_TO_SIDE[side_code],
        )