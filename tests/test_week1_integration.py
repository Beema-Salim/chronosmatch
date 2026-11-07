import asyncio

from chronosmatch.integration.mmap_order_channel import MMapOrderChannel
from chronosmatch.simulator.simulator import MarketSimulator


def test_simulator_to_mmap_end_to_end(tmp_path):
    file_path = tmp_path / "market_orders.mmap"

    async def generate_orders():
        simulator = MarketSimulator(
            order_interval=0,
            buffer=None,
        )

        return [
            order
            async for order in simulator.generate_orders(5)
        ]

    simulator_orders = asyncio.run(generate_orders())

    with MMapOrderChannel(file_path, capacity=10) as channel:
        for index, order in enumerate(simulator_orders):
            channel.write(order, index=index)

        restored_orders = [
            channel.read(index=index)
            for index in range(len(simulator_orders))
        ]

    assert restored_orders == simulator_orders
    assert len(restored_orders) == 5