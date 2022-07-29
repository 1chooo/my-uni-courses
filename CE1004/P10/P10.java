

import java.util.ArrayList;
import java.util.Scanner;

public class P10 {
  public static void main(String[] Args) {
    Scanner myObj = new Scanner(System.in);
    Item cola = new Item("Cola", 30);
    Item greenTea = new Item("Green Tea", 25);
    Item lemonTea = new Item("Lemon Tea", 29);
    Item mineralTea = new Item("Mineral Tea", 20);
    ArrayList<String> product = new ArrayList<>();

    int price = 0;
    while (true) {
      System.out.println("(1)choose drinks (2)list (3)pay (4)exit");
      String choose;
      choose = myObj.nextLine();
      String pay;
      if (choose.equals("4")) {
        System.out.println("exit");
        break;
      } else if (choose.equals("1")) {
        System.out.println("choose drinks (drinks / amount)");
        System.out.println("(1)Cola (2)Green Tea (3)Lemon Tea (4)Mineral Tea");
        String s = "";
        s = myObj.nextLine();
        String[] Temp = s.split(" ");
        String s1 = Temp[0];
        String s2 = Temp[1];
        int num = Integer.parseInt(s2);

        if (s1.equals("1")) {
          product.add(cola.getName());
          price += (cola.getPrice() * num);
        } else if (s1.equals("2")) {
          product.add(greenTea.getName());
          price += (greenTea.getPrice() * num);
        } else if (s1.equals("3")) {
          product.add(lemonTea.getName());
          price += (lemonTea.getPrice() * num);
        } else if (s1.equals("4")) {
          product.add(mineralTea.getName());
          price += (mineralTea.getPrice() * num);
        } else {
          System.out.println("invalid input");
        }
        product.add(s2);
      } else if (choose.equals("2")) {
        if (product.size() == 0) {
          System.out.println("Empty");
        } else {
          if (product.size() != 2) {
            for (int j = 0; j < product.size() - 1; j += 2) {
              if (product.get(j).equals("hi")) {
                int temp = 0;
              } else {
                if (j < product.size() - 1) {
                  for (int k = j + 2; k < product.size(); k += 2) {
                    if (product.get(j).equals(product.get(k))) {
                      product.set(k, "hi");
                      int temp = Integer.parseInt(product.get(j + 1));
                      temp += Integer.parseInt(product.get(k + 1));
                      product.set(k + 1, "hi");
                      product.set(j + 1, String.valueOf(temp));
                    }
                  }
                } else {
                  break;
                }
              }
            }
          }

          for (int i = 0; i < product.size(); i += 2) {
            if (product.get(i).equals("hi")) {
              int temp = 0;
            } else {
              System.out.print(product.get(i));
              System.out.print(" ");
              System.out.println(product.get(i + 1));
            }
          }
        }
      } else if (choose.equals("3")) {
        System.out.print("total cost: ");
        System.out.println(price);
        System.out.println("please pay: ");
        pay = myObj.nextLine();
        int temp = Integer.parseInt(pay);
        int change = temp - price;
        if (change > 0) {
          System.out.print("money change: ");
          System.out.println(change);
          System.out.println("thank you");
          break;
        } else {
          System.out.println("money not enough");
        }
      }else {
        System.out.println("invalid input");
      }
    }
    myObj.close();
  }
}


class Item {
  private String Name;
  private int Price;

  public Item(String Name, int Price) {
    this.Name = Name;
    this.Price = Price;
  }

  public String getName() {
    return Name;
  }
  public int getPrice() {
    return Price;
  }
}