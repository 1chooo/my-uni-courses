import java.util.Scanner;

public class A01 {
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);

    int inputInt1;
    int inputInt2;
    int plus;
    int minus;

    inputInt1 = myObj.nextInt();
    inputInt2 = myObj.nextInt();

    plus = inputInt1 + inputInt2;
    minus = inputInt1 - inputInt2;

    System.out.println(plus);
    System.out.println(minus);

    myObj.close();
  }
}
