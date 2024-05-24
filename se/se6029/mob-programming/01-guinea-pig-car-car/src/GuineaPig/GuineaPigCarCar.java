// GuineaPigCarCar.java

package GuineaPig;

import java.util.ArrayList;
import Car.Car;

public class GuineaPigCarCar extends GuineaPig {
    private Car car;
    private ArrayList<String> foods = new ArrayList<String>();

    public GuineaPigCarCar() {
        this("GuineaPigCarCar", new Car());
    }

    public GuineaPigCarCar(String name, Car car) {
        super(name);
        this.car = car;
    }

    public void eat(String food) {
        System.out.print(super.name + " eat " + food + ".");

        eatRule(food);
    }

    public void pupu() {
        // System.out.println(super.name + "pupu.");
        // 吃什麼棒什麼
        System.out.printf(super.name);
        for (String pupu : foods) {
            System.out.printf(" %s", pupu);
        }
   
        System.out.println();
        foods.clear();
        super.foodCount = 0;

        car.resetSpeed();
    }

    public int getSpeed() {
        return car.getSpeed();
    }

    // 這邊可以做到當規則變了修改這裡就好，或許可以寫個 Rule.java 來統一管理
    private void eatRule(String food) {
        foods.add(food);

        if (foods.size() > 5) {
            car.resetSpeed();
        } else if (food == "carrot") {
            car.accelerate();
        } else {
            // do nothing
        }
    }

}
