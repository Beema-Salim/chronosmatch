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


def test_generate_buy_order():
    generator = OrderGenerator()

    order = generator.generate("BUY")

    assert order.side == "BUY"
    assert order.is_valid()


def test_generate_sell_order():
    generator = OrderGenerator()

    order = generator.generate("SELL")

    assert order.side == "SELL"
    assert order.is_valid()