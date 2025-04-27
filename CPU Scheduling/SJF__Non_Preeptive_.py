def sjf_scheduling(processes):
    processes = sorted(processes, key=lambda x: x[1]) 

    completion_time = []
    turnaround_time = []
    waiting_time = []
    
    current_time = 0
    remaining_processes = processes.copy()
    scheduled_processes = []
    
    while remaining_processes:
        available_processes = []

        for p in remaining_processes:
            if p[1] <= current_time:
                available_processes.append(p)

        if available_processes:
            next_process = min(available_processes, key=lambda x: x[2])  
        else:
            next_process = min(remaining_processes, key=lambda x: x[1]) 
            current_time = next_process[1]

        remaining_processes.remove(next_process)
        
        pid, arrival, burst = next_process
        completion = current_time + burst
        turnaround = completion - arrival
        waiting = turnaround - burst
        
        scheduled_processes.append((pid, arrival, burst, completion, turnaround, waiting))
        
        current_time = completion
    
    print("PID | Arrival | Burst | Completion | Turnaround | Waiting")
    for p in scheduled_processes:
        print(f"{p[0]:3} | {p[1]:7} | {p[2]:5} | {p[3]:10} | {p[4]:10} | {p[5]:7}")
    
    avg_turnaround = sum(p[4] for p in scheduled_processes) / len(processes)
    avg_waiting = sum(p[5] for p in scheduled_processes) / len(processes)
    
    print(f"\nThoi gian hoan thanh trung binh: {avg_turnaround:.2f}")
    print(f"Thoi gian cho trung binh: {avg_waiting:.2f}")

processes = [("P0", 3, 2), ("P1", 2, 4), ("P2", 0, 6), ("P3", 1, 4)]
sjf_scheduling(processes)
