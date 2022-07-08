package Coding1;

import java.util.Scanner;

public class Coding1C {
    public static void main(String[] Args) {
        Scanner myObj = new Scanner(System.in);

        int runTimes = myObj.nextInt();
        myObj.nextLine();

        for (int i = 0; i < runTimes; i++) {
            String inStr = myObj.nextLine();
            ColumnNumber columnNumber = new ColumnNumber(inStr);
            columnNumber.showAns();
        }

        myObj.close();
    }
}


class ColumnNumber {
    private String inStr;

    public ColumnNumber(String inStr) {
        this.inStr = inStr;
    }

    public void showAns() {
        int len = inStr.length();
        int outNum;
        int sum = 0;
        char out;
        for (int i = 0; i < len; i++) {
            out = inStr.charAt(i);
            // Turn into ASCII code
            outNum = (out - 64);
            sum += outNum * Math.pow(26, (len - 1) - i);
        }

        System.out.println(sum);
    }
}