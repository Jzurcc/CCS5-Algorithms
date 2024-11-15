import time

def findWaitingTime(processes, burst_times, arrival_times, wt, quantum):
	n = len(processes)
	rt = burst_times.copy()
	complete = 0
	t = 0
	minm = float('inf')
	short = 0
	check = False

	while complete != n:
		for j in range(n):
			if arrival_times[j] <= t and rt[j] < minm and rt[j] > 0:
				minm = rt[j]
				short = j
				check = True
		if not check:
			t += 1
			continue

		rt[short] -= 1
		minm = rt[short] if rt[short] > 0 else float('inf')

		if rt[short] == 0:
			complete += 1
			check = False
			fint = t + 1
			wt[short] = fint - burst_times[short] - arrival_times[short]
			if wt[short] < 0:
				wt[short] = 0
		t += 1

	return t  # Total running time

def findTurnAroundTime(burst_times, wt, tat):
	n = len(burst_times)
	for i in range(n):
		tat[i] = burst_times[i] + wt[i]

def findavgTime(processes, burst_times, arrival_times, quantum):
	n = len(processes)
	wt = [0] * n
	tat = [0] * n

	start_time = time.time()
	total_running_time = findWaitingTime(processes, burst_times, arrival_times, wt, quantum)
	findTurnAroundTime(burst_times, wt, tat)
	end_time = time.time()

	print("Processes    Burst Time     Waiting Time    Turn-Around Time")
	total_wt = 0
	total_tat = 0
	for i in range(n):
		total_wt += wt[i]
		total_tat += tat[i]
		print(f" {processes[i]}           {burst_times[i]}            {wt[i]}            {tat[i]}")

	avg_wt = total_wt / n
	avg_tat = total_tat / n
	throughput = n / total_running_time
	running_duration = end_time - start_time

	print("\nAverage waiting time = %.5f" % avg_wt)
	print("Average turn around time = %.5f" % avg_tat)
	print("Total running time (CPU clock time) = %.5f seconds" % running_duration)
	print("Throughput = %.5f processes per time unit" % throughput)

if __name__ == "__main__":
	processes = [1, 2, 3, 4]
	burst_times = [6, 8, 7, 3]
	arrival_times = [1, 1, 2, 3]
	quantum = 2
	findavgTime(processes, burst_times, arrival_times, quantum)
