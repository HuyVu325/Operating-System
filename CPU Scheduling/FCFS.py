def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x[1])
    
    completion_time = []
    turnaround_time = []
    waiting_time = []
    
    current_time = 0
    for process in processes:
        pid, arrival, burst = process
        if current_time < arrival:
            current_time = arrival
        completion = current_time + burst
        turnaround = completion - arrival
        waiting = turnaround - burst
        
        completion_time.append(completion)
        turnaround_time.append(turnaround)
        waiting_time.append(waiting)
        
        current_time = completion
    
    print("PID | Arrival | Burst | Completion | Turnaround | Waiting")
    for i, process in enumerate(processes):
        print(f"{process[0]:3} | {process[1]:7} | {process[2]:5} | {completion_time[i]:10} | {turnaround_time[i]:10} | {waiting_time[i]:7}")
    
    avg_turnaround = sum(turnaround_time) / len(processes)
    avg_waiting = sum(waiting_time) / len(processes)
    
    print(f"\nThoi gian hoan thanh trung binh: {avg_turnaround:.2f}")
    print(f"Thoi gian cho trung binh: {avg_waiting:.2f}")

processes = [(1, 0, 5), (2, 1, 3), (3, 2, 8), (4, 3, 6)]
fcfs_scheduling(processes)

