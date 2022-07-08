package Coding5;

import java.util.ArrayList;
import java.util.Scanner;

public class Coding5A {
    public static void main(String[] Args) {
        Scanner myObj = new Scanner(System.in);

        int runTimes = myObj.nextInt();

        for (int i = 0; i < runTimes; i++) {
            ArrayList<Integer> xValue = new ArrayList<>();
            ArrayList<Integer> yValue = new ArrayList<>();
            int num = myObj.nextInt();
            for (int j = 0; j < num; j++) {
                int x = myObj.nextInt();
                xValue.add(x);
                int y = myObj.nextInt();
                yValue.add(y);
            }
            ClosestPairOf2DPoints closestPairOf2DPoints = new ClosestPairOf2DPoints(xValue, yValue);
        }

        myObj.close();
    }
}


class ClosestPairOf2DPoints {
    private ArrayList<Integer> xValue;
    private ArrayList<Integer> yValue;

    public ClosestPairOf2DPoints(ArrayList<Integer> xValue, ArrayList<Integer> yValue) {
        this.xValue = xValue;
        this.yValue = yValue;
    }

    public void sortPoint() {
        
    }
}