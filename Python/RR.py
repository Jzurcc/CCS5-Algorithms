import time

def findWaitingTime(processes, bt, wt, quantum):
    n = len(processes)
    rem_bt = bt[:]
    t = 0
    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        if done:
            break

def findTurnAroundTime(processes, bt, wt, tat):
    n = len(processes)
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def RR(processes, bt, quantum):
    n = len(processes)
    wt = [0] * n
    tat = [0] * n
    start_time = time.time()
    findWaitingTime(processes, bt, wt, quantum)
    findTurnAroundTime(processes, bt, wt, tat)
    end_time = time.time()
    total_wt = sum(wt)
    total_tat = sum(tat)
    avg_wt = total_wt / n
    avg_tat = total_tat / n
    throughput = n / (end_time - start_time)
    print("Processes Burst Time Waiting Time Turn-Around Time")
    for i in range(n):
        print(f" {processes[i]}        {bt[i]}        {wt[i]}          {tat[i]}")
    print(f"\nAverage waiting time = {avg_wt:.5f}")
    print(f"Average turn around time = {avg_tat:.5f}")
    print(f"Throughput = {throughput}")
    print(f"Running time = {end_time - start_time:.5f} seconds")

if __name__ == "__main__":
    processes = [1, 2, 3]
    burst_time = [10, 5, 8]
    quantum = 2
    RR(processes, burst_time, quantum)
