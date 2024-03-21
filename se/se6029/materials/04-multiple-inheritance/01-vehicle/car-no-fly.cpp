#include <iostream>

using namespace std;

class Vehicle {
  public:
    Vehicle() { cout << "Vehicle Constructor" << endl; }
    virtual ~Vehicle() { cout << "Vehicle Destructor" << endl; }
    virtual void accelerate() const { cout << "Vehicle Accelerating" << endl; }
    void setAcceleration(double a) { acceleration = a; }
    double getAcceleration() const { return acceleration; }

  private:
    double acceleration;
};

class Car : public Vehicle {
  public:
    Car() { cout << "Car Constructor" << endl; }
    virtual ~Car() { cout << "Car Destructor" << endl; }
    virtual void accelerate() const { cout << "Car Accelerating" << endl; }
    void drive() const { cout << "Car Driving" << endl; }

  private:
    // Car inherits acceleration accessors, member
};

class JetCar : public Car {
  public:
    JetCar() {}
    virtual ~JetCar() {}
    virtual void drive() const { cout << "JetCar driving" << endl; }
    virtual void fly() const { cout << "JetCar flying" << endl; }
};

/*
-----------------------
some function elsewhere
-----------------------
*/

void analyzePerformance(Car *testVehicle) {
    testVehicle->drive();
    testVehicle->fly();
}

/*
drive.cpp:44:18: error: no member named 'fly' in 'Car'
    testVehicle->fly();
    ~~~~~~~~~~~  ^
1 error generated.
*/