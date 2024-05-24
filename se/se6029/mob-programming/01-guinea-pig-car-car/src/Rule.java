import java.util.ArrayList;

import Car.Car;

public class Rule {

    public Rule() {
    }

    // Once rule change, we can just override this method
    public void eatRule(
            Car car, ArrayList<String> foods, String food) {
        foods.add(food);

        if (foods.size() > 5) {
            car.resetSpeed();
        } else if (food == "carrot") {
            car.accelerate();
        } else {
            // doNoting();
        }
    }
}
