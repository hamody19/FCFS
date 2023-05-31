from process import Process
from typing import List
from colorama import Fore, init

init()


def print_fcfs(processes: List[Process]):
    total_turnaround_time = total_waiting_time = 0
    print("-"*19, f"{Fore.BLUE}FCFS{Fore.RESET}", "-"*19)
    for process in processes:
        total_turnaround_time += process.p_turnaround_time
        total_waiting_time += process.p_waiting_time
        print(
            f"{Fore.CYAN}[+]{Fore.RESET} Process name: "
            f"{Fore.GREEN}{process.p_name}{Fore.RESET}"
        )
        print(
            f"{Fore.CYAN}[+]{Fore.RESET} Process arrival time: "
            f"{Fore.RED}{process.p_arrival_time} ms{Fore.RESET}"
        )
        print(
            f"{Fore.CYAN}[+]{Fore.RESET} Process burst time: "
            f"{Fore.RED}{process.p_burst_time} ms{Fore.RESET}"
        )
        print(
            f"{Fore.CYAN}[+]{Fore.RESET} Process termination time: "
            f"{Fore.RED}{process.p_exit_time} ms{Fore.RESET}"
        )
        print(
            f"{Fore.CYAN}[+]{Fore.RESET} Process turnaround time: "
            f"{Fore.RED}{process.p_turnaround_time} ms{Fore.RESET}"
        )
        print(
            f"{Fore.CYAN}[+]{Fore.RESET} Process waiting time: "
            f"{Fore.RED}{process.p_waiting_time} ms{Fore.RESET}"
        )
        print("-"*44)
    # end of the loop
    print(
        f"{Fore.CYAN}[+]{Fore.RESET} average turnaround time: "
        f"{Fore.RED}{total_turnaround_time/processes.__len__()} ms{Fore.RESET}"
    )
    print(
        f"{Fore.CYAN}[+]{Fore.RESET} average waiting time: "
        f"{Fore.RED}{total_waiting_time/processes.__len__()} ms{Fore.RESET}"
    )
    print("-" * 19, f"{Fore.GREEN}end!{Fore.RESET}", "-" * 19)

