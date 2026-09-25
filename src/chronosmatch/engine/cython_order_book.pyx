cdef class CythonOrderBook:
    """Cython-based order book foundation."""

    cdef int buy_orders
    cdef int sell_orders

    def _cinit_(self):
        self.buy_orders = 0
        self.sell_orders = 0

    cpdef add_buy_order(self):
        """Record a BUY order."""
        self.buy_orders += 1

    cpdef add_sell_order(self):
        """Record a SELL order."""
        self.sell_orders += 1

    cpdef int get_buy_count(self):
        """Return the number of BUY orders."""
        return self.buy_orders

    cpdef int get_sell_count(self):
        """Return the number of SELL orders."""
        return self.sell_orders