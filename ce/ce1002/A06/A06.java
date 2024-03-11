import java.util.ArrayList;
import java.util.Scanner;

public class A06 {
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);
    Transaction t1 = new Transaction();
    int Times = 0;
    int operator = 0;
    while (true) {
      operator = myObj.nextInt();
      myObj.nextLine();
      if (operator == 4) {
        break;
      } else if (operator == 1) {
        Times++;
        String[] incomeContent = myObj.nextLine().split(" ");
        t1.addName(incomeContent[0]);
        t1.addIncome(Integer.parseInt(incomeContent[1]));
      } else if (operator == 2) {
        Times++;
        String[] payContent = myObj.nextLine().split(" ");
        t1.addName(payContent[0]);
        t1.addPay(Integer.parseInt(payContent[1]));
      } else if (operator == 3) {
        int maxNameLength = 0;
        for (int j = 0; j < Times; j++) {
          int nameLength = t1.nameLength(j);
          if (nameLength > maxNameLength) {
            maxNameLength = nameLength;
          }
        }

        int maxIncomeLength = 0;
        for (int k = 0; k < Times; k++) {
          int incomeLength = t1.incomeLength(k);
          if (incomeLength > maxIncomeLength) {
            maxIncomeLength = incomeLength;
          }
        }

        for (int i = 0; i < Times; i++) {
          int nameLen;
          int incomeLen;
          System.out.print(t1.getName(i));
          nameLen = t1.nameLength(i);
          if (nameLen < maxNameLength) {
            for (int l = 0; l < (maxNameLength-nameLen); l++) {
              System.out.print(" ");
            }
          }
          System.out.print("  ");
          System.out.print(t1.getIncome(i));
          incomeLen = t1.incomeLength(i);
          if (incomeLen < maxIncomeLength) {
            for (int l = 0; l < (maxIncomeLength - incomeLen); l++) {
              System.out.print(" ");
            }
          }
          System.out.print("  ");
          System.out.println(t1.getPay(i));
        }
        System.out.print("Total: ");
        System.out.println(t1.getTotal());
      } else {
        System.out.println("Invalid Operation");
      }
    }
    myObj.close();
  }
}

class Transaction {
  private ArrayList<String> name = new ArrayList<>();
  private ArrayList<Integer> income = new ArrayList<>();
  private ArrayList<Integer> pay = new ArrayList<>();
  private int total;

  public Transaction() {}

  public void addName(String n) {
    this.name.add(n);
  }
  public void addIncome(int i) {
    this.income.add(i);
    this.pay.add(0);
    this.total = this.total + i;
  }
  public void addPay(int p) {
    this.income.add(0);
    this.pay.add(p);
    this.total = this.total - p;
  }

  public String getName(int num) {
    return this.name.get(num);
  }
  public int getIncome(int num) {
    return this.income.get(num);
  }
  public int getPay(int num) {
    return this.pay.get(num);
  }
  public int getTotal() {
    return this.total;
  }

  public int nameLength(int num) {
    int l = this.getName(num).length();
    return l;
  }
  public int incomeLength(int num) {
    String s = String.valueOf(this.getIncome(num));
    int l = s.length();
    return l;
  }
}