import java.util.InputMismatchException;
import java.util.Scanner;

public class A10 {

  public static void main(String[] Args) {

    while (true) {
      Scanner myObj = new Scanner(System.in);

      System.out.println("請輸入整數");
      int result, number1, number2;

      try {
        number1 = myObj.nextInt();
        number2 = myObj.nextInt();
        if (number1 < 0 || number2 < 0) {
          System.out.println("分子或分母為負數了！");
        } else {
          result = (number1 / number2);
          System.out.println(result);
          break;
        }
      }
      catch (ArithmeticException exception) {
        System.out.println("分母不能為0");
      }
      catch (InputMismatchException exception) {
        System.out.println("輸入為非整數");
      }
      myObj.close();
    }
  }
}