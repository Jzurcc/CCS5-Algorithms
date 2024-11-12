// using System;
// using System.Diagnostics;

// class Process 
// {
//     public int pid;
//     public int burstTime;
//     public int priority;

//     public Process(int pid, int burstTime, int priority)
//     {
//         this.pid = pid;
//         this.burstTime = burstTime;
//         this.priority = priority;
//     }

//     public int Prior => priority;
// }

// class GFG 
// {
//     public void FindWaitingTime(Process[] processes, int n, int[] wt)
//     {
//         wt[0] = 0;
//         for (int i = 1; i < n; i++)
//             wt[i] = processes[i - 1].burstTime + wt[i - 1];
//     }

//     public void FindTurnAroundTime(Process[] processes, int n, int[] wt, int[] tat)
//     {
//         for (int i = 0; i < n; i++)
//             tat[i] = processes[i].burstTime + wt[i];
//     }

//     public void CalculateTimes(Process[] processes, int n)
//     {
//         int[] wt = new int[n];
//         int[] tat = new int[n];
//         int totalWt = 0, totalTt = 0;
//         var stopwatch = Stopwatch.StartNew();

//         FindWaitingTime(processes, n, wt);
//         FindTurnAroundTime(processes, n, wt, tat);

//         stopwatch.Stop();
//         double runningTime = stopwatch.Elapsed.TotalSeconds;
//         double throughput = n / runningTime;

//         Console.WriteLine("\nProcesses Burst Time Waiting Time Turn Around Time");
//         for (int i = 0; i < n; i++)
//         {
//             totalWt += wt[i];
//             totalTt += tat[i];
//             Console.WriteLine(" " + processes[i].pid + "\t\t" + processes[i].burstTime + "\t " + wt[i] + "\t\t " + tat[i]);
//         }

//         double avgWt = (double)totalWt / n;
//         double avgTt = (double)totalTt / n;

//         Console.WriteLine("\nAverage waiting time = " + avgWt);
//         Console.WriteLine("Average turn-around time = " + avgTt);
//         Console.WriteLine("Throughput = " + throughput);
//         Console.WriteLine("Running time = " + runningTime + " seconds");
//     }

//     public void Priority(Process[] processes, int[] burstTimes)
//     {
//         int n = processes.Length;
//         Array.Sort(processes, (a, b) => b.Prior.CompareTo(a.Prior));
//         Console.WriteLine("Order in which processes get executed:");
//         foreach (var process in processes)
//             Console.Write(process.pid + " ");
//         Console.WriteLine();
        
//         CalculateTimes(processes, n);
//     }

//     static void Main(string[] args)
//     {
//         Process[] processes = {
//             new Process(1, 10, 2),
//             new Process(2, 5, 0),
//             new Process(3, 8, 1)
//         };
//         new GFG().Priority(processes, [5, 8, 10]);
//     }
// }
