import time

def HRRN(processes, bt, at):
	n = len(processes)
	sum_bt = sum(bt)
	avg_wt = 0
	avg_tt = 0

	completed = [0] * n
	waiting_time = [0] * n
	turnaround_time = [0] * n
	normalised_tt = [0] * n

	start_time = time.time()
	t = min(at)

	while t < sum_bt:
		hrr = -1
		loc = 0

		for i in range(n):
			if at[i] <= t and not completed[i]:
				response_ratio = (bt[i] + (t - at[i])) / bt[i]
				if hrr < response_ratio:
					hrr = response_ratio
					loc = i

		t += bt[loc]
		waiting_time[loc] = t - at[loc] - bt[loc]
		turnaround_time[loc] = t - at[loc]
		avg_tt += turnaround_time[loc]
		normalised_tt[loc] = turnaround_time[loc] / bt[loc]
		completed[loc] = 1
		avg_wt += waiting_time[loc]

	end_time = time.time()
	running_time = end_time - start_time
	throughput = n / running_time

	print("Process Arrival Burst Waiting Turnaround Normalized TT")
	for i in range(n):
		print(f"{processes[i]}      {at[i]}      {bt[i]}     {waiting_time[i]}     {turnaround_time[i]}     {normalised_tt[i]:.6f}")
	print(f"Average waiting time: {avg_wt / n:.6f}")
	print(f"Average turnaround time: {avg_tt / n:.6f}")
	print(f"Running time: {running_time:.6f} seconds")
	print(f"Throughput: {throughput:.6f} processes per second")

if __name__ == '__main__':
	processes = [1, 2, 3, 4, 5]
	at = [0, 2, 4, 6, 8]
	bt = [3, 6, 4, 5, 2]
	HRRN(processes, at, bt)
