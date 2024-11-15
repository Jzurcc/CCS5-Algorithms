def findWaitingTime(processes, bt, wt, quantum):
    n = len(processes)
    rem_bt = [0] * n
    for i in range(n):
        rem_bt[i] = bt[i]
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
    return t  # Total running time

def findTurnAroundTime(processes, bt, wt, tat):
    n = len(processes)
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def findavgTime(processes, bt, quantum):
    n = len(processes)
    wt = [0] * n
    tat = [0] * n
    total_time = findWaitingTime(processes, bt, wt, quantum)
    findTurnAroundTime(processes, bt, wt, tat)

    print("Processes    Burst Time     Waiting Time    Turn-Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(" ", processes[i], "\t\t", bt[i], "\t\t", wt[i], "\t\t", tat[i])

    print("\nAverage waiting time = %.5f " % (total_wt / n))
    print("Average turn around time = %.5f " % (total_tat / n))
    print("Total running time = %d" % total_time)
    print("Throughput = %.5f processes per time unit" % (n / total_time))

if __name__ == "__main__":
    proc = [1, 2, 3]
    burst_time = [10, 5, 8]
    quantum = 2
    findavgTime(proc, burst_time, quantum)
