package Coding4;

import java.util.Scanner;

public class Coding4B {
    public static void main(String[] Args) {
        Scanner myObj = new Scanner(System.in);

        int runTimes = myObj.nextInt();

        for (int i = 0; i < runTimes; i++) {
            int page = myObj.nextInt();
            
            AddThePage addThePage = new AddThePage();
            addThePage.GetTotalPages(page);
        }
        
        myObj.close();
    }
}


class AddThePage {

    public AddThePage() {}

    public void GetTotalPages (int page) {
        int i = 0;
        int total = 0;
        int rp = 0;

        while (true) {
            i++;
            total += i;

            if (total > page) {
                rp = total;
                break;
            }
        }

        System.out.printf("%d %d%n", (rp - page), i);
    }
}