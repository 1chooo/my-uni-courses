import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class A12_2 {
  public static void main(String[] Args) {
    ArrayList<String> dateArray = new ArrayList<>();
    ArrayList<String> contentArray = new ArrayList<>();

    try {
      Document document = Jsoup.parse(new File("./A12_1_109601003.txt"), "UTF-8");
      int length = document.select("div.item-title").size();
      for (int i = 0; i < length; i++) {
        String date = document.select("div.item-time").get(i).text();
        dateArray.add(date);
//        System.out.print(date + " ");
        String content = document.select("div.item-time").get(i).text() + " " + document.select("div.item-title").get(i).text();
        contentArray.add(content);
//        System.out.println(content);
      }
      Collections.sort(contentArray);
      for (int i = contentArray.size() - 1; i >= 0; i--) {
        System.out.println(contentArray.get(i));
      }
//      System.out.println(contentArray);
    }
    catch(IOException e) {
      e.printStackTrace();
    }
  }
}