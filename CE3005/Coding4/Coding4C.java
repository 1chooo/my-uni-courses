package Coding4;

import java.util.Scanner;

public class Coding4C {
    public static void main(String[] Args) {
        Scanner myObj = new Scanner(System.in);
        
        int runTimes = myObj.nextInt();

        for (int i = 0; i < runTimes; i++) {
            int l = myObj.nextInt();
            int u = myObj.nextInt();
            Divisors divisors = new Divisors();
            divisors.BiggestDivisors(l, u);
        }
        myObj.close();
    }    
}


class Divisors {

    public void BiggestDivisors(int a, int b) {
        int max = 0;
        int divisor = 0;
        int num = 0;
    
        for (int i = a; i < (b + 1); i++) {
            for (int j = 1; j < Math.pow(i, 0.5); j++) {
                if (i % j == 0) {
                    divisor += 2;
                }
            }

            if (divisor > max) {
                max = divisor;
                num = i;
            }
            divisor = 0;
        }
        System.out.printf("Between %d and %d, %d has a maximum of %d divisors.%n", a, b, num, max);
    }
}