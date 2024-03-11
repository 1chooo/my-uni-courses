import java.util.Scanner;

public class A02 {
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);

    int inputInt = myObj.nextInt();
    myObj.nextLine();
    String inputString = myObj.nextLine();

    int bottom;
    char out = inputString.charAt(0);   // take the frame
    char in = inputString.charAt(1);    // take the inside
    bottom = 2 * inputInt;              // the bottom
    int spaceNum = inputInt - 1;           // the spaceNum
    char space = ' ';

    for (int i = 1; i <= inputInt; i++) {
      // the TOP
      if (i == 1){
        for (int j = 1; j <= spaceNum; j++) {
          System.out.print(space);
        }
        System.out.print(out);
        System.out.print(out);
        for (int k = 1; k <= spaceNum; k++) {
          System.out.print(space);
        }
        System.out.println();
      }
      // the BOTTOM
      else if (i == inputInt) {
        for (int m = 1; m <= bottom; m++) {
          System.out.print(out);
        }
        System.out.println();
      }
      else {
        for (int j = 0; j <= (spaceNum - i); j++) {
          System.out.print(space);
        }
        System.out.print(out);
        for (int k = 1; k <= ((i - 1) * 2); k++) {
          System.out.print(in);
        }
        System.out.print(out);
        for (int l = 0; l <= (spaceNum - i); l++) {
          System.out.print(space);
        }
        System.out.println();
      }
    }

    myObj.close();
  }
}
