def findWaitingTime(processes, burstTime, waitingTime):
    n = len(processes)
    waitingTime[0] = 0
    for i in range(1, n):
        waitingTime[i] = burstTime[i - 1] + waitingTime[i - 1]

def findTurnAroundTime(processes, burstTime, waitingTime, turnaroundTime):
    for i in range(len(processes)):
        turnaroundTime[i] = burstTime[i] + waitingTime[i]

def FCFS(processes, burstTime):
    n = len(processes)
    waitingTime = [0] * n
    turnaroundTime = [0] * n
    totalWaitingTime = 0
    totalTurnaroundTime = 0
    findWaitingTime(processes, n, burstTime, waitingTime)
    findTurnAroundTime(processes, n, burstTime, waitingTime, turnaroundTime)
    print("Processes Burst time Waiting time Turn around time")
    for i in range(n):
        totalWaitingTime += waitingTime[i]
        totalTurnaroundTime += turnaroundTime[i]
        print(" " + str(i + 1) + "\t\t" + str(burstTime[i]) + "\t " + str(waitingTime[i]) + "\t\t " + str(turnaroundTime[i]))
    print("Average waiting time =", str(totalWaitingTime / n))
    print("Average turn around time =", str(totalTurnaroundTime / n))

if __name__ == "__main__":
    processes = [1, 2, 3]
    n = len(processes)
    burstTime = [10, 5, 8]
    FCFS(processes, burstTime)