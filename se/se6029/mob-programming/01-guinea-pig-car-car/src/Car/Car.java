// Car/Car.java

package Car;

public class Car {
    protected int speed;
    protected int initSpeed;
    protected int accelerateSpeed;

    // 為避免沒有給任何值
    public Car() {
        this.speed = 0;
        this.initSpeed = speed;
        this.accelerateSpeed = 0;
    }

    public Car(int initSpeed, int accelerateSpeed) {
        this.speed = initSpeed;
        this.initSpeed = initSpeed;
        this.accelerateSpeed = accelerateSpeed;
    }

    public void accelerate() {
        this.speed = this.accelerateSpeed;
    }

    public void resetSpeed() {
        this.speed = this.initSpeed;
    }

    public int getSpeed() {
        return speed;
    }
}
