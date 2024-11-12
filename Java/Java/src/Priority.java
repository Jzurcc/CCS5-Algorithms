import java.util.*;

class Process {
    int pid;
    int burstTime;
    int priority;

    Process(int pid, int burstTime, int priority) {
        this.pid = pid;
        this.burstTime = burstTime;
        this.priority = priority;
    }

    public int getPriority() {
        return priority;
    }
}

public class Priority {
    public void findWaitingTime(Process[] processes, int n, int[] wt) {
        wt[0] = 0;
        for (int i = 1; i < n; i++)
            wt[i] = processes[i - 1].burstTime + wt[i - 1];
    }

    public void findTurnAroundTime(Process[] processes, int n, int[] wt, int[] tat) {
        for (int i = 0; i < n; i++)
            tat[i] = processes[i].burstTime + wt[i];
    }

    public void calculateTimes(Process[] processes, int n) {
        int[] wt = new int[n], tat = new int[n];
        int totalWt = 0, totalTt = 0;

        long startTime = System.nanoTime();

        findWaitingTime(processes, n, wt);
        findTurnAroundTime(processes, n, wt, tat);

        long endTime = System.nanoTime();
        double runningTime = (endTime - startTime) / 1_000_000_000.0;
        double throughput = n / runningTime;

        System.out.println("\nProcesses Burst Time Waiting Time Turn-Around Time");
        for (int i = 0; i < n; i++) {
            totalWt += wt[i];
            totalTt += tat[i];
            System.out.println(" " + processes[i].pid + "\t\t" + processes[i].burstTime + "\t " + wt[i] + "\t\t " + tat[i]);
        }

        double avgWt = (double) totalWt / n;
        double avgTt = (double) totalTt / n;

        System.out.println("\nAverage waiting time = " + avgWt);
        System.out.println("Average turn-around time = " + avgTt);
        System.out.println("Throughput = " + throughput);
        System.out.println("Running time = " + runningTime + " seconds");
    }

    public void _Priority(Process[] processes, int n) {
        Arrays.sort(processes, (a, b) -> b.getPriority() - a.getPriority());
        System.out.println("Order in which processes get executed:");
        for (Process process : processes)
            System.out.print(process.pid + " ");
        System.out.println();

        calculateTimes(processes, n);
    }

    public static void main(String[] args) {
        Process[] processes = {
            new Process(1, 10, 2),
            new Process(2, 5, 0),
            new Process(3, 8, 1)
        };
        new Priority()._Priority(processes, processes.length);
    }
}
