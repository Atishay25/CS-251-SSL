package Q2;
import java.util.Scanner;

public class Main {

    /*
     * NOTE: Create helper functions here if required
     */

    // Function to run all testcases
    public static int run(int testcase, Scanner input){
        if(testcase <= 0) return 0;
        else{
            int n = input.nextInt();
            int arr[] = new int[n];
            getArray(arr, n, input);
            int sqaureSum = square(0,0,arr);
            System.out.println(sqaureSum);
            return run(testcase-1,input);
        }
    }

    // Function to get elements of array using Recursion
    public static int getArray(int[] arr, int n, Scanner input){
        if(n <= 0) return 0;
        else{
            arr[n-1] = input.nextInt();
            return getArray(arr, n-1, input);
        }
    }

    // Function to square elements of array without using Recursion
    public static int square(int sum ,int  n,int[] arr){
        if(n < arr.length){
            sum += arr[n]*arr[n];
            return square(sum,n+1,arr);
        }
        else{
            return sum;
        }
    }
    
    public static void main(String args[]) {
        /*
         * Complete this method
         * NOTE: Take input from STDIN and print the output to STDOUT
         */

        Scanner input = new Scanner(System.in);
        int testcases = input.nextInt();
        run(testcases,input);
        input.close();
    }
}
