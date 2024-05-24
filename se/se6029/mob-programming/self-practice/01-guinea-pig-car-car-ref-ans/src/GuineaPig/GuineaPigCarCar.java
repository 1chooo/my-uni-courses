package GuineaPig;

import java.util.ArrayList;

public class GuineaPigCarCar extends GuineaPig implements ICar {
	private ICar car;
	public GuineaPigCarCar(String name, Car car) {
		super(name);
		this.car = car;
	}
	
	@Override
	public ArrayList<Food> pupu() {
		ArrayList<Food> tmp = (ArrayList<Food>) stomach.clone();
		stomach.clear();
		car.resetSpeed();
		return tmp;
	}
	
	@Override
	public void eat(Food food) {
		if(food == Food.Carrot) {
			accelerate();
		}
		stomach.add(food);
	}

	@Override
	public void accelerate() {
		car.accelerate();
	}

	@Override
	public int getSpeed() {
		return car.getSpeed();
	}
	
	@Override
	public void resetSpeed() {
		car.resetSpeed();
	}
}