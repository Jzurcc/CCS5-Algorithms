using System;
using System.Diagnostics;

public class RR
{
	static void FindWaitingTime(int[] processes, int[] bt, int[] wt, int quantum)
	{
		int n = processes.Length;
		int[] rem_bt = new int[n];
		Array.Copy(bt, rem_bt, n);
		int t = 0;
		while (true)
		{
			bool done = true;
			for (int i = 0; i < n; i++)
			{
				if (rem_bt[i] > 0)
				{
					done = false;
					if (rem_bt[i] > quantum)
					{
						t += quantum;
						rem_bt[i] -= quantum;
					}
					else
					{
						t += rem_bt[i];
						wt[i] = t - bt[i];
						rem_bt[i] = 0;
					}
				}
			}
			if (done)
				break;
		}
	}

	static void FindTurnAroundTime(int[] processes, int[] bt, int[] wt, int[] tat)
	{
		int n = processes.Length;
		for (int i = 0; i < n; i++)
			tat[i] = bt[i] + wt[i];
	}

	static void _RR(int[] processes, int[] bt, int quantum)
	{
		int n = processes.Length;
		int[] wt = new int[n];
		int[] tat = new int[n];
		var stopwatch = Stopwatch.StartNew();
		FindWaitingTime(processes, bt, wt, quantum);
		FindTurnAroundTime(processes, bt, wt, tat);
		stopwatch.Stop();
		double total_wt = 0, total_tat = 0;
		for (int i = 0; i < n; i++)
		{
			total_wt += wt[i];
			total_tat += tat[i];
		}
		double avg_wt = total_wt / n;
		double avg_tat = total_tat / n;
		double throughput = n / stopwatch.Elapsed.TotalSeconds;
		Console.WriteLine("Processes Burst Time Waiting Time Turn-Around Time");
		for (int i = 0; i < n; i++)
			Console.WriteLine($" {processes[i]}        {bt[i]}        {wt[i]}          {tat[i]}");
		Console.WriteLine($"\nAverage waiting time = {avg_wt:F5}");
		Console.WriteLine($"Average turn around time = {avg_tat:F5}");
		Console.WriteLine($"Throughput = {throughput}");
		Console.WriteLine($"Running time = {stopwatch.Elapsed.TotalSeconds:F5} seconds");
	}

	public static void Main()
	{
		int[] processes = { 1, 2, 3 };
		int[] burst_time = { 10, 5, 8 };
		int quantum = 2;
		_RR(processes, burst_time, quantum);
	}
}
