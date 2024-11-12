using System.Diagnostics;

class Process {
    public int id;
    public int at, bt, wt, tt;
    public int completed;
    public float ntt;
}

class HRRN_ {
    public static void HRRN(int[] processes, int[] arrivalTimes, int[] burstTimes) {
        int n = processes.Length;
        int sum_bt = 0;
        float avg_wt = 0, avg_tt = 0;

        Process[] p = new Process[n];
        for (int i = 0; i < n; i++) {
            p[i] = new Process { id = processes[i], at = arrivalTimes[i], bt = burstTimes[i], completed = 0 };
            sum_bt += p[i].bt;
        }

        Stopwatch stopwatch = Stopwatch.StartNew();
        float t = p[0].at;

        while (t < sum_bt) {
            float hrr = -1;
            int loc = -1;

            for (int i = 0; i < n; i++) {
                if (p[i].at <= t && p[i].completed == 0) {
                    float response_ratio = (p[i].bt + (t - p[i].at)) / p[i].bt;
                    if (hrr < response_ratio) {
                        hrr = response_ratio;
                        loc = i;
                    }
                }
            }

            t += p[loc].bt;
            p[loc].wt = (int)(t - p[loc].at - p[loc].bt);
            p[loc].tt = (int)(t - p[loc].at);
            avg_tt += p[loc].tt;
            p[loc].ntt = (float)p[loc].tt / p[loc].bt;
            p[loc].completed = 1;
            avg_wt += p[loc].wt;
        }

        stopwatch.Stop();
        double runningTime = stopwatch.Elapsed.TotalSeconds;
        double throughput = n / runningTime;

        Console.WriteLine("PN\tAT\tBT\tWT\tTAT\tNTT");
        for (int i = 0; i < n; i++) {
            Console.WriteLine($"{p[i].id}\t{p[i].at}\t{p[i].bt}\t{p[i].wt}\t{p[i].tt}\t{p[i].ntt:F6}");
        }

        Console.WriteLine($"Average waiting time: {avg_wt / n:F6}");
        Console.WriteLine($"Average turnaround time: {avg_tt / n:F6}");
        Console.WriteLine($"Running time: {runningTime:F6} seconds");
        Console.WriteLine($"Throughput: {throughput:F6} processes per second");
    }

    static void Main() {
        int[] processes = { 1, 2, 3, 4, 5 };
        int[] arrivalTimes = { 0, 2, 4, 6, 8 };
        int[] burstTimes = { 3, 6, 4, 5, 2 };
        HRRN(processes, arrivalTimes, burstTimes);
    }
}
