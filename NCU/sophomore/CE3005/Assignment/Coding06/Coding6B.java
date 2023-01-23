package Coding06;

import java.util.ArrayList;
import java.util.Scanner;

public class Coding6B {
    public static void main(String[] Args) {
        Scanner myObj = new Scanner(System.in);

        int runTimes = myObj.nextInt();

        for (int i = 0; i < runTimes; i++) {
            ArrayList<Integer> individualPrice = new ArrayList<>();
            int total = myObj.nextInt();
            int number = myObj.nextInt();

            for (int j = 0; j < number; j++) {
                int temp = myObj.nextInt();
                individualPrice.add(temp);
            }
        }
        
        myObj.close();
    }
}


class SuperThief {

}