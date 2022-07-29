package CE1004.P12;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class P12 {
  public static void main (String[] Args) throws IOException {
    String fileRoot = "./CE1004/src/m2-2.txt";

    JudgeCircleRelation judgeCircleRelation = new JudgeCircleRelation(fileRoot);

    judgeCircleRelation.readFile();
    judgeCircleRelation.solvePoint();
    judgeCircleRelation.solveCircle();
    judgeCircleRelation.solveLine();
    judgeCircleRelation.countDot();
    judgeCircleRelation.judgeRelation();
    judgeCircleRelation.showResult();
  }
}

class JudgeCircleRelation {
  private String point;
  private String center;
  private String line;
  private String fileRoot;
  private ArrayList<Integer> pointValue = new ArrayList<>();
  private ArrayList<Integer> xValue = new ArrayList<>();
  private ArrayList<Integer> yValue = new ArrayList<>();
  private ArrayList<Integer> centerValue = new ArrayList<>();
  private ArrayList<Integer> xCenter = new ArrayList<>();
  private ArrayList<Integer> yCenter = new ArrayList<>();
  private ArrayList<Integer> radius = new ArrayList<>();
  private ArrayList<Integer> straight = new ArrayList<>();
  private ArrayList<Integer> dotInCircle = new ArrayList<>();
  private ArrayList<String> lineWithCircle = new ArrayList<>();

  JudgeCircleRelation(String fileRoot) {
    this.fileRoot = fileRoot;
  }

  public void readFile() throws IOException {
    FileReader fileReader = new FileReader(fileRoot);
    BufferedReader bufferedReader = new BufferedReader(fileReader);
    point = bufferedReader.readLine();
    center = bufferedReader.readLine();
    line = bufferedReader.readLine();
    bufferedReader.close();
    fileReader.close();
  }

  public void solvePoint() {
    String[] pointTemp = Arrays.stream(
            point.split("[\\[\\],]")).filter(
                    e -> e.trim().length() > 0).toArray(String[]::new);
    for (String i : pointTemp) {
      pointValue.add(Integer.valueOf(i));
    }
    for (int i = 0; i < pointValue.size(); i += 2) {
      xValue.add(pointValue.get(i));
      yValue.add(pointValue.get(i + 1));
    }
  }

  public void solveCircle() {
    String[] centerTemp = Arrays.stream(
            center.split("[\\[\\],]")).filter(
                    e -> e.trim().length() > 0).toArray(String[]::new);
    for (String i : centerTemp) {
      centerValue.add(Integer.valueOf(i));
    }
    for (int i = 0; i < centerValue.size(); i += 3) {
      xCenter.add(centerValue.get(i));
      yCenter.add(centerValue.get(i + 1));
      radius.add(centerValue.get(i + 2));
    }
  }

  public void solveLine() {
    String[] lineTemp = Arrays.stream(
            line.split("[\\[\\],]")).filter(
                    e -> e.trim().length() > 0).toArray(String[]::new);
    for (String i : lineTemp) {
      straight.add(Integer.valueOf(i));
    }
  }

  public void countDot() {
    for (int i = 0; i < radius.size(); i++) {
      int count = 0;
      for (int j = 0; j < xValue.size(); j++) {
        double xSquare = Math.pow(xValue.get(j) - xCenter.get(i), 2);
        double ySquare = Math.pow(yValue.get(j) - yCenter.get(i), 2);
        double distant = Math.sqrt(xSquare + ySquare);
        if (distant <= radius.get(i)) {
          count ++;
        }
      }
      dotInCircle.add(count);
    }
  }

  public void judgeRelation() {
    for (int i = 0; i < radius.size(); i++) {
      double numerator = Math.abs(straight.get(0) * xCenter.get(i)
              + straight.get(1) * yCenter.get(i) + straight.get(2));
      double denominator = Math.sqrt(straight.get(0) * straight.get(0)
              + straight.get(1) * straight.get(1));
      double tempDistant = numerator / denominator;
      if (tempDistant < radius.get(i)) {
        lineWithCircle.add("intersect");
      }
      else if (tempDistant == radius.get(i)) {
        lineWithCircle.add("tangency");
      }
      else {
        lineWithCircle.add("disjoint");
      }
    }
  }

  public void showResult() {
    for (Integer s : dotInCircle) {
      System.out.print(s + " ");
    }
    for (String s : lineWithCircle) {
      System.out.print(s + " ");
    }
    System.out.println();
  }
}