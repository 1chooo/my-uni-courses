package Coding06;

import java.util.Scanner;

public class Coding6A {
    public static void main(String[] Args) {
        Scanner myObj = new Scanner(System.in);

        while (true) {
            int x1 = myObj.nextInt();
            int y1 = myObj.nextInt();
            int x2 = myObj.nextInt();
            int y2 = myObj.nextInt();

            if ((x1 + y1 + x2 + y2) == 0) {
                break;
            }

            Queen queen = new Queen(x1, y1, x2, y2);
            queen.countSteps();
        }

        myObj.close();
    }
}


class Queen {
    private int x1;
    private int y1;
    private int x2;
    private int y2;

    public Queen(int x1, int y1, int x2, int y2) {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
    }

    public void countSteps() {
        int xDistance = Math.abs(x2 - x1);
        int yDistance = Math.abs(y2 - y1);

        if (xDistance == 0 && yDistance == 0) {
            System.out.println(0);
        } else if (xDistance == yDistance || x1 == x2 || y1 == y2) {
            System.out.println(1);
        } else {
            System.out.println(2);
        }
    }
}