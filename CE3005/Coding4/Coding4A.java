package Coding4;

import java.util.Scanner;

public class Coding4A {
    public static void main(String[] Args) {
        Scanner myObj = new Scanner(System.in);
        UglyNumber uglyNumber = new UglyNumber();

        int runTimes = myObj.nextInt();

        for (int i = 0; i < runTimes; i++) {
            int inNum = myObj.nextInt();
            uglyNumber.FindFlag(inNum);
        }

        myObj.close();
    }
}


class UglyNumber {

    public void FindFlag(int a) {

        // Set "count" equals to 1 because 1 also is uglynumber.
        int count = 1;
        
        // Then start counting from 2
        int num = 2;
    
        while (true) {
    
            int b = num;

            // The domain of "Ugly Number" is that only divided into 2, 3, 5.
            while (b % 2 == 0) {
                b = b / 2;
            }

            while (b % 3 == 0) {
                b = b / 3;
            }

            while (b % 5 == 0) {
                b = b / 5;
            }
    
            if (b == 1) {
                count++;
            }

            if (count == a) {
                System.out.println(num);
                break;
            } else {
                num++;
            }
        }
    }
}