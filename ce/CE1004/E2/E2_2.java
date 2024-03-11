package CE1004.E2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class E2_2 {
  public static void main (String[] Args) throws IOException {

    FileReader fileReader = new FileReader("./src/e2-2.txt");
    BufferedReader bufferedReader = new BufferedReader(fileReader);
    ArrayList<Integer> pointValue = new ArrayList<>();
    ArrayList<Integer> xValue = new ArrayList<>();
    ArrayList<Integer> yValue = new ArrayList<>();
    ArrayList<Integer> centerValue = new ArrayList<>();
    ArrayList<Integer> xCenter = new ArrayList<>();
    ArrayList<Integer> yCenter = new ArrayList<>();
    ArrayList<Integer> radius = new ArrayList<>();
    ArrayList<Integer> straight = new ArrayList<>();
    ArrayList<Integer> dotInCircle = new ArrayList<>();
    ArrayList<String> lineWithCircle = new ArrayList<>();

    String point;
    String center;
    String line;

    point = bufferedReader.readLine();
    center = bufferedReader.readLine();
    line = bufferedReader.readLine();
    bufferedReader.close();

    String[] pointTemp = Arrays.stream(point.split("[\\[\\],]")).filter(e -> e.trim().length() > 0).toArray(String[]::new);
    for (int i = 0; i < pointTemp.length; i++) {
      pointValue.add(Integer.valueOf(pointTemp[i]));
    }

    String[] centerTemp = Arrays.stream(center.split("[\\[\\],]")).filter(e -> e.trim().length() > 0).toArray(String[]::new);
    for (int i = 0; i < centerTemp.length; i++) {
      centerValue.add(Integer.valueOf(centerTemp[i]));
    }

    String[] lineTemp = Arrays.stream(line.split("[\\[\\],]")).filter(e -> e.trim().length() > 0).toArray(String[]::new);
    for (int i = 0; i < lineTemp.length; i++) {
      straight.add(Integer.valueOf(lineTemp[i]));
    }

    for (int i = 0; i < pointValue.size(); i += 2) {
      xValue.add(pointValue.get(i));
      yValue.add(pointValue.get(i + 1));
    }

    for (int i = 0; i < centerValue.size(); i += 3) {
      xCenter.add(centerValue.get(i));
      yCenter.add(centerValue.get(i + 1));
      radius.add(centerValue.get(i + 2));
    }

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
    for (int i = 0; i < radius.size(); i++) {
      double numerator = Math.abs(straight.get(0) * xCenter.get(i) + straight.get(1) * yCenter.get(i) + straight.get(2));
      double denominator = Math.sqrt(straight.get(0) * straight.get(0) + straight.get(1) * straight.get(1));
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
    for (Integer s : dotInCircle) {
      System.out.print(s + " ");
    }
    for (String s : lineWithCircle) {
      System.out.print(s + " ");
    }
    System.out.println();
  }
}