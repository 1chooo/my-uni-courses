import java.util.Scanner;

public class P01 {
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);

    String inputName;
    String inputStudentNumber;

    inputName = myObj.nextLine();
    inputStudentNumber = myObj.nextLine();

    System.out.println("Hello world!!!");
    System.out.println("I'm " + inputName + " and my student ID is " + inputStudentNumber + '.');

    myObj.close();
  }
}