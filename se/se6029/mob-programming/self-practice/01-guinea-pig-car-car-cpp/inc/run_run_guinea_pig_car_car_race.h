// run_run_guinea_pig_car_car_race.h

#ifndef RUN_RUN_GUINEA_PIG_CAR_CAR_RACE_H
#define RUN_RUN_GUINEA_PIG_CAR_CAR_RACE_H

#include "guinea_pig_car_car.h"
#include <string>
#include <vector>

class RunRunGuineaPigCarCarRace {
  private:
    std::vector<GuineaPigCarCar> contestants;
    std::vector<int> distances;

  public:
    RunRunGuineaPigCarCarRace(std::vector<GuineaPigCarCar> &contestants);
    void run();

  private:
    void reset();
    void onTime();
    void on10Sec();
    int incrementTime(int time);

    static const int RUNWAY_LENGTH = 4000;
};

#endif // RUN_RUN_GUINEA_PIG_CAR_CAR_RACE_H
