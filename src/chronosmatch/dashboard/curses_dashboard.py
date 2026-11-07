import curses
import time


class CursesDashboard:
    """Terminal dashboard for ChronosMatch."""

    def __init__(self) -> None:
        self.running = True
        self.best_bid: float | None = None
        self.best_ask: float | None = None
        self.orders_processed = 0
        self.trades_executed = 0

    def update_market(
        self,
        best_bid: float | None,
        best_ask: float | None,
    ) -> None:
        """Update the current best bid and ask prices."""
        self.best_bid = best_bid
        self.best_ask = best_ask

    def record_order(self) -> None:
        """Record a processed order."""
        self.orders_processed += 1

    def record_trade(self) -> None:
        """Record an executed trade."""
        self.trades_executed += 1

    def draw(self, stdscr) -> None:
        """Render the dashboard screen."""
        stdscr.clear()
        stdscr.addstr(1, 2, "ChronosMatch Dashboard")
        stdscr.addstr(3, 2, "Status: RUNNING")
        stdscr.addstr(4, 2, f"Orders Processed: {self.orders_processed}")
        stdscr.addstr(5, 2, f"Trades Executed: {self.trades_executed}")

        bid = "--" if self.best_bid is None else f"{self.best_bid:.2f}"
        ask = "--" if self.best_ask is None else f"{self.best_ask:.2f}"

        stdscr.addstr(6, 2, f"Best Bid: {bid}")
        stdscr.addstr(7, 2, f"Best Ask: {ask}")
        stdscr.addstr(9, 2, "Press Q to exit.")
        stdscr.refresh()

    def run(self) -> None:
        """Start the terminal dashboard."""
        curses.wrapper(self._run)

    def _run(self, stdscr) -> None:
        """Run the curses event loop."""
        curses.curs_set(0)
        stdscr.nodelay(True)

        while self.running:
            self.draw(stdscr)

            key = stdscr.getch()
            if key in (ord("q"), ord("Q")):
                self.running = False

            time.sleep(0.1)