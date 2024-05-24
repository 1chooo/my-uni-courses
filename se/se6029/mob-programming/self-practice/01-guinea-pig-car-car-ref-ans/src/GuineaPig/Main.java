package GuineaPig;

import java.util.ArrayList;

public class Main {
	public static final int DISTANCE = 4000;
	public static void main(String[] args) {
		ArrayList<GuineaPigCarCar> gPCarCars = new ArrayList<GuineaPigCarCar>();
		gPCarCars.add(new GuineaPigCarCar("Shiromo", new PoliceCar()));
		gPCarCars.add(new GuineaPigCarCar("Abbey", new Ambulance()));
		gPCarCars.add(new GuineaPigCarCar("Teddy", new TrashTruck()));
		RunRunGuineaPigCarCar(gPCarCars);
	}
	
	public static void RunRunGuineaPigCarCar(ArrayList<GuineaPigCarCar> gPCarCars) {
		int[] distance =  new int[gPCarCars.size()];
		for(int d : distance)
			d = 0;
		
		boolean raceFinished = false;
		for(int time = 1; ; time ++) {
			for (int i = 0; i < gPCarCars.size(); i++) {
				distance[i] += gPCarCars.get(i).getSpeed();
				if(distance[i] >= DISTANCE) {
					System.out.println("\nNO.1 CarCar is " + gPCarCars.get(i).getName() + "!!!!!\n");
					raceFinished = true;
					break;
				}
			}
			if(raceFinished)
				break;
			if(time % 10 == 0) {
				GuineaPigCarCar fastestCarCar = gPCarCars.get(FastestCarCarIdx(distance));
				fastestCarCar.eat(Food.Lettuce);
				if(fastestCarCar.stomach.size() > 5)
					System.out.println(fastestCarCar.getName() + " " + fastestCarCar.pupu());
				
				GuineaPigCarCar lastCarCar = gPCarCars.get(LastCarCarIdx(distance));
				lastCarCar.eat(Food.Carrot);
				if(lastCarCar.stomach.size() > 5)
					System.out.println(lastCarCar.getName() + " " + lastCarCar.pupu());
			}
		}
		
		for (int i = 0; i < gPCarCars.size(); i++) {
			System.out.println(gPCarCars.get(i).getName() + " ran a total of " + distance[i] + " meters");
		}
	}
	
	public static int LastCarCarIdx(int[] distance) {
		if(distance.length == 0)
			return -1;
		int lastIdx = 0;
		for (int i = 0; i < distance.length; i++) {
			if(distance[i] < distance[lastIdx]) {
				lastIdx = i;
			}
		}
		return lastIdx;
	}
	
	public static int FastestCarCarIdx(int[] distance) {
		if(distance.length == 0)
			return -1;
		int fastestIdx = 0;
		for (int i = 0; i < distance.length; i++) {
			if(distance[fastestIdx] < distance[i]) {
				fastestIdx = i;
			}
		}
		return fastestIdx;
	}
}