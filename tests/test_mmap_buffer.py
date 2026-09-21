from chronosmatch.integration.mmap_buffer import MMapBuffer


def test_mmap_buffer_write_and_read(tmp_path):
    file_path = tmp_path / "orders.mmap"

    with MMapBuffer(file_path, size=128) as buffer:
        data = b"chronosmatch"

        buffer.write(data)

        assert buffer.read(len(data)) == data


def test_mmap_buffer_supports_offsets(tmp_path):
    file_path = tmp_path / "orders.mmap"

    with MMapBuffer(file_path, size=128) as buffer:
        buffer.write(b"BUY", offset=10)

        assert buffer.read(3, offset=10) == b"BUY"


def test_mmap_buffer_rejects_invalid_size(tmp_path):
    file_path = tmp_path / "orders.mmap"

    try:
        MMapBuffer(file_path, size=0)
    except ValueError:
        assert True
    else:
        assert False


def test_mmap_buffer_rejects_out_of_bounds_write(tmp_path):
    file_path = tmp_path / "orders.mmap"

    with MMapBuffer(file_path, size=8) as buffer:
        try:
            buffer.write(b"too long data", offset=0)
        except ValueError:
            assert True
        else:
            assert False