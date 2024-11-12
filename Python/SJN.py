import time

def SJN(processes, burstTimes):
    n = len(processes)
    A = [[0 for j in range(4)] for i in range(n)]
    totalWt, totalTt = 0, 0

    for i in range(n):
        A[i][0] = processes[i]
        A[i][1] = burstTimes[i]

    for i in range(n):
        index = i
        for j in range(i + 1, n):
            if A[j][1] < A[index][1]:
                index = j
        A[i][1], A[index][1] = A[index][1], A[i][1]
        A[i][0], A[index][0] = A[index][0], A[i][0]

    startTime = time.time()

    A[0][2] = 0
    for i in range(1, n):
        A[i][2] = sum(A[j][1] for j in range(i))
        totalWt += A[i][2]

    for i in range(n):
        A[i][3] = A[i][1] + A[i][2]
        totalTt += A[i][3]

    avgWt = totalWt / n
    avgTt = totalTt / n
    endTime = time.time()
    runningTime = endTime - startTime
    throughput = n / runningTime

    print("Processes Burst Time Waiting Time Turnaround Time")
    for i in range(n):
        print(f"P{A[i][0]}\t\t{A[i][1]}\t\t{A[i][2]}\t\t{A[i][3]}")

    print(f"\nAverage Waiting Time= {avgWt}")
    print(f"Average Turnaround Time= {avgTt}")
    print("Throughput =", throughput)
    print("Running time =", endTime - startTime, "seconds")

if __name__ == "__main__":
    processes = [1, 2, 3]
    burstTimes = [10, 5, 8]
    SJN(processes, burstTimes)
