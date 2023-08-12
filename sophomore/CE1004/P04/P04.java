package CE1004.P04;
class Pet {
  // do something here
  public static void speak() {
    System.out.println("I'm not a pet!");
  }
}

class Cat extends Pet {
  // do something here
  public static void speak() {
    System.out.println("I'm a Cat!");
  }
}

class Dog extends Pet {
  // do something here
  public static void speak() {
    System.out.println("I'm a Dog!");
  }
}

class  newborn_Cat extends Cat {
  // do something here
  public static void speak() {
    System.out.println("I can't speak but I can meow.");
  }
}

class  newborn_Dog extends Dog {
  // do something here
  public static void speak() {
    System.out.println("I can't speak but I can woof.");
  }
}

public class P04 {
  public static void main(String[] args) {
    // 以下不要改
    Pet putin = new Pet();
    Cat neko  = new Cat();
    Dog inu   = new Dog();
    newborn_Cat meow = new newborn_Cat();
    newborn_Dog woof = new newborn_Dog();
    putin.speak();
    neko.speak();
    inu.speak();
    meow.speak();
    woof.speak();
  }
}