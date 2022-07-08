package Coding3;

import java.util.ArrayList;
import java.util.Scanner;

public class Coding3A {
    public static void main(String[] Args) {
        Scanner myObj = new Scanner(System.in);
        
        while (true) {
            ArrayList<Integer> myArray = new ArrayList<>();
            int n = myObj.nextInt();

            if (n == 0) break;

            for (int i = 0; i < n; i++) {
                int temp = myObj.nextInt();
                myArray.add(temp);
            }

            AgeSort ageSort = new AgeSort(n, myArray);
            ageSort.sort();
        }
        myObj.close();
    }
}


class AgeSort {
    private int n;
    private ArrayList<Integer> myArray;

    public AgeSort(int n, ArrayList<Integer> myArray) {
        this.n = n;
        this.myArray = myArray;
    }

    public void sort() {
        for (int i = (n - 1); i > 0; i--) {
            for (int j = 0; j < i; j++) {
                int left = myArray.get(j);
                int right = myArray.get(j + 1);

                if (left > right) {
                    myArray.set(j, right);
                    myArray.set(j + 1, left);
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (i == (n - 1)) {
                System.out.println(myArray.get(i));
            } else {
                System.out.print(myArray.get(i));
                System.out.print(" ");
            }
        }
    }
}