package CE1004.P05;
import java.util.Scanner;

public class P05 {
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);

    String heroName = "";
    int heroHp = 0;
    int heroAtk = 0;
    String heroWeapon = "";
    int heroWeaponAtk = 0;

    String enemyName= "";
    int enemyHp = 0;
    int enemyAtk = 0;
    String enemyDropItem = "";
    int option;
    int nextGame;

    Hero h1 = new Hero(heroName, heroHp, heroAtk, heroWeapon, heroWeaponAtk);
    Enemy e1 = new Enemy(enemyName, enemyHp, enemyAtk, enemyDropItem);

    // Step one
    System.out.println("Please Create a hero: ");
    System.out.print("Name: ");
    heroName = myObj.nextLine();
    h1.Name = heroName;
    System.out.print("Hp: ");
    heroHp = myObj.nextInt();
    h1.Hp = heroHp;
    System.out.print("Atk: ");
    heroAtk = myObj.nextInt();
    myObj.nextLine();
    h1.Atk = heroAtk;
    System.out.print(h1.getName() + "'s Weapon: ");
    heroWeapon = myObj.nextLine();
    h1.Weapon = heroWeapon;
    System.out.print(h1.getName() + "'s Weapon Atk: ");
    heroWeaponAtk = myObj.nextInt();
    h1.WeaponAtk = heroWeaponAtk;
    myObj.nextLine();
    System.out.println();

    // Step two
    System.out.println("Please Create an enemy: ");
    System.out.print("Name: ");
    enemyName = myObj.nextLine();
    e1.Name = enemyName;
    System.out.print("Hp: ");
    enemyHp = myObj.nextInt();
    e1.Hp = enemyHp;
    System.out.print("Atk: ");
    enemyAtk = myObj.nextInt();
    myObj.nextLine();
    e1.Atk = enemyAtk;
    System.out.print("DropItem: ");
    enemyDropItem = myObj.nextLine();
    e1.DropItem = enemyDropItem;
    System.out.println("============");
    System.out.println();

    while (h1.getHp() > 0 & e1.getHp() > 0) {

      // Step 3
      System.out.println("A Wild " + e1.getName() + " appeared!");
      System.out.println("What will " + h1.getName() + " do?");
      System.out.println(h1.getName() + "'s Hp: " + h1.getHp());
      System.out.println(e1.getName() + "'s Hp: " + e1.getHp());
      System.out.println("1.Attack 2.Do nothing");
      option = myObj.nextInt();


      if (option == 1) {
        System.out.println(h1.getName() + " use " + h1.getWeapon() + " and hurt " + e1.getName() + " " + (h1.getAtk()+h1.getWeaponAtk()) + " points.");
        e1.Hp = e1.getHp() - (h1.getAtk()+h1.getWeaponAtk());
        h1.Hp = h1.getHp() - e1.getAtk();
      } else if (option == 2) {
        System.out.println(h1.getName() + " is doing nothing.");
        h1.Hp = h1.getHp() - e1.getAtk();
      }
      if (e1.getHp() <= 0) {
        System.out.println(h1.getName() + " wins!");
        System.out.println(e1.getName() + " dropped item \"" + e1.getDropItem() + "\" left on the ground.");
        System.out.println("Want another adventure?");
        System.out.println("1.Yes 2.No");
        nextGame = myObj.nextInt();
        if (nextGame == 1) {
          myObj.nextLine();
          System.out.println();
          System.out.println("Please Create an enemy: ");
          System.out.print("Name: ");
          enemyName = myObj.nextLine();
          e1.Name = enemyName;
          System.out.print("Hp: ");
          enemyHp = myObj.nextInt();
          e1.Hp = enemyHp;
          System.out.print("Atk: ");
          enemyAtk = myObj.nextInt();
          myObj.nextLine();
          e1.Atk = enemyAtk;
          System.out.print("DropItem: ");
          enemyDropItem = myObj.nextLine();
          e1.DropItem = enemyDropItem;
          System.out.println("============");
          System.out.println();
        } else if (nextGame == 2) { System.out.println("Game Over"); }
      }
      if (h1.getHp() <= 0) {
        System.out.println(e1.getName() + " wins!");
        System.out.println(h1.getName() + "'s Weapon \"" + h1.getWeapon() + "\" left on the ground.");
        System.out.println("Game Over");
      }
    }
    myObj.close();
  }
}

class Role {
  public String Name;
  public int Hp;
  public int Atk;

  public Role(String Name, int Hp, int Atk) {
    this.Name = Name;
    this.Hp = Hp;
    this.Atk = Atk;
  }

  public String getName() { return Name; }
  public int getHp() { return Hp; }
  public int getAtk() { return Atk; }
}

class Hero extends Role {
  public String Weapon;
  public int WeaponAtk;

  public Hero(String Name, int Hp, int Atk, String Weapon, int WeaponAtk) {
    super(Name, Hp, Atk);
    this.Weapon = Weapon;
    this.WeaponAtk = WeaponAtk;
  }

  public String getWeapon() { return Weapon; }
  public int getWeaponAtk() { return WeaponAtk; }
}

class Enemy extends Role {
  String DropItem;

  public Enemy(String Name, int Hp, int Atk, String DropItem) {
    super(Name, Hp, Atk);
    this.DropItem = DropItem;
  }

  public String getDropItem() { return DropItem; }
}