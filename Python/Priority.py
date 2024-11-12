import time

def priorityScheduling(processes, burstTimes):
    n = len(processes)
    waitingTime = [0] * n
    turnaroundTime = [0] * n
    TotalWt, totalTt = 0, 0

    startTime = time.time()

    waitingTime[0] = 0
    for i in range(1, n):
        waitingTime[i] = burstTimes[i - 1] + waitingTime[i - 1]

    for i in range(n):
        turnaroundTime[i] = burstTimes[i] + waitingTime[i]
        TotalWt += waitingTime[i]
        totalTt += turnaroundTime[i]

    avgWt = TotalWt / n
    avgTt = totalTt / n
    endTime = time.time()
    runningTime = endTime - startTime
    throughput = n / runningTime

    print("Processes Burst Time Waiting Time Turn-Around Time")
    for i in range(n):
        print(f" {processes[i]}\t\t{burstTimes[i]}\t\t{waitingTime[i]}\t\t{turnaroundTime[i]}")
    
    print("Average waiting time =", avgWt)
    print("Average turn-around time =", avgTt)
    print("Throughput =", throughput)
    print("Running time =", runningTime, "seconds")

if __name__ == "__main__":
    processes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    burstTimes = [10, 5, 8, 15, 12, 13, 14, 15, 17, 4]
    priorityScheduling(processes, burstTimes)
