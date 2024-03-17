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
    Car() {}
    virtual ~Car() {}
    virtual void accelerate() const { cout << "Car Accelerating" << endl; }
    virtual void drive() const { cout << "Car Driving" << endl; }
    virtual void fly() const { cout << "Cars can only fall" << endl; }

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

void analyzePerformance(Car *testVehicle) {
    testVehicle->drive();
    testVehicle->fly();
}

int main() {
    Car myCar;
    JetCar myJetCar;
    analyzePerformance(&myCar);
    analyzePerformance(&myJetCar);
    return 0;
}


/*
Outputs:

Vehicle Constructor
Vehicle Constructor
Car Driving
Cars can only fall
JetCar driving
JetCar flying
Vehicle Destructor
Vehicle Destructor
*/
