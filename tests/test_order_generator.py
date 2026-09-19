from chronosmatch.simulator.order_generator import OrderGenerator


def test_order_generator_creates_valid_order():
    generator = OrderGenerator()

    order = generator.generate()

    assert order.is_valid()


def test_order_ids_increment():
    generator = OrderGenerator(start_order_id=100)

    first = generator.generate()
    second = generator.generate()

    assert first.order_id == 100
    assert second.order_id == 101