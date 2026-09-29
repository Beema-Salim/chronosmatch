import curses
import time


class CursesDashboard:
    """Simple terminal dashboard for ChronosMatch."""

    def __init__(self) -> None:
        self.running = True

    def draw(self, stdscr) -> None:
        """Render the dashboard screen."""
        stdscr.clear()
        stdscr.addstr(1, 2, "ChronosMatch Dashboard")
        stdscr.addstr(3, 2, "Status: RUNNING")
        stdscr.addstr(4, 2, "Orders Processed: 0")
        stdscr.addstr(5, 2, "Trades Executed: 0")
        stdscr.addstr(6, 2, "Best Bid: --")
        stdscr.addstr(7, 2, "Best Ask: --")
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