package CE1004.P02;

import java.io.IOException;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.BufferedReader;
import java.io.FileReader;

public class P02 {
  public static void main(String[] args) throws IOException {
    FileReader fr = new FileReader("./CE1004/src/test.txt");
    BufferedReader br = new BufferedReader(fr);
    FileWriter fw = new FileWriter("./CE1004/src/stu_id.txt");
    BufferedWriter bufw = new BufferedWriter(fw);

    String line;
    while ((line = br.readLine()) != null) {
      bufw.write(line);
      bufw.newLine();
    }
    bufw.flush();
    fr.close();
    br.close();
    fw.close();
    bufw.close();
  }
}