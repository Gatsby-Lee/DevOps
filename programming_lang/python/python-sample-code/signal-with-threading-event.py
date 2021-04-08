"""
@ref: https://docs.python.org/3/library/threading.html#threading.Event
@ref: https://docs.python.org/3/library/signal.html#signal.signal
@ref: https://docs.python.org/3/reference/datamodel.html#frame-objects
"""
import logging
import signal
import threading

LOGGER = logging.getLogger(__name__)


def create_signal_handlers(signalnum, tevent: threading.Event):
    # pylint: disable=unused-argument
    def signal_handler(sig, frame_obj):
        LOGGER.info("Signal %s detected", sig)
        tevent.set()

    # When threads are enabled, `signal.signal` can only be called from the main thread;
    # attempting to call it from other threads will cause a `ValueError` exception to be raised.
    signal.signal(signalnum, signal_handler)


def create_test_threads():
    tevent = threading.Event()
    create_signal_handlers(signal.SIGTERM, tevent)

    def worker():
        while tevent.is_set() is False:
            print("hello")
            tevent.wait(2)

    thread_count = 2
    t_list = []
    for _ in range(thread_count):
        t = threading.Thread(target=worker)
        t.start()
        t_list.append(t)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    create_test_threads()
