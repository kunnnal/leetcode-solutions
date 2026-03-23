import java.util.Scanner;

public class MinPartitions {

    // Recursive solution
    private static int solve(String n, int index, int maxVal) {
        // Base case: reached end of string
        if (index == n.length())
            return maxVal;

        // Early exit: max possible value found
        if (maxVal == 9)
            return 9;

        int currDigit = n.charAt(index) - '0';
        int newMax = Math.max(maxVal, currDigit);

        // Recurse to next index
        return solve(n, index + 1, newMax);
    }

    public static int minPartitions(String n) {
        return solve(n, 0, 0);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number (as string): ");
        String n = scanner.nextLine().trim();

        // Input validation
        if (!n.matches("[0-9]+")) {
            System.out.println("Invalid input! Please enter digits only.");
            scanner.close();
            return;
        }

        int result = minPartitions(n);
        System.out.println("Minimum Partitions needed: " + result);

        scanner.close();
    }
}