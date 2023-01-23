package CE1004.P06;
import java.util.ArrayList;
import java.util.Scanner;

public class P06 {
  public static void main(String[] Args) {
    ArrayList<String> bookShelf = new ArrayList<>();
    ArrayList<String> temp = new ArrayList<>();
    Scanner myObj = new Scanner(System.in);
    String inStr;

    while (true) {
      inStr = myObj.nextLine();
      String[] strArr;
      int num;
      strArr = inStr.split(" ");
      if (strArr[0].equals("exit")) {
        System.out.println(bookShelf);
        break;
      }
      if (strArr[0].equals("1")) {
        num = Integer.parseInt(strArr[1]);
        int len = bookShelf.size();
        if (num > len) {
          bookShelf.add(strArr[2]);
        } else if (num == len) {
          bookShelf.add(strArr[2]);
        } else {
          num = num - 1;
          temp.addAll(bookShelf);
          for (int i = 0; i < len; i++) {
            if (i < num) {
              int bot = 1;
            } else if (i == num) {
              bookShelf.set(i, strArr[2]);
            } else {
              bookShelf.remove(i);
            }
          }
          for (int j = 0; j < temp.size(); j++) {
            if (j < num) {
              temp.remove(j);
            } else {
              bookShelf.add(temp.get(j));
            }
          }
        }
        temp.clear();
      } else if (strArr[0].equals("2")) {
        num = Integer.parseInt(strArr[1]);
        num = num - 1;
        bookShelf.remove(num);
      }
    }

    myObj.close();
  }
}