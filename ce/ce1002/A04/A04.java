public class A04 {
  static public void main(String[] args){
    Archer archer = new Archer("Alex",10,100);
    Medic medic = new Medic("Justin",5,100);
    System.out.printf("弓箭手：(%s, %d, %d)%n", archer.getName(),archer.getLevel(), archer.getHealth());
    System.out.printf("醫護兵：(%s, %d, %d)%n", medic.getName(),medic.getLevel(), medic.getHealth());
    archer.Reload();
    archer.Attack();
    medic.Cure();
  }
}

class Character {
  public String name;
  public int level;
  public int health;

  public Character(String name, int level, int health) {
    this.name = name;
    this.level = level;
    this.health = health;
  }

  public String getName() {
    return name;
  }

  public int getLevel() {
    return level;
  }

  public int getHealth() {
    return health;
  }
}

class Archer extends Character {

  public Archer(String name, int level, int health) {
    super(name, level, health);
  }

  public void Attack() {
    System.out.println("弓箭手：發射弓箭");
  }

  public void Reload() {
    System.out.println("弓箭手：填裝彈藥");
  }
}

class Medic extends Character {

  public Medic(String name, int level, int health) {
    super(name, level, health);
  }

  public void Cure() { System.out.println("醫療兵：治癒中");}
}