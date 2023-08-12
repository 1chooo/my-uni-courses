package CE1004.E3;

import java.util.Scanner;

public class E3_2 {
  public static void main(String[] Args) {
    Scanner myObjects = new Scanner(System.in);

    while (true) {
      int row = myObjects.nextInt();
      if (row == 0) {
        break;
      }
      int column = myObjects.nextInt();
      int times = myObjects.nextInt();
      String[][] chess = new String[row][column];

      for (int i = 0; i < row; i++) {
        String in = myObjects.next();
        for (int j = 0; j < column; j++) {
          chess[i][j] = String.valueOf(in.charAt(j));
        }
      }

      String[][] answer = new String[row][column];

      GameOfLife gameOfLife = new GameOfLife(row, column, times, chess, answer);

      for (int k = 0; k < times; k++) {
        chess = gameOfLife.rule(row, column, chess);
      }
      gameOfLife.getAns();
    }
    myObjects.close();
  }
}

class GameOfLife {
  private int row;
  private int column;
  int times;
  private String[][] chess;
  private String[][] answer = new String[row][column];

  public GameOfLife(int row, int column, int times, String[][] chess, String[][] answer) {
    this.row = row;
    this.column = column;
    this.times = times;
    this.chess = chess;
    this.answer = answer;
  }

  public String[][] rule (int row, int column, String[][] chess) {
    int alive = 0;
    for (int i = 0; i < row; i++) {
      for (int j = 0; j < column; j++) {
        if (chess[i][j].charAt(0) == '0') {
          alive = count(i, j, chess);
          if (alive == 3) {
            answer[i][j] = "1";
          } else {
            answer[i][j] = "0";
          }
        } else {
          alive = count(i, j, chess);
          if (alive == 2 || alive == 3) {
            answer[i][j] = "1";
          } else {
            answer[i][j] = "0";
          }
        }
      }
    }
    return answer;
  }

  public int count(int i, int j, String[][] input) {
    int count = 0;
    for (int m = i-1; m < i+2; m++) {
      for (int n = j-1; n < j+2; n++){
        try {
          if (input[m][n].charAt(0) == '1') {
            if (!(m == i && n == j)) {
              count++;
            }
          }
        }
        catch (Exception e) {}
      }
    }
    return count;
  }

  public void getAns() {
    for (int i = 0; i < row; i++) {
      for (int j = 0; j < column; j++) {
        System.out.print(answer[i][j]);
      }
      System.out.println();
    }
  }
}