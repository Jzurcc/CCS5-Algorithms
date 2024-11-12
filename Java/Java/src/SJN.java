public class SJN {
    public static void sjn(int[] processes, int[] burstTimes) {
        int n = processes.length;
        int[][] processInfo = new int[100][4];
        int total = 0;
        float avgWt, avgTat;

        for (int i = 0; i < n; i++) {
            processInfo[i][1] = burstTimes[i];
            processInfo[i][0] = processes[i];
        }

        for (int i = 0; i < n; i++) {
            int index = i;
            for (int j = i + 1; j < n; j++) {
                if (processInfo[j][1] < processInfo[index][1]) {
                    index = j;
                }
            }
            int temp = processInfo[i][1];
            processInfo[i][1] = processInfo[index][1];
            processInfo[index][1] = temp;
            temp = processInfo[i][0];
            processInfo[i][0] = processInfo[index][0];
            processInfo[index][0] = temp;
        }

        processInfo[0][2] = 0;
        for (int i = 1; i < n; i++) {
            processInfo[i][2] = 0;
            for (int j = 0; j < i; j++) {
                processInfo[i][2] += processInfo[j][1];
            }
            total += processInfo[i][2];
        }
        avgWt = (float) total / n;
        total = 0;

        System.out.println("P\tBT\tWT\tTAT");
        for (int i = 0; i < n; i++) {
            processInfo[i][3] = processInfo[i][1] + processInfo[i][2];
            total += processInfo[i][3];
            System.out.println("P" + processInfo[i][0] + "\t" + processInfo[i][1] + "\t" + processInfo[i][2] + "\t" + processInfo[i][3]);
        }
        avgTat = (float) total / n;

        System.out.println("Average Waiting Time= " + avgWt);
        System.out.println("Average Turnaround Time= " + avgTat);
    }

    public static void main(String[] args) {
        int[] processes = {1, 2, 3};
        int[] burstTimes = {10, 5, 8};
        sjn(processes, burstTimes);
    }
}
