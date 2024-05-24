package GuineaPig;

public class Car implements ICar{
	protected int BASICSPEED;
	protected int ACC;
	protected int speed;
	
	public Car(int BASICSPEED, int ACC) {
		this.BASICSPEED = BASICSPEED;
		this.ACC = ACC;
		this.speed = BASICSPEED;
	}
	
	@Override
	public void accelerate() {
		speed += ACC;
	}

	@Override
	public int getSpeed() {
		return speed;
	}
	
	@Override
	public void resetSpeed() {
		speed = BASICSPEED;
	}
}