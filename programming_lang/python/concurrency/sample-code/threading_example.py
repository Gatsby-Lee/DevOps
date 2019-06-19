import logging
import threading
import time

LOGGER = logging.getLogger(__name__)

def infinite_loop_worker():
    """thread worker function"""

    while True:
        n = threading.currentThread().getName()
        t = int(time.time())
        LOGGER.info('%s: %s', n, t)
        time.sleep(2)

def finite_loop_worker(loop=3):
    """thread worker function"""

    for _ in range(loop):
        n = threading.currentThread().getName()
        t = int(time.time())
        LOGGER.info('%s: %s', n, t)
        time.sleep(2)

def main_run_infinite_loop_non_daemon_thread(num_threads=2):
    """
    main-thread,Program(Process) WAITS until all spawed(child)-thread completes.
    """
    LOGGER.info('==== Starting launch non-Daemon Threads ====')
    for i in range(num_threads):
        n = 'infinite-loop-non-daemon-%s' % i
        t = threading.Thread(target=infinite_loop_worker, name=n)
        t.start()
    LOGGER.info('==== Finished launching non-Daemon Threads ====')


def main_run_infinite_loop_daemon_thread(num_threads=2):
    """
    main-thread,Program(Process) KILLS Daemon threads abruptly since there are only non-daemon threads.
    And, main-thread,Program(Process) EXITS.
    """
    LOGGER.info('==== Starting launch Daemon Threads ====')
    for i in range(num_threads):
        n = 'infinite-loop-daemon-%s' % i
        # Python3 has daemon argument, but python2 doesn't.
        # t = threading.Thread(target=infinite_loop_worker, name=n, daemon=True)
        t = threading.Thread(target=infinite_loop_worker, name=n)
        t.daemon = True
        t.start()
    LOGGER.info('==== Finished launching Daemon Threads ====')


def main_run_finite_loop_nondaemon_and_infinite_daemon_thread(num_threads=2):
    """
    main-thread,Program(Process) WAITS until non-Daemon threads completes.
    And, main-thread,Program(Process) KILLS Daemon threads abruptly.
    And, main-thread,Program(Process) EXITS.
    """
    LOGGER.info('==== Starting launch Daemon Threads ====')
    for i in range(num_threads):
        n = 'infinite-loop-Daemon-%s' % i
        # Python3 has daemon argument, but python2 doesn't.
        # t = threading.Thread(target=infinite_loop_worker, name=n, daemon=True)
        t = threading.Thread(target=infinite_loop_worker, name=n)
        t.daemon = True
        t.start()
    LOGGER.info('==== Finished launching Daemon Threads ====')

    LOGGER.info('==== Starting launch non-Daemon Threads ====')
    for i in range(num_threads):
        n = 'finite-loop-non-daemon-%s' % i
        t = threading.Thread(target=finite_loop_worker, name=n)
        t.start()
    LOGGER.info('==== Finished launching non-Daemon Threads ====')


def main_run_nondaemon_with_start_join(num_threads=2):
    """
    main-thread,Program(Process) GOES to first For-Loop.
    Launch FIRST-BATCH-finite-loop-non-daemon-1 and WAITS until FIRST-BATCH-finite-loop-non-daemon-1 completes.
    Once FIRST-BATCH-finite-loop-non-daemon-1 completes, FIRST-BATCH-finite-loop-non-daemon-2 is launched.
    Once FIRST-BATCH-finite-loop-non-daemon-2 completes, main-thread,Program(Process) GOES to second For-Loop.

    main-thread,Program(Process) launch almost simultaneously
        SECOND-BATCH-finite-loop-non-daemon-1
        SECOND-BATCH-finite-loop-non-daemon-2
    AND, WAITS until these two threads completes.
    ONCE these two threads completes,
        main-thread,Program(Process) EXISTS.
    """
    LOGGER.info('==== Starting launch non-Daemon Threads with JOIN ====')
    for i in range(num_threads):
        n = 'FIRST-BATCH-finite-loop-non-daemon-%s' % i
        t = threading.Thread(target=finite_loop_worker, name=n)
        t.start()
        # FIRST-BATCH-finite-loop-non-daemon-2 will be blocked until FIRST-BATCH-finite-loop-non-daemon-1 completes.
        t.join()
    LOGGER.info('==== Finished launching non-Daemon Threads with JOIN ====')

    LOGGER.info('==== Starting launch non-Daemon Threads without JOIN ====')
    for i in range(num_threads):
        n = 'SECOND-BATCH-finite-loop-non-daemon-%s' % i
        t = threading.Thread(target=finite_loop_worker, name=n)
        t.start()
    LOGGER.info('==== Finished launching non-Daemon Threads without JOIN ====')


def main_run_nondaemon_with_start_first_join_later(num_threads=2):
    """
    main-thread,Program(Process) GOES to first For-Loop.
    Launch FIRST-BATCH-finite-loop-non-daemon
    AND WAITS until these two threads completes.

    ONCE FIRST-BATCH-finite-loop-non-daemon complete.
    Launch SECOND-BATCH-finite-loop-non-daemon
    AND WAITS until these two threads completes.

    SINCE there is no more active threads, main-thread,Program(Process) EXITS.
    """
    LOGGER.info('==== Starting creating non-Daemon Threads ====')
    join_threads = []
    for i in range(num_threads):
        n = 'FIRST-BATCH-finite-loop-non-daemon-%s' % i
        t = threading.Thread(target=finite_loop_worker, name=n)
        join_threads.append(t)
    LOGGER.info('==== Finished creating non-Daemon Threads ====')
    LOGGER.info('==== Starting non-Daemon Threads with JOIN ====')
    for t in join_threads:
        t.start()
    for t in join_threads:
        t.join()
    LOGGER.info('==== Finished non-Daemon Threads with JOIN ====')

    # SECOND-BATCH will be blocked until FIRST-BATCH completes.

    LOGGER.info('==== Starting launch non-Daemon Threads without JOIN ====')
    for i in range(num_threads):
        n = 'SECOND-BATCH-finite-loop-non-daemon-%s' % i
        t = threading.Thread(target=finite_loop_worker, name=n)
        t.start()
    LOGGER.info('==== Finished launching non-Daemon Threads without JOIN ====')


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    file_handler = logging.FileHandler('threading_example.log')
    file_handler.setLevel(level=logging.DEBUG)
    LOGGER.addHandler(file_handler)
    # main_run_infinite_loop_non_daemon_thread()
    # main_run_infinite_loop_daemon_thread()
    # main_run_finite_loop_nondaemon_and_infinite_daemon_thread()
    # main_run_nondaemon_with_start_join()
    main_run_nondaemon_with_start_first_join_later()
