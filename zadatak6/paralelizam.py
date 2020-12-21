import threading
import queue

NUM_THREADS = 4

def worker(work_queue, results_queue):
    while True:
        item = work_queue.get()
        if item == "END":
            break
        results_queue.put(item ** 2)
        work_queue.task_done()

if __name__ == '__main__':
    work_queue = queue.Queue()
    results_queue = queue.Queue()

    threads = [
        threading.Thread(target=worker,
                         args=(work_queue, results_queue))
        for i in range(NUM_THREADS)
    ]

    for thread in threads:
        thread.start()

    for i in range(1, 11):
        work_queue.put(i)

    work_queue.join()
    print('all items processed')

    for t in range(NUM_THREADS):
        work_queue.put("END")

    while threads:
        threads.pop().join()

    while not results_queue.empty():
        print(results_queue.get())
