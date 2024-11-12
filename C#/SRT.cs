using System;
using System.Diagnostics;

public class SRT_
{
	static void FindWaitingTime(int[] processes, int[] burstTimes, int[] waitingTimes, int quantum) {
		int n = processes.Length;
		int[] remainingBurstTimes = new int[n];
		Array.Copy(burstTimes, remainingBurstTimes, n);
		int t = 0;
		while (true) {
			bool done = true;
			for (int i = 0; i < n; i++) {
				if (remainingBurstTimes[i] > 0) {
					done = false;
					if (remainingBurstTimes[i] > quantum) {
						t += quantum;
						remainingBurstTimes[i] -= quantum;
					}
					else {
						t += remainingBurstTimes[i];
						waitingTimes[i] = t - burstTimes[i];
						remainingBurstTimes[i] = 0;
					}
				}
			}
			if (done)
				break;
		}
	}

	static void FindTurnAroundTime(int[] processes, int[] burstTimes, int[] waitingTimes, int[] turnaroundTime) {
		int n = processes.Length;
		for (int i = 0; i < n; i++)
			turnaroundTime[i] = burstTimes[i] + waitingTimes[i];
	}

	static void SRT(int[] processes, int[] burstTimes, int quantum) {
		int n = processes.Length;
		int[] waitingTimes = new int[n];
		int[] turnaroundTime = new int[n];
		var stopwatch = Stopwatch.StartNew();
		FindWaitingTime(processes, burstTimes, waitingTimes, quantum);
		FindTurnAroundTime(processes, burstTimes, waitingTimes, turnaroundTime);
		stopwatch.Stop();
		double totalWt = 0, totalTurnaroundTime = 0;
		for (int i = 0; i < n; i++) {
			totalWt += waitingTimes[i];
			totalTurnaroundTime += turnaroundTime[i];
		}
		double avgWt = totalWt / n;
		double avgTt = totalTurnaroundTime / n;
		double throughput = n / stopwatch.Elapsed.TotalSeconds;
		Console.WriteLine("Processes Burst Time Waiting Time Turn-Around Time");
		for (int i = 0; i < n; i++)
			Console.WriteLine($" {processes[i]}        {burstTimes[i]}        {waitingTimes[i]}          {turnaroundTime[i]}");
		Console.WriteLine($"\nAverage waiting time = {avgWt:F5}");
		Console.WriteLine($"Average turn around time = {avgTt:F5}");
		Console.WriteLine($"Throughput = {throughput}");
		Console.WriteLine($"Running time = {stopwatch.Elapsed.TotalSeconds:F5} seconds");
	}

	public static void Main() {
		int[] processes = { 1, 2, 3 };
		int[] burst_time = { 10, 5, 8 };
		int quantum = 2;
		SRT(processes, burst_time, quantum);
	}
}
