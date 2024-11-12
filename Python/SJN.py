def SJN(processes, burstTime):
    n = len(processes)
    A = [[0 for j in range(4)] for i in range(100)]
    total, avgWt, avgTat = 0, 0, 0

    for i in range(n):
        A[i][1] = burstTime[i]
        A[i][0] = processes[i]

    for i in range(n):
        index = i
        for j in range(i + 1, n):
            if A[j][1] < A[index][1]:
                index = j

        A[i][1], A[index][1] = A[index][1], A[i][1]
        A[i][0], A[index][0] = A[index][0], A[i][0]

    A[0][2] = 0
    for i in range(1, n):
        A[i][2] = sum(A[j][1] for j in range(i))
        total += A[i][2]
    avgWt = total / n

    total = 0
    print("P\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        A[i][3] = A[i][1] + A[i][2]
        total += A[i][3]
        print(f"P{A[i][0]}\t{A[i][1]}\t{A[i][2]}\t{A[i][3]}")
    avgTat = total / n

    print(f"Average Waiting Time= {avgWt}")
    print(f"Average Turnaround Time= {avgTat}")


if __name__ == "__main__":
    processes = [1, 2, 3]
    burstTime = [10, 5, 8]
    SJN(processes, burstTime)
