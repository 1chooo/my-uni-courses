package Coding1;

import java.util.ArrayList;
import java.util.Scanner;

public class Coding1B {
    public static void main(String[] Args) {
        Scanner myObj = new Scanner(System.in);

        int runTimes = myObj.nextInt();

        for (int i = 0; i < runTimes; i++) {
            ArrayList <Integer> myArray = new ArrayList<>();
            int inNum = myObj.nextInt();
            myArray.add(inNum);
            HappyNumber happyNumber = new HappyNumber(inNum, myArray);
            happyNumber.judgeHappyNumber();
        }
        myObj.close();
    }    
}


class HappyNumber {
    private int inNum;
    private ArrayList<Integer> myArray;

    public HappyNumber(int inNum, ArrayList<Integer> myArray) {
        this.inNum = inNum;
        this.myArray = myArray;
    }

    public void judgeHappyNumber() {
        while (true) {
            if (inNum == 4) {
                System.out.println("Not Happy");
                break;
            }
            
            int sum = 0;
            while (inNum != 0) {
                int r = inNum % 10;
                sum += r * r;
                inNum = (inNum - r) / 10;
            }
            myArray.add(sum);

            // If the last element of the array is "four", 
            // then the "input number" must not be the "happy number"; 
            // however, if the last element of the array is "one", 
            // the "input number" must be the "happy number".

            int last = myArray.size() - 1;
            if (myArray.get(last) == 4) {
                System.out.println("Not Happy");
                break;
            } else if (myArray.get(last) == 1) {
                System.out.println("Happy");
                break;
            }

            // let input number equals to sum, 
            // then it will update the loop.

            inNum = sum;

            // If it exist the same element in the array,
            // then it will repeat and never stop; therefore,
            // we make this result "Not Happy Number".
            
            int len1 = myArray.size();
            for (int j = 0; j < myArray.size(); j++) {
                for (int k = 0; k < myArray.size(); k++) {
                    if(j != k && myArray.get(j) == myArray.get(k)) {
                        myArray.remove(myArray.get(j));
                    }
                }
            }
            int len2 = myArray.size();
            if (len1 < len2) {
                System.out.println("Not Happy");
                break;
            }
        }
    }
}