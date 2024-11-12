namespace Main
{
    class Program
    {
        static void Main(string[] args)
        {
            int[,] A = new int[100, 4];
            int n;
            int total = 0;
            float avg_wt, avg_tat;
            Console.WriteLine("Enter number of process:");
            n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Enter Burst Time:");
            for (int i = 0; i < n; i++)
            {
                Console.Write("P" + (i + 1) + ": ");
                A[i, 1] = Convert.ToInt32(Console.ReadLine());
                A[i, 0] = i + 1;
            }
            for (int i = 0; i < n; i++)
            {
                int index = i;
                for (int j = i + 1; j < n; j++)
                {
                    if (A[j, 1] < A[index, 1])
                    {
                        index = j;
                    }
                }
                int temp = A[i, 1];
                A[i, 1] = A[index, 1];
                A[index, 1] = temp;
                temp = A[i, 0];
                A[i, 0] = A[index, 0];
                A[index, 0] = temp;
            }
            A[0, 2] = 0;
            for (int i = 1; i < n; i++)
            {
                A[i, 2] = 0;
                for (int j = 0; j < i; j++)
                {
                    A[i, 2] += A[j, 1];
                }
                total += A[i, 2];
            }
            avg_wt = (float)total / n;
            total = 0;
            Console.WriteLine("P\tBT\tWT\tTAT");
            for (int i = 0; i < n; i++)
            {
                A[i, 3] = A[i, 1] + A[i, 2];
                total += A[i, 3];
                Console.WriteLine("P" + A[i, 0] + "\t" + A[i, 1] + "\t" + A[i, 2] + "\t" + A[i, 3]);
            }
            avg_tat = (float)total / n;
            Console.WriteLine("Average Waiting Time= " + avg_wt);
            Console.WriteLine("Average Turnaround Time= " + avg_tat);
        }
    }
}
