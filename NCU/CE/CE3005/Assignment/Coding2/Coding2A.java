package Coding2;

import java.util.ArrayList;
import java.util.Scanner;

public class Coding2A {
    public static void main(String[] Args) {
        Scanner myObj = new Scanner(System.in);

        int runTimes = myObj.nextInt();

        for (int i = 0; i < runTimes; i++) {
            ArrayList<Integer> myArray = new ArrayList<>();
            int length = myObj.nextInt();
            for (int j = 0; j < length; j++) {
                int temp = myObj.nextInt();
                myArray.add(temp);
            }
            BubbleSort bubbleSort = new BubbleSort(myArray, length);
            bubbleSort.showAns();
        }
        myObj.close();
    }
}


class BubbleSort {
    private ArrayList<Integer> myArray;
    private int length;
    private int swapTimes = 0;

    public BubbleSort(ArrayList<Integer> myArray, int length) {
        this.myArray = myArray;
        this.length = length;
    }

    public void sort() {
        for (int i = (length - 1); i > 0; i--) {
            for (int j = 0; j < i; j++) {
                int left = myArray.get(j);
                int right = myArray.get(j + 1);
                if (left > right) {
                    myArray.set(j, right);
                    myArray.set(j + 1, left);
                    swapTimes ++;
                }
            }
        }
    }

    public void showAns() {
        sort();
        System.out.printf("Optimal swapping takes %d swaps.%n", swapTimes);
    }
}