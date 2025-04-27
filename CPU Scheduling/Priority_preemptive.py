import heapq

class Process:
    def __init__(self, process_id, arrival_time, burst_time, priority):
        self.process_id = process_id 
        self.arrival_time = arrival_time 
        self.burst_time = burst_time 
        self.priority = priority  
        self.remaining_time = burst_time  
        self.start_time = -1  
        self.completion_time = 0  
        self.waiting_time = 0 
        self.turnaround_time = 0  

def priority_preemptive_scheduling(process_list):

    process_list.sort(key=lambda process: process.arrival_time)
    
    priority_queue = [] 
    current_time = 0  
    process_index = 0  
    completed = 0  
    total_processes = len(process_list) 
    
    while completed < total_processes:

        while process_index < total_processes and process_list[process_index].arrival_time <= current_time:
            heapq.heappush(priority_queue, (process_list[process_index].priority, process_list[process_index].arrival_time, process_index))
            process_index += 1
        
        if priority_queue:

            _, _, selected_process_index = heapq.heappop(priority_queue)
            selected_process = process_list[selected_process_index]

            if selected_process.start_time == -1:
                selected_process.start_time = current_time
            
            selected_process.remaining_time -= 1
            current_time += 1

            if selected_process.remaining_time == 0:
                selected_process.completion_time = current_time
                selected_process.turnaround_time = selected_process.completion_time - selected_process.arrival_time
                selected_process.waiting_time = selected_process.turnaround_time - selected_process.burst_time
                completed += 1
            else:
                heapq.heappush(priority_queue, (selected_process.priority, selected_process.arrival_time, selected_process_index))
        else:
            current_time += 1

    return process_list

# Danh sách tiến trình (Process ID, Arrival Time, Burst Time, Priority)
processes = [
    Process(1, 0, 5, 2),
    Process(2, 1, 3, 1),
    Process(3, 2, 8, 4),
    Process(4, 3, 6, 3)
]

completed_processes = priority_preemptive_scheduling(processes)

print(f"{'Process':<8}{'Arrival':<8}{'Burst':<6}{'Priority':<9}{'Start':<6}{'Complete':<9}{'TAT':<5}{'Waiting'}")
for process in completed_processes:
    print(f"{process.process_id:<8}{process.arrival_time:<8}{process.burst_time:<6}{process.priority:<9}{process.start_time:<6}{process.completion_time:<9}{process.turnaround_time:<5}{process.waiting_time}")
