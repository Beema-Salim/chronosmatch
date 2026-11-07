import mmap
from pathlib import Path


class MMapBuffer:
    """File-backed memory-mapped buffer for shared raw bytes."""

    def __init__(self, file_path: str | Path, size: int = 4096) -> None:
        if size <= 0:
            raise ValueError("size must be greater than zero")

        self.file_path = Path(file_path)
        self.size = size
        self._file = None
        self._mmap = None

        self._open()

    def _open(self) -> None:
        """Create the backing file and memory-map it."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        self._file = self.file_path.open("w+b")
        self._file.truncate(self.size)

        self._mmap = mmap.mmap(
            self._file.fileno(),
            self.size,
        )

    def write(self, data: bytes, offset: int = 0) -> None:
        """Write raw bytes into the mapped memory."""
        if offset < 0 or offset + len(data) > self.size:
            raise ValueError("Data exceeds buffer boundaries")

        self._mmap.seek(offset)
        self._mmap.write(data)

    def read(self, length: int, offset: int = 0) -> bytes:
        """Read raw bytes from the mapped memory."""
        if length < 0 or offset < 0 or offset + length > self.size:
            raise ValueError("Read exceeds buffer boundaries")

        self._mmap.seek(offset)
        return self._mmap.read(length)

    def close(self) -> None:
        """Close the memory mapping and backing file."""
        if self._mmap is not None:
            self._mmap.close()
            self._mmap = None

        if self._file is not None:
            self._file.close()
            self._file = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()