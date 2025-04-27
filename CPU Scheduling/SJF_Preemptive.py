class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def sjf_preemptive(processes):
    time = 0
    completed = 0
    n = len(processes)
    while completed != n:

        available_processes = []

        for p in processes:
            if p.arrival_time <= time and p.remaining_time > 0:
                available_processes.append(p)
        
        if available_processes:

            current_process = min(available_processes, key=lambda p: p.remaining_time)
            current_process.remaining_time -= 1
            
            if current_process.remaining_time == 0:
                completed += 1
                current_process.completion_time = time + 1
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
        
        time += 1
    
    return processes

def print_processes(processes):
    processes.sort(key=lambda p: p.completion_time)
    print("PID\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for p in processes:
        print(f"{p.pid}\t{p.arrival_time}\t\t{p.burst_time}\t\t{p.completion_time}\t\t{p.turnaround_time}\t\t{p.waiting_time}")

if __name__ == "__main__":
    processes = [
        Process("P0", 3, 2),
        Process("P1", 2, 4),
        Process("P2", 0, 6),
        Process("P3", 1, 4)
    ]
    
    completed_processes = sjf_preemptive(processes)
    print_processes(completed_processes)
