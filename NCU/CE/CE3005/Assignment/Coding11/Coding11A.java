package Coding11;

import java.util.Scanner;
import java.util.ArrayList;

public class Coding11A {
    public static void main(String[] Args) {
        Scanner myObjects = new Scanner(System.in);
        ArrayList<Integer> scoreArray = new ArrayList<>();

        int runTimes = myObjects.nextInt();
        myObjects.nextLine();

        for (int i = 0; i < runTimes; i++) {
            for (int j = 0; j < 20; j++) {
                int temp = myObjects.nextInt();
                scoreArray.add(temp);
            }
            myObjects.nextLine();
            int order = myObjects.nextInt();
            KthSmallest kthSmallest = new KthSmallest(scoreArray);
            kthSmallest.sortScore();
            kthSmallest.showAns(order - 1);
            scoreArray.clear();
        }
        myObjects.close();
    }
}


class KthSmallest {
    private ArrayList<Integer> scoreArray = new ArrayList<>();
  
    public KthSmallest(ArrayList<Integer> scoreArray) {
        this.scoreArray = scoreArray;
    }
  
    public void sortScore() {
        int len = 20;
        for (int i = len - 1; i > 0; i--) {
            for (int j = 0; j < i; j++) {
                int left = scoreArray.get(j);
                int right = scoreArray.get(j + 1);
                if (left > right) {
                    scoreArray.set(j, right);
                    scoreArray.set(j + 1, left);
                }
            }
        }
    }
  
    public void showAns(int order) {
        System.out.println(scoreArray.get(order));
    }
}