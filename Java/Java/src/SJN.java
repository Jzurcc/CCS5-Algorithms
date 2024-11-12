public class SJN {
	public static void sjn(int[] processes, int[] burstTimes) {
		int n = processes.length;
		int[][] A = new int[100][4];
		int total = 0;
		float avgWt, avgTat;

		for (int i = 0; i < n; i++) {
			A[i][1] = burstTimes[i];
			A[i][0] = processes[i];
		}

		for (int i = 0; i < n; i++) {
			int index = i;
			for (int j = i + 1; j < n; j++) {
				if (A[j][1] < A[index][1]) {
					index = j;
				}
			}
			int temp = A[i][1];
			A[i][1] = A[index][1];
			A[index][1] = temp;
			temp = A[i][0];
			A[i][0] = A[index][0];
			A[index][0] = temp;
		}

		A[0][2] = 0;
		for (int i = 1; i < n; i++) {
			A[i][2] = 0;
			for (int j = 0; j < i; j++) {
				A[i][2] += A[j][1];
			}
			total += A[i][2];
		}
		avgWt = (float) total / n;
		total = 0;

		System.out.println("P\tBT\tWT\tTAT");
		for (int i = 0; i < n; i++) {
			A[i][3] = A[i][1] + A[i][2];
			total += A[i][3];
			System.out.println("P" + A[i][0] + "\t" + A[i][1] + "\t" + A[i][2] + "\t" + A[i][3]);
		}
		avgTat = (float) total / n;

		System.out.println("Average Waiting Time= " + avgWt);
		System.out.println("Average Turnaround Time= " + avgTat);
	}

	public static void main(String[] args) {
		int[] processes = {1, 2, 3};
		int[] burstTimes = {10, 5, 8};
		sjn(processes, burstTimes);
	}
}
