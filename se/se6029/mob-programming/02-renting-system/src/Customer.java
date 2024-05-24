import java.util.ArrayList;

public class Customer {

    private String name;
    private ArrayList<Rental> rentalRecord;
    
    public Customer(String name){
        this.name = name;
        this.rentalRecord = new ArrayList<Rental>();
    }

    public String getName(){
        return this.name;
    }

    public void statement(){
        System.out.println(name);
        float totalPoints = 0,
              totalSpend = 0;
        for(Rental r : this.rentalRecord){
            String movieName = r.getMovieName();
            float price = r.getCost();
            float points = r.getPoints();
            totalSpend += price;
            totalPoints += points;
            System.out.printf("Movie name: %s, Price: %f, Points: %f\n", movieName, price, points);
        }
        System.out.printf("Spend until now: %.2f\n", totalSpend);
        System.out.printf("Points until now: %.2f\n", totalPoints);
    }

    public void rent(Movie mv, int rentDays) {
        Rental r = new Rental(mv, this, rentDays);

        rentalRecord.add(r);
    }
}
