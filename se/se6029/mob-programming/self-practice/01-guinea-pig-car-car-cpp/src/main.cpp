// main.cpp

#include "ambulance.h"
#include "car.h"
#include "guinea_pig_car_car.h"
#include "police_car.h"
#include "run_run_guinea_pig_car_car_race.h"
#include "trash_truck.h"
#include <vector>

int main() {
    std::vector<GuineaPigCarCar> contestants;

    contestants.push_back(GuineaPigCarCar("Shiromro", PoliceCar()));
    contestants.push_back(GuineaPigCarCar("Abbey", Ambulance()));
    contestants.push_back(GuineaPigCarCar("Teddy", TrashTruck()));

    RunRunGuineaPigCarCarRace race(contestants);
    race.run();

    return 0;
}
