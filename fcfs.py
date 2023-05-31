from typing import List
from process import Process


def fcfs(processes: List[Process]) -> None:
    processes.sort(key=lambda process: process.p_arrival_time)
    current_time: int = 0
    for process in processes:
        current_time += process.p_burst_time
        process.p_exit_time = current_time
        process.p_turnaround_time = current_time - process.p_arrival_time
        process.p_waiting_time = process.p_turnaround_time - process.p_burst_time
