import java.util.Arrays;

class Process {
    int id, at, bt, wt, tt;
    int completed;
    float ntt;
}

public class HRRN {
    public static void hrrn(int[] processes, int[] arrivalTimes, int[] burstTimes) {
        int n = processes.length;
        int sum_bt = Arrays.stream(burstTimes).sum();
        float avg_wt = 0, avg_tt = 0;

        Process[] p = new Process[n];
        for (int i = 0; i < n; i++) {
            p[i] = new Process();
            p[i].id = processes[i];
            p[i].at = arrivalTimes[i];
            p[i].bt = burstTimes[i];
            p[i].completed = 0;
        }

        long startTime = System.nanoTime();
        float t = Arrays.stream(arrivalTimes).min().getAsInt();

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
            p[loc].wt = (int) (t - p[loc].at - p[loc].bt);
            p[loc].tt = (int) (t - p[loc].at);
            avg_tt += p[loc].tt;
            p[loc].ntt = (float) p[loc].tt / p[loc].bt;
            p[loc].completed = 1;
            avg_wt += p[loc].wt;
        }

        long endTime = System.nanoTime();
        double runningTime = (endTime - startTime) / 1e9;
        double throughput = n / runningTime;

        System.out.println("PN\tAT\tBT\tWT\tTAT\tNTT");
        for (int i = 0; i < n; i++) {
            System.out.printf("%d\t%d\t%d\t%d\t%d\t%.6f\n", p[i].id, p[i].at, p[i].bt, p[i].wt, p[i].tt, p[i].ntt);
        }

        System.out.printf("Average waiting time: %.6f\n", avg_wt / n);
        System.out.printf("Average turnaround time: %.6f\n", avg_tt / n);
        System.out.printf("Running time: %.6f seconds\n", runningTime);
        System.out.printf("Throughput: %.6f processes per second\n", throughput);
    }

    public static void main(String[] args) {
        int[] processes = { 1, 2, 3, 4, 5 };
        int[] arrivalTimes = { 0, 2, 4, 6, 8 };
        int[] burstTimes = { 3, 6, 4, 5, 2 };
        hrrn(processes, arrivalTimes, burstTimes);
    }
}
