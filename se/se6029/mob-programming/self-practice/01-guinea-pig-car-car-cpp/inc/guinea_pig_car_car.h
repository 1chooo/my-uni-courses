// guinea_pig_car_car.h

#ifndef GUINEA_PIG_CAR_CAR_H
#define GUINEA_PIG_CAR_CAR_H

#include "car.h"
#include "guinea_pig.h"
#include <string>
#include <vector>

class GuineaPigCarCar : public GuineaPig {
  private:
    Car car;
    std::vector<std::string> foods;

  public:
    GuineaPigCarCar();
    GuineaPigCarCar(std::string name, Car car);
    void eat(std::string food);
    void pupu();
    int getSpeed();

  private:
    void eatRule(std::string food);
};

#endif // GUINEA_PIG_CAR_CAR_H
