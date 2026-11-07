cdef class CythonMatchingEngine:
    """Basic Cython foundation for the ChronosMatch matching engine."""

    cdef int processed_orders

    def _cinit_(self):
        self.processed_orders = 0

    cpdef int process_order(self):
        """Record that an order has been processed."""
        self.processed_orders += 1
        return self.processed_orders

    cpdef int get_processed_orders(self):
        """Return the number of processed orders."""
        return self.processed_orders