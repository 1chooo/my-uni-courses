package CE1004.E1;

import java.util.Scanner;

public class E1_2 {
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);

    int inNum = 0;
    while (true) {
      inNum = myObj.nextInt();
      if (inNum == -1) {
        break;
      }
      myObj.nextLine();
      String inStr = myObj.nextLine();
      char first = inStr.charAt(0);
      char second = inStr.charAt(1);
      int top = 2 * inNum;
      int a = 0;

      for (int i = 0; i < inNum; i++) {
        int r = i % inNum;
        if (r % 2 == 1) {
          if (a == 0) {
            for (int j = 0; j < 2 *inNum; j++) {
              System.out.print(first);
            }
            System.out.println();
          } else {
            for (int k = 0; k < a; k++) {
              System.out.print(" ");
            }
            for (int l = 0; l < 2 * (inNum-a); l++) {
              System.out.print(second);
            }
            System.out.println();
          }
        } else {
          for (int m = 0; m < a; m++) {
            System.out.print(" ");
          }
          for (int n = 0; n < 2 * (inNum-a); n++) {
            System.out.print(first);
          }
          System.out.println();
        }

        a += 1;
      }
    }
    myObj.close();
  }
}
