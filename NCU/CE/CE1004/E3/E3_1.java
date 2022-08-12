package CE1004.E3;

import java.util.Dictionary;
import java.util.Hashtable;
import java.util.Scanner;

public class E3_1 {
  public static void main(String[] args) {

    Scanner myObjects = new Scanner(System.in);

    while (true) {
      String startDate = myObjects.nextLine();
      if (startDate.equals("0")) {
        break;
      }

      String endDate = myObjects.nextLine();
      CountLeapDay countLeapDay = new CountLeapDay(startDate, endDate);
      countLeapDay.setMonth();
      countLeapDay.splitDate();
      int leapDay = countLeapDay.count(countLeapDay.getStartDateArrayToInteger(), countLeapDay.getEndDateArrayToInteger());
      leapDay += countLeapDay.correction("start", countLeapDay.getStartDateArrayToInteger());
      leapDay += countLeapDay.correction("end", countLeapDay.getEndDateArrayToInteger());
      System.out.println(leapDay);
    }
    myObjects.close();
  }
}

class CountLeapDay {
  private String startDate;
  private String endDate;
  private Dictionary<String, Integer> dictionary = new Hashtable<>();
  private int[] startDateArrayToInteger = new int[3];
  private int[] endDateArrayToInteger = new int[3];

  public CountLeapDay(String startDate, String endDate) {
    this.startDate = startDate;
    this.endDate = endDate;
  }

  public void setMonth() {
    dictionary.put("January", 1);
    dictionary.put("February", 2);
    dictionary.put("March", 3);
    dictionary.put("April", 4);
    dictionary.put("May", 5);
    dictionary.put("June", 6);
    dictionary.put("July", 7);
    dictionary.put("August", 8);
    dictionary.put("September", 9);
    dictionary.put("October", 10);
    dictionary.put("November", 11);
    dictionary.put("December", 12);
  }

  public void splitDate() {
    String[] startDateArray = startDate.split(" |, ");
    String[] endDateArray = endDate.split(" |, ");

    startDateArrayToInteger[0] = dictionary.get(startDateArray[0]);
    startDateArrayToInteger[1] = Integer.parseInt(startDateArray[1]);
    startDateArrayToInteger[2] = Integer.parseInt(startDateArray[2]);

    endDateArrayToInteger[0] = dictionary.get(endDateArray[0]);
    endDateArrayToInteger[1] = Integer.parseInt(endDateArray[1]);
    endDateArrayToInteger[2] = Integer.parseInt(endDateArray[2]);
  }

  public int[] getStartDateArrayToInteger() {
    return startDateArrayToInteger;
  }

  public int[] getEndDateArrayToInteger() {
    return endDateArrayToInteger;
  }

  public int count(int[] startDateArrayToInteger, int[] endDateArrayToInteger) {
    int count = 0;
    for (int i = startDateArrayToInteger[2]; i <= endDateArrayToInteger[2]; i++) {
      if (i % 400 == 0) {
        count++;
      } else if (i % 100 == 0) {
        int pass = 0;
      } else if (i % 4 == 0) {
        count++;
      }
    }

    return count;
  }

  public int correction(String string, int[] date) {
    int correction = 0;
    if (string.equals("start")) {
      if (count(date, date) == 1) {
        if (date[0] > 2) {
          correction = -1;
        } else if (date[0] == 2) {
          if (date[1] > 29) {
            correction = -1;
          }
        }
      }
    }
    if (string.equals("end")) {
      if (count(date, date) == 1) {
        if (date[0] < 2) {
          correction = -1;
        } else if (date[0] == 2) {
          if (date[1] < 29) {
            correction = -1;
          }
        }
      }
    }

    return correction;
  }
}