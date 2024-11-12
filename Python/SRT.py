import time

def findWaitingTime(processes, burstTimes, waitingTimes, quantum):
	n = len(processes)
	rem_bt = burstTimes[:]
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
					waitingTimes[i] = t - burstTimes[i]
					rem_bt[i] = 0
		if done:
			break

def findTurnAroundTime(processes, burstTimes, waitingTimes, turnaroundTime):
	n = len(processes)
	for i in range(n):
		turnaroundTime[i] = burstTimes[i] + waitingTimes[i]

def SRT(processes, burstTimes, quantum):
	n = len(processes)
	waitingTimes = [0] * n
	turnaroundTime = [0] * n
	startTime = time.time()
	findWaitingTime(processes, burstTimes, waitingTimes, quantum)
	findTurnAroundTime(processes, burstTimes, waitingTimes, turnaroundTime)
	endTime = time.time()
	totalWt = sum(waitingTimes)
	totalTt = sum(turnaroundTime)
	avgWt = totalWt / n
	avgTt = totalTt / n
	throughput = n / (endTime - startTime)
	print("Processes Burst Time Waiting Time Turn-Around Time")
	for i in range(n):
		print(f" {processes[i]}        {burstTimes[i]}        {waitingTimes[i]}          {turnaroundTime[i]}")
	print(f"\nAverage waiting time = {avgWt:.5f}")
	print(f"Average turn around time = {avgTt:.5f}")
	print(f"Throughput = {throughput}")
	print(f"Running time = {endTime - startTime:.5f} seconds")

if __name__ == "__main__":
	processes = [1, 2, 3]
	burst_time = [10, 5, 8]
	quantum = 2
	SRT(processes, burst_time, quantum)
