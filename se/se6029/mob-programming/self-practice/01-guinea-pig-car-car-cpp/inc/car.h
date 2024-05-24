// car.h

#ifndef CAR_H
#define CAR_H

class Car {
  private:
    int speed;
    int initSpeed;
    int accelerateSpeed;

  public:
    Car();
    Car(int initSpeed, int accelerateSpeed);
    void accelerate();
    void resetSpeed();
    int getSpeed();
};

#endif // CAR_H
