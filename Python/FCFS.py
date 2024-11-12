import time

def findWaitingTime(n, burstTimes, waitingTime):
    waitingTime[0] = 0
    for i in range(1, n):
        waitingTime[i] = burstTimes[i - 1] + waitingTime[i - 1]

def findTurnAroundTime(n, burstTimes, waitingTime, turnaroundTime):
    for i in range(n):
        turnaroundTime[i] = burstTimes[i] + waitingTime[i]

def FCFS(processes, burstTimes):
    n = len(processes)
    waitingTime = [0] * n
    turnaroundTime = [0] * n
    totalWt = 0
    totalTt = 0

    startTime = time.time()
    findWaitingTime(n, burstTimes, waitingTime)
    findTurnAroundTime(n, burstTimes, waitingTime, turnaroundTime)
    avgWt = totalWt / n
    avgTt = totalTt / n
    endTime = time.time()
    runningTime = endTime - startTime
    throughput = n / runningTime
    

    print("Processes Burst time Waiting time Turn around time")
    for i in range(n):
        totalWt += waitingTime[i]
        totalTt += turnaroundTime[i]
        print(" " + str(i + 1) + "\t\t" + str(burstTimes[i]) + "\t " + str(waitingTime[i]) + "\t\t " + str(turnaroundTime[i]))
    
    print("Average waiting time =", avgWt)
    print("Average turn-around time =", avgTt)
    print("Throughput =", throughput)
    print("Running time =", runningTime, "seconds")

if __name__ == "__main__":
    processes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    burstTimes = [10, 5, 8, 15, 12, 13, 14, 15, 17, 4]
    FCFS(processes, burstTimes)
