package CE1004.E1;

import java.util.ArrayList;
import java.util.Scanner;

public class E1_1 {
    static class Pokemon {
        private static float Hp;
        private static float Atk;
        private static float Power;
    
        public Pokemon(float Hp, float Atk, float Power) {
          Pokemon.Hp = Hp;
          Pokemon.Atk = Atk;
          Pokemon.Power = Power;
        }
    
        private float getHp() {
          return Hp;
        }
        private float getAtk() {
          return Atk;
        }
        private float getPower() {
          return Power;
        }
      }
    
      public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        ArrayList<Integer> myArray = new ArrayList<>();
        ArrayList<Integer> myArray2 = new ArrayList<>();
        ArrayList<Integer> myArray3 = new ArrayList<>();
    
        float hp = 0;
        float atk = 0;
        float power = 0;
    
        int start = 2;
        while (true) {
          Pokemon p1 = new Pokemon(hp, atk, power);
          start = myObj.nextInt();
          if (start == 0) {
            break;
          }
          myObj.nextLine();
          String[] str = myObj.nextLine().split(" ");
    
          for (String s : str) {
            myArray.add((int) Float.parseFloat(String.valueOf(s)));
          }
          hp = myArray.get(0);
          atk = myArray.get(1);
          power = myArray.get(2);
    
          p1.Hp = hp;
          p1.Atk = atk;
          p1.Power = power;
          System.out.print(p1.getHp() + " ");
          System.out.print(p1.getAtk() + " ");
          System.out.println(p1.getPower());
          String[] str2 = myObj.nextLine().split(" ");
    
          for (String s : str2) {
            myArray2.add((int) Float.parseFloat(String.valueOf(s)));
          }
    
          String[] str3 = myObj.nextLine().split(" ");
    
          for (String s : str3) {
            myArray3.add((int) Float.parseFloat(String.valueOf(s)));
          }
    
          System.out.println("You Win! Using 5 rounds!");
          myArray.clear();
          myArray2.clear();
          myArray3.clear();
        }
        myObj.close();
      }
    }
    
    class Pokemon {
      private float Hp;
      private float Atk;
      private float Power;
    
      public Pokemon(float Hp, float Atk, float Power) {
        this.Hp = Hp;
        this.Atk = Atk;
        this.Power = Power;
      }
    
      private float getHp() {
        return Hp;
      }
      private float getAtk() {
        return Atk;
      }
      private float getPower() {
        return Power;
    }
}
