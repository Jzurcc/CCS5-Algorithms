class FCFS_ 
{
    static void findWaitingTime(int n, int[] burstTimes, int[] Wt) {
        Wt[0] = 0;
        for (int i = 1; i < n; i++) {
            Wt[i] = burstTimes[i - 1] + Wt[i - 1];
        }
    }

    static void findTurnAroundTime(int n, int[] burstTimes, int[] Wt, int[] Tt) {
        for (int i = 0; i < n; i++) {
            Tt[i] = burstTimes[i] + Wt[i];
        }
    }

    static void FCFS(int[] processes, int[] burstTimes) {
        int n = processes.Length;
        int[] Wt = new int[n];
        int[] Tt = new int[n];
        int totalWt = 0, totalTt = 0;

        findWaitingTime(n, burstTimes, Wt);
        findTurnAroundTime(n, burstTimes, Wt, Tt);

        Console.Write("Processes Burst time Waiting time Turn around time\n");
        for (int i = 0; i < n; i++) {
            totalWt += Wt[i];
            totalTt += Tt[i];
            Console.WriteLine(" {0}      {1}      {2}     {3}", i + 1, burstTimes[i], Wt[i], Tt[i]);
        }
        float avgWt = (float)totalWt / n;
        int avgTt = totalTt / n;
        Console.Write("Average waiting time = {0}\nAverage turn around time = {1} ", avgWt, avgTt);
    }

    public static void Main(String[] args) {
        int[] processes = {1, 2, 3};
        int[] burst_time = {10, 5, 8};
        FCFS(processes, burst_time);
    }
}
