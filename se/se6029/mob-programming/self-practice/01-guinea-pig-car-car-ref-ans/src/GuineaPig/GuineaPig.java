package GuineaPig;

import java.util.ArrayList;

public class GuineaPig {
	private String name;
	protected ArrayList<Food> stomach;
	public GuineaPig(String name) {
		this.name = name;
		this.stomach = new ArrayList<Food>();
	}
	
	public String getName() {
		return name;
	}
	
	public String noise() {
		return "PUI PUI";
	}
	
	public void eat(Food food) {
		stomach.add(food);
	}
	
	public ArrayList<Food> pupu() {
		for(int i = 0; i < stomach.size(); i++) {
			stomach.set(i, Food.Pupu);
		}
		ArrayList<Food> tmp = (ArrayList<Food>) stomach.clone();
		stomach.clear();
		return tmp;
	}
}