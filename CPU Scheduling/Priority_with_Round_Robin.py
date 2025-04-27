class Process:
    def __init__(self, pid, burst_time, priority):
        self.pid = pid
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

def priority_with_round_robin(processes, time_quantum):

    processes.sort(key=lambda p: p.priority)
    
    queue = []  
    time = 0  
    index = 0  
    
    while index < len(processes) or queue:
       
        while index < len(processes) and (queue == [] or processes[index].priority == queue[0].priority):
            queue.append(processes[index])
            index += 1
        
        if queue:
            process = queue.pop(0)
            execute_time = min(process.remaining_time, time_quantum)
            process.remaining_time -= execute_time
            time += execute_time
            
            if process.remaining_time > 0:
                queue.append(process)
            else:
                process.turnaround_time = time 
                process.waiting_time = process.turnaround_time - process.burst_time
    
    return processes

def print_results(processes):
    print("PID\tPriority\tBurst Time\tWaiting Time\tTurnaround Time")
    for p in processes:
        print(f"{p.pid}\t{p.priority}\t\t{p.burst_time}\t\t{p.waiting_time}\t\t{p.turnaround_time}")

# Danh sách tiến trình
process_list = [
    Process(1, 4, 3),
    Process(2, 5, 2),
    Process(3, 8, 2),
    Process(4, 7, 1),
    Process(5, 3, 3)
]

time_quantum = 2
scheduled_processes = priority_with_round_robin(process_list, time_quantum)
print_results(scheduled_processes)
