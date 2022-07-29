import java.io.*;
import java.net.URL;

public class A12_1 {
  public static void main(String[] Args) throws IOException {
    String URLString = "https://www.csie.ncu.edu.tw";
    String fileRoot = "./A12_1_109601003.txt";

    GetWebsiteHTML getWebsiteHTML = new GetWebsiteHTML(URLString, fileRoot);
    getWebsiteHTML.WriteToFile();
  }
}

class GetWebsiteHTML {
  private String URLString;
  private String fileRoot;

  GetWebsiteHTML(String URLString, String fileRoot) {
    this.URLString = URLString;
    this.fileRoot = fileRoot;
  }

  public void WriteToFile() throws IOException {
    URL url = new URL(URLString);
    FileWriter fileWriter = new FileWriter(fileRoot);
    BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(url.openStream()));

    String line = "";

    while ((line = bufferedReader.readLine()) != null) {
      bufferedWriter.write(line);
      bufferedWriter.newLine();
    }

    bufferedWriter.flush();
    bufferedReader.close();
    fileWriter.close();
    bufferedWriter.close();
  }
}