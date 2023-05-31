from dataclasses import dataclass, field

@dataclass
class Process:
    p_name: str
    p_arrival_time: int
    p_burst_time: int
    p_exit_time: int = field(init=False, default=0)
    p_waiting_time: int = field(init=False, default=0)
    p_turnaround_time: int = field(init=False, default=0)
