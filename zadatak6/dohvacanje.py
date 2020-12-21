import urllib.request
import threading
import queue
import os

def worker(results_queue, url):
    sadrzaj = urllib.request.urlopen(url).read()
    results_queue.put(sadrzaj)

if __name__ == '__main__':
    results_queue = queue.Queue()
    
    t1 = threading.Thread(target=worker, args=(results_queue, "https://google.com"))
    t2 = threading.Thread(target=worker, args=(results_queue, "https://bing.com"))

    t1.start()
    t2.start()
    
    sajt = results_queue.get()

    with open("sajt.html", "w") as fajl:
       fajl.write(str(sajt)) 
