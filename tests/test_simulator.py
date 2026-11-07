import asyncio

from chronosmatch.simulator.simulator import MarketSimulator


def test_simulator_generates_requested_number_of_orders():
    async def run_test():
        simulator = MarketSimulator(order_interval=0)

        orders = [
            order
            async for order in simulator.generate_orders(5)
        ]

        assert len(orders) == 5
        assert all(order.is_valid() for order in orders)

    asyncio.run(run_test())


def test_simulator_generates_unique_order_ids():
    async def run_test():
        simulator = MarketSimulator(order_interval=0)

        orders = [
            order
            async for order in simulator.generate_orders(3)
        ]

        order_ids = [order.order_id for order in orders]

        assert order_ids == [1, 2, 3]

    asyncio.run(run_test())


def test_set_order_rate():
    simulator = MarketSimulator()

    simulator.set_order_rate(100)

    assert simulator.order_interval == 0.01


def test_set_order_rate_rejects_zero():
    simulator = MarketSimulator()

    try:
        simulator.set_order_rate(0)
    except ValueError:
        assert True
    else:
        assert False