package Coding2;

import java.util.Scanner;


public class Coding2B {
    public static void main(String[] Args) {
        Scanner myObj = new Scanner(System.in);

        int runTimes = myObj.nextInt();

        for (int i = 0; i < runTimes; i++) {
            int inNum = myObj.nextInt();
            Fibonacci fibonacci = new Fibonacci(inNum);
            fibonacci.recursiveFibonacci(inNum);
            fibonacci.showAns();
            
        }

        myObj.close();
    }
}


class Fibonacci {
    private int n;

    public Fibonacci(int n) {
        this.n = n;
    }

    public int recursiveFibonacci(int n) {
        if (n == 1) {
            return 1;
        } else if (n == 2) {
            return 1;
        }
        return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2);
    }

    public void showAns() {
        System.out.println(recursiveFibonacci(n));
    }
}