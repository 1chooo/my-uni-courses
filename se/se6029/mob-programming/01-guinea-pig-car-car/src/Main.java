import Car.Ambulance;
import Car.PoliceCar;
import Car.TrashTruck;
import GuineaPig.GuineaPigCarCar;

import java.util.ArrayList;

public class Main {

    public static ArrayList<GuineaPigCarCar> contestants = new ArrayList<GuineaPigCarCar>();

    public static void main(String[] args) {
        contestants.add(new GuineaPigCarCar("Shiromro", new PoliceCar()));
        contestants.add(new GuineaPigCarCar("Abbey", new Ambulance()));
        contestants.add(new GuineaPigCarCar("Teddy", new TrashTruck()));
        RunRunGuineaPigCarCarRace race = new RunRunGuineaPigCarCarRace(contestants);
        race.run();
    }
}
