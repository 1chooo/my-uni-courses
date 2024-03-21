#include <iostream>

using namespace std;

class Vehicle {
  public:
    Vehicle() { cout << "Vehicle Constructor" << endl; }
    virtual ~Vehicle() { cout << "Vehicle Destructor" << endl; }
    virtual void accelerate() const { cout << "Vehicle Accelerating" << endl; }
    void setAcceleration(double a) { acceleration = a; }
    double getAcceleration() const { return acceleration; }

  protected:
    double acceleration;
};

class Car : public Vehicle {
  public:
    Car() { cout << "Car Constructor" << endl; }
    virtual ~Car() { cout << "Car Destructor" << endl; }
    virtual void accelerate() const { cout << "Car Accelerating" << endl; }
    virtual void drive() const { cout << "Car Driving" << endl; }

  private:
    // Car inherits acceleration accessors, member
};
class Jet : public Vehicle {
  public:
    Jet() { cout << "Jet Constructor" << endl; }
    virtual ~Jet() { cout << "Jet Destructor" << endl; }
    virtual void fly() const { cout << "Jet flying" << endl; }
};

class JetCar : public Car, public Jet {
  public:
    JetCar() { cout << "JetCar Constructor" << endl; }
    virtual ~JetCar() { cout << "JetCar Destructor" << endl; }
    virtual void drive() const { cout << "JetCar driving" << endl; }
    virtual void fly() const { cout << "JetCar flying" << endl; }
};
void analyzeCarPerformance(Car *testVehicle) {
    testVehicle->drive();
    // drive() exists for both base and sub class
}
void analyzeJetPerformance(Jet *testVehicle) {
    testVehicle->fly();
    // fly() exists for both base and sub class
}

int main() {
    Car myCar;
    cout << endl;

    Jet myJet;
    cout << endl;

    JetCar myJetCar;
    cout << endl;
    
    cout << "Car testing in progress" << endl;
    analyzeCarPerformance(&myCar);
    analyzeCarPerformance(&myJetCar);

    cout << "Jet testing in progress" << endl;
    analyzeJetPerformance(&myJet);
    analyzeJetPerformance(&myJetCar);
    cout << endl;

    return 0;
}

/*
Outputs:

Vehicle Constructor
Car Constructor

Vehicle Constructor
Jet Constructor

Vehicle Constructor
Car Constructor
Vehicle Constructor
Jet Constructor
JetCar Constructor

Car testing in progress
Car Driving
JetCar driving
Jet testing in progress
Jet flying
JetCar flying

JetCar Destructor
Jet Destructor
Vehicle Destructor
Car Destructor
Vehicle Destructor
Jet Destructor
Vehicle Destructor
Car Destructor
Vehicle Destructor
*/