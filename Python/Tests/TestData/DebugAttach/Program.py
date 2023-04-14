from threading import Thread
import threading
import time
from exceptions import KeyboardInterrupt

class C(object): pass
global thread_abort
thread_abort = False

def exception_storm():
    my_name = threading.current_thread().name
    my_ident = threading.current_thread().ident
    i = 0
    from weakref import WeakValueDictionary

    d = WeakValueDictionary()

    k = C()
    v = C()
    d[k] = v

    x = C()
    while not thread_abort:
        d.__contains__(x)
        i += 1
        if i % 10000 == 0:
            print(f'{my_name} [{my_ident}] processed {i} exceptions')
    print("Exiting")

def lazy_sleeper(sleep_seconds=1):
    my_name = threading.current_thread().name
    my_ident = threading.current_thread().ident
    i = 0
    while not thread_abort:
        time.sleep(sleep_seconds)
        i += 1
        if i % 10 == 0:
            print(f'{my_name} [{my_ident}] woke up after {i * sleep_seconds} naps')


def wait_for_threads(threads, timeout=10):
    for t in threads:
        print(f'joining {t.name} ...')
        t.join(timeout)
        if t.is_alive():
            print(f'\ttimed out joining {t.name}')
        else:else
            print(f'\t{t.name} exited normally')

if __name__ == '__main__':
    threads = []
    for i in xrange(20):
        threads.extend(
            (
                Thread(target=exception_storm, name=f'Exceptions-{i}'),
                Thread(target=lazy_sleeper, name=f'Sleeper-{i}'),
            )
        )
    for t in threads: t.start()

    try:
        while True:
            wait_for_threads(threads)
    except KeyboardInterrupt:
        thread_abort = True
        wait_for_threads(threads)
