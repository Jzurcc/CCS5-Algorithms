class FCFS_Algorithm 
{
    static void findWaitingTime(int[] processes, int n, int[] bt, int[] wt) 
    {
        wt[0] = 0;
        for (int i = 1; i < n; i++) 
        {
            wt[i] = bt[i - 1] + wt[i - 1];
        }
    }

    static void findTurnAroundTime(int[] processes, int n, int[] bt, int[] wt, int[] tat) 
    {
        for (int i = 0; i < n; i++) 
        {
            tat[i] = bt[i] + wt[i];
        }
    }

    static void FCFS(int[] processes, int n, int[] bt)
    {
        int[] wt = new int[n];
        int[] tat = new int[n];
        int total_wt = 0, total_tat = 0;

        findWaitingTime(processes, n, bt, wt);
        findTurnAroundTime(processes, n, bt, wt, tat);

        Console.Write("Processes Burst time Waiting time Turn around time\n");
        for (int i = 0; i < n; i++)
        {
            total_wt += wt[i];
            total_tat += tat[i];
            Console.Write(" {0} ", (i + 1));
            Console.Write("     {0} ", bt[i]);
            Console.Write("     {0}", wt[i]);
            Console.Write("     {0}\n", tat[i]);
        }
        float s = (float)total_wt / n;
        int t = total_tat / n;
        Console.Write("Average waiting time = {0}", s);
        Console.Write("\n");
        Console.Write("Average turn around time = {0} ", t);
    }

    public static void Main(String[] args)
    {
        int[] processes = {1, 2, 3};
        int n = processes.Length;
        int[] burst_time = {10, 5, 8};
        FCFS(processes, n, burst_time);
    }
}
