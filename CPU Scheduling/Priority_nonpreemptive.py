class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid  
        self.arrival_time = arrival_time  
        self.burst_time = burst_time  
        self.priority = priority  
        self.start_time = 0
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def priority_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)  
    
    current_time = 0
    completed_processes = []

    while processes:

        ready_queue = [p for p in processes if p.arrival_time <= current_time]

        if not ready_queue:
            current_time = processes[0].arrival_time
            continue

        ready_queue.sort(key=lambda x: x.priority)
        process = ready_queue[0]
        processes.remove(process)

        process.start_time = current_time
        process.completion_time = process.start_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time

        current_time = process.completion_time

        completed_processes.append(process)

    return completed_processes

# Danh sách tiến trình (pid, arrival_time, burst_time, priority)
process_list = [
    Process(1, 0, 5, 2),
    Process(2, 1, 3, 1),
    Process(3, 2, 8, 4),
    Process(4, 3, 6, 3)
]

completed_processes = priority_scheduling(process_list)

print(f"{'PID':<5}{'Arrival':<8}{'Burst':<6}{'Priority':<9}{'Start':<6}{'Complete':<9}{'TAT':<5}{'Waiting'}")
for p in completed_processes:
    print(f"{p.pid:<5}{p.arrival_time:<8}{p.burst_time:<6}{p.priority:<9}{p.start_time:<6}{p.completion_time:<9}{p.turnaround_time:<5}{p.waiting_time}")
