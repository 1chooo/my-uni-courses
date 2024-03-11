package CE1004.P03;
class Student {
  private String name;
  private int score;

  public Student(String name, int score) {
    this.name = name;
    this.score = score;
  }
  public String getName() {
    return name;
  }
  public int getScore() {
    return score;
  }
  public void changeScore(int newScore) {
    this.score = newScore;
  }
}

public class P03 {
  public static void main(String[] args) {
    // 以下不要改
    Student putin = new Student("Putin", 59);
    System.out.println(putin.getName() + " before: " + putin.getScore());
    putin.changeScore(40);
    System.out.println(putin.getName() + " after: " + putin.getScore());
//        putin.score = 100;
  }
}