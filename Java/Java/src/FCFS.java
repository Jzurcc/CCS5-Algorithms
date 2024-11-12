import java.text.ParseException;

class FCFS {

    static void findWaitingTime(int processes[], int n, int burstTimes[], int waitingTimes[]) {
        waitingTimes[0] = 0;
        for (int i = 1; i < n; i++) {
            waitingTimes[i] = burstTimes[i - 1] + waitingTimes[i - 1];
        }
    }

    static void findTurnAroundTime(int processes[], int n, int burstTimes[], int waitingTimes[], int turnaroundTimes[]) {
        for (int i = 0; i < n; i++) {
            turnaroundTimes[i] = burstTimes[i] + waitingTimes[i];
        }
    }

    static void _FCFS(int processes[], int burstTimes[]) {
        int n = processes.length;
        int waitingTimes[] = new int[n], turnaroundTimes[] = new int[n];
        int totalWt = 0, totalTt = 0;

        findWaitingTime(processes, n, burstTimes, waitingTimes);
        findTurnAroundTime(processes, n, burstTimes, waitingTimes, turnaroundTimes);

        System.out.printf("Processes Burst time Waiting time Turn around time\n");
        for (int i = 0; i < n; i++) {
            totalWt += waitingTimes[i];
            totalTt += turnaroundTimes[i];
            System.out.printf(" %d      %d      %d     %d\n", (i + 1), burstTimes[i], waitingTimes[i], turnaroundTimes[i]);
        }
        float avgWt = (float) totalWt / n;
        int avgTt = totalTt / n;
        System.out.printf("Average waiting time = %f\nAverage turn around time = %d ", avgWt, avgTt);
    }

    public static void main(String[] args) throws ParseException {
        int processes[] = {1, 2, 3};
        int burstTimes[] = {10, 5, 8};
        _FCFS(processes, burstTimes);
    }
}
