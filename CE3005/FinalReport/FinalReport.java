/**
 * Debug: it has to store g(n) and h(n)
 */

package FinalReport;

import java.util.Scanner;
import static java.lang.Math.min;

public class FinalReport {
  public static void main(String[] Args) {
    Scanner myObjects = new Scanner(System.in);

    int runTimes = myObjects.nextInt(); // Decide how much time we have to conduct.

    for (int i = 0; i < runTimes; i++) {

      // Create the array then we prevent overflow;
      // therefore, we announce bigger than needed.
      // [11][11] is enough.

      int[][] total;
      total = new int[100][100];

      // Here we make the 2D array to store the input.
      for (int j = 1; j <= 3; j++) {
        int temp = myObjects.nextInt();
        total[0][j] = temp;
      }
      for (int j = 1; j <= 3; j++) {
        for (int k = 4; k <= 6; k++) {
          int temp = myObjects.nextInt();
          total[j][k] = temp;
        }
      }
      for (int j = 4; j <= 6; j++) {
        for (int k = 7; k <= 9; k++) {
          int temp = myObjects.nextInt();
          total[j][k] = temp;
        }
      }
      for (int j = 7; j <= 9; j++) {
        int temp = myObjects.nextInt();
        total[j][10] = temp;
      }

      // Here we decide which stage we gave to count.
      int finalStage = myObjects.nextInt();

      // Here is the first stage. We find the minimum directly.
      if (finalStage == 1) {
        int small = 2147483647;
        for (int j = 1; j <= 3; j++) {
          if (small > total[0][j]) {
            small = total[0][j];
          }
        }
        System.out.println(small);
      }

      // Here is the second stage.
      // We start to consider the next steps we will do.
      if (finalStage == 2) {
        int small = 2147483647;
        int temp1;
        int temp2;
        for (int j = 0; j < 3; j++) {
          // g(x)
          temp1 = total[0][j + 1];
          // through the temp2 we can realize the minimum cost of the next step,
          // That is to say the function h(x)
          temp2 = min(min(total[j + 1][4], total[j + 1][5]), total[j + 1][6]);
          temp1 += temp2;
          if (small > temp1) {
            small = temp1;
          }
        }
        System.out.println(small);
      }

      // Here is the stage three, then we start to consider more status to find the lower cost.
      if (finalStage == 3) {
        int small = 2147483647;
        int temp1;
        int temp2;
        for (int j = 1; j <= 3; j++) {
          for (int k = 4; k <= 6; k++) {
            // g(x) and we need to get the previous result.
            temp1 = total[0][j] + total[j][k];
            // as same as the last stage status.
            // We have to realize the minimum cost of the next step h(x)
            temp2 = min(min(total[k][7], total[k][8]), total[k][9]);
            temp1 += temp2;
            if (small > temp1) {
              small = temp1;
            }
          }
        }
        System.out.println(small);
      }

      // The specialist is that stage four and stage five must point to the same result.
      // That's why we use or in this status.
      if (finalStage == 4 || finalStage == 5) {
        int small = 2147483647;
        int temp1;
        // We got through every status to find that the lowest cost of this.
        for (int j = 1; j <= 3; j++) {
          for (int k = 4; k <= 6; k++) {
            for (int l = 7; l <= 9; l++) {
              // g(x) + h(x)
              temp1 = total[0][j] + total[j][k] + total[k][l] + total[l][10];
              if (small > temp1) {
                small = temp1;
              }
            }
          }
        }
        System.out.println(small);
      }
    }
    myObjects.close();
  }
}