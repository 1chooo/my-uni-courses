package Coding3;

import java.util.Scanner;

public class Coding3B {
    public static void main(String[] Args) {
        Scanner myObj = new Scanner(System.in);
        
        String[] inStr = myObj.nextLine().split(" ");

        int len = inStr.length;

        int[] sequence = new int[len];

        for (int i = 0; i < len; i++) {
            sequence[i] = Integer.parseInt(inStr[i]);
        }

        for (int i = 0; i < len; i++) {
            if (i == len - 1) {
                System.out.println(sequence[i]);
            } else {
                System.out.print(sequence[i]);
                System.out.print(" ");
            }
        }

        QuickSort quickSort = new QuickSort();
        quickSort.Sort(sequence, 0, len - 1);

        myObj.close();
    }    
}


class QuickSort {

    public QuickSort() {}

    public int[] Sort(int[] A, int lb, int rb) {
        if (lb >= rb) {
            return A;
        }
    
        int pivot = A[rb];
        int l = lb;
        int r = rb - 1;
    
        while (true) {
            while (A[l] < pivot) {
                l += 1;
            }
            while (A[r] >= pivot && r > lb) {
                r -= 1;
            }
            if (l < r) {
                int temp = A[l];
                A[l] = A[r];
                A[r] = temp;
                for (int j = 0; j < A.length; j++) {
                    if (j == A.length - 1) {
                        System.out.println(A[j]);
                    } else {
                        System.out.print(A[j]);
                        System.out.print(" ");
                    }
                }
            } else {
                break;
            }
        }
    
        if (A[rb] != A[l]) {
            int temp = A[rb];
            A[rb] = A[l];
            A[l] = temp;
            for (int j = 0; j < A.length; j++) {
                if (j == A.length - 1) {
                    System.out.println(A[j]);
                } else {
                    System.out.print(A[j]);
                    System.out.print(" ");
                }
            }
        }

        Sort(A, lb, l - 1);
        Sort(A, l + 1, rb);
        return A;
    }
}