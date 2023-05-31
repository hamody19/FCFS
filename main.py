from process import Process
from fcfs import fcfs
from printFcfs import print_fcfs
from threading import Thread
if __name__ == "__main__":
    processes = [
        Process("p1", p_arrival_time=0, p_burst_time=15),
        Process("p2", p_arrival_time=2, p_burst_time=6),
        Process("p3", p_arrival_time=3, p_burst_time=7),
        Process("p4", p_arrival_time=5, p_burst_time=5)
    ]
    thread = Thread(target=fcfs(processes))
    thread.start()
    thread.join()
    print_fcfs(processes)