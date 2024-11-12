public class SRT {

	static void findWaitingTime(int[] processes, int[] bt, int[] wt, int quantum) {
		int n = processes.length;
		int[] rem_bt = bt.clone();
		int t = 0;
		while (true) {
			boolean done = true;
			for (int i = 0; i < n; i++) {
				if (rem_bt[i] > 0) {
					done = false;
					if (rem_bt[i] > quantum) {
						t += quantum;
						rem_bt[i] -= quantum;
					} else {
						t += rem_bt[i];
						wt[i] = t - bt[i];
						rem_bt[i] = 0;
					}
				}
			}
			if (done) break;
		}
	}

	static void findTurnAroundTime(int[] processes, int[] bt, int[] wt, int[] tat) {
		int n = processes.length;
		for (int i = 0; i < n; i++)
			tat[i] = bt[i] + wt[i];
	}

	static void srt(int[] processes, int[] bt, int quantum) {
		int n = processes.length;
		int[] wt = new int[n], tat = new int[n];
		long startTime = System.nanoTime();
		findWaitingTime(processes, bt, wt, quantum);
		findTurnAroundTime(processes, bt, wt, tat);
		long endTime = System.nanoTime();
		double total_wt = 0, total_tat = 0;
		for (int i = 0; i < n; i++) {
			total_wt += wt[i];
			total_tat += tat[i];
		}
		double avg_wt = total_wt / n;
		double avg_tat = total_tat / n;
		double throughput = n / ((endTime - startTime) / 1_000_000_000.0);
		System.out.println("Processes Burst Time Waiting Time Turn-Around Time");
		for (int i = 0; i < n; i++)
			System.out.printf(" %d         %d        %d          %d%n", processes[i], bt[i], wt[i], tat[i]);
		System.out.printf("%nAverage waiting time = %.5f%n", avg_wt);
		System.out.printf("Average turn around time = %.5f%n", avg_tat);
		System.out.printf("Throughput = %.5f%n", throughput);
		System.out.printf("Running time = %.5f seconds%n", (endTime - startTime) / 1_000_000_000.0);
	}

	public static void main(String[] args) {
		int[] processes = {1, 2, 3};
		int[] burst_time = {10, 5, 8};
		int quantum = 2;
		srt(processes, burst_time, quantum);
	}
}
