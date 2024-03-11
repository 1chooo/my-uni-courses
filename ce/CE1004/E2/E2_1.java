package CE1004.E2;


import java.util.ArrayList;
import java.util.Scanner;

public class E2_1 {
  public static void main(String[] Args) {
    ShoppingChart shoppingChart = new ShoppingChart();
    Scanner myObj = new Scanner(System.in);

    while (true) {
      System.out.println("選擇一指令：");
      System.out.println("添加商品：add");
      System.out.println("查詢購物車商品：query");
      System.out.println("修改商品數量：update");
      System.out.println("結算金額：pay");
      String action = myObj.nextLine();
      if (action.equals("exit")) {
        break;
      } else if (action.equals("add")) {
        shoppingChart.add();
      } else if (action.equals("query")) {
        shoppingChart.query();
      } else if (action.equals("pay")) {
        shoppingChart.pay();
      } else if (action.equals("update")) {
        shoppingChart.update();
      } else {
        System.out.println("沒有該功能！");
      }
    }
    myObj.close();
  }
}

class ShoppingChart {
  private Scanner myObj = new Scanner(System.in);
  private ArrayList<String> numberList = new ArrayList<>();
  private ArrayList<String> nameList = new ArrayList<>();
  private ArrayList<Float> priceList = new ArrayList<>();
  private ArrayList<Integer> amountList = new ArrayList<>();

  public float countTotal() {
    float price = 0;
    int len = numberList.size();
    for (int i = 0; i < len; i++) {
      Float tempPrice = priceList.get(i);
      int tempAmount = amountList.get(i);
      price += tempPrice * tempAmount;
    }
    return price;
  }

  public void add() {
    System.out.println("請輸入商品編號：");
    String number = myObj.nextLine();
    numberList.add(number);
    System.out.println("請輸入商品名稱：");
    String name = myObj.nextLine();
    nameList.add(name);
    System.out.println("請輸入商品價格：");
    String price = myObj.nextLine();
    priceList.add(Float.parseFloat(price));
    System.out.println("請輸入商品數量：");
    String amount = myObj.nextLine();
    amountList.add(Integer.parseInt(amount));

    countTotal();
    System.out.print("您的商品：");
    System.out.print(name);
    System.out.println("已添加到購物車");
  }
  public void query() {
    System.out.println("========購物車內容如下========");
    System.out.println("編號      名稱      價格      數量");
    for (int i = 0; i < numberList.size(); i++) {
      System.out.print(numberList.get(i));
      System.out.print("        ");
      System.out.print(nameList.get(i));
      System.out.print("    ");
      System.out.print(priceList.get(i));
      System.out.print("    ");
      System.out.println(amountList.get(i));
    }
  }
  public void update() {
    String number;
    System.out.println("請輸入需要修改的商品編號");
    number = myObj.nextLine();
    int success = -1;
    for (int i = 0; i < numberList.size(); i++) {
      if (number.equals(numberList.get(i))) {
        success = i;
      }
    }
    if (success == -1) {
      System.out.println("無此商品");
    } else {
      System.out.print("請輸入 ");
      System.out.print(nameList.get(success));
      System.out.println(" 的修改數量");
      String amount;
      amount = myObj.nextLine();
      System.out.println("修改完成");
      amountList.set(success, Integer.parseInt(amount));
      countTotal();
      query();
    }

  }
  public void pay() {
    query();
    System.out.println("訂單總金額：" + countTotal());
  }
}