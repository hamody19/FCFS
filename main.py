from process import Process
from fcfs import fcfs
from printFcfs import print_fcfs
from threading import Thread
if __name__ == "__main__":
    processes = [
        Process("p1", 0, 15),
        Process("p2", 2, 6),
        Process("p3", 3, 7),
        Process("p4", 5, 5)
    ]
    thread = Thread(target=fcfs(processes))
    thread.start()
    thread.join()
    print_fcfs(processes)