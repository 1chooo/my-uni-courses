package Coding1;

import java.util.Scanner;

public class Coding1A {
    public static void main(String[] Args) {
        Scanner myObj = new Scanner(System.in);
        
        int runTimes = myObj.nextInt();

        for (int i = 1; i <= runTimes; i++) {
            int sum = 0;
            int a = myObj.nextInt();
            int b = myObj.nextInt();

            OddSum oddSum = new OddSum(a, b, sum);
            oddSum.showAns(i);
        }

        myObj.close();
    }
}


class OddSum {
    private int a;
    private int b;
    private int sum;

    public OddSum(int a, int b, int sum) {
        this.a = a;
        this.b = b;
        this.sum = sum;
    }

    public void countOddSum() {
        for (int i = a; i <= b; i++) if (i % 2 == 1) sum += i;
    }

    public void showAns(int num) {
        countOddSum();
        
        System.out.printf("Case %d: %d%n", num, sum);
    }
}