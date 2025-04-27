def round_robin(processes, burst_time, quantum):

    n = len(processes)
    remaining_time = burst_time.copy()
    waiting_time = [0] * n
    turnaround_time = [0] * n
    t = 0  
    
    while True:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False
                if remaining_time[i] > quantum:
                    t += quantum
                    remaining_time[i] -= quantum
                else:
                    t += remaining_time[i]
                    waiting_time[i] = t - burst_time[i]
                    remaining_time[i] = 0
        
        if done:
            break
    
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]
    
    print("Process	Burst Time	Waiting Time	Turnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    
processes = [1, 2, 3]
burst_time = [24, 3, 3]
quantum = 4
round_robin(processes, burst_time, quantum)