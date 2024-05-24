// run_run_guinea_pig_car_car_race.cpp

#include "run_run_guinea_pig_car_car_race.h"
#include <iostream>

RunRunGuineaPigCarCarRace::RunRunGuineaPigCarCarRace(std::vector<GuineaPigCarCar> &contestants) : contestants(contestants), distances(contestants.size(), 0) {}

void RunRunGuineaPigCarCarRace::reset() {
    distances.assign(contestants.size(), 0);
}

void RunRunGuineaPigCarCarRace::onTime() {
    for (size_t i = 0; i < contestants.size(); ++i) {
        distances[i] += contestants[i].getSpeed();
    }
}

void RunRunGuineaPigCarCarRace::on10Sec() {
    int first = 0, last = 0;
    int firstDist = -1, lastDist = RUNWAY_LENGTH;
    for (size_t i = 0; i < contestants.size(); ++i) {
        if (distances[i] > firstDist) {
            firstDist = distances[i];
            first = i;
        }
        if (distances[i] < lastDist) {
            lastDist = distances[i];
            last = i;
        }
    }
    contestants[first].eat("vegetable");
    contestants[last].eat("carrot");
}

void RunRunGuineaPigCarCarRace::run() {
    int t = 0;
    bool racing = true;

    reset();

    while (racing) {
        for (int d : distances) {
            if (d >= RUNWAY_LENGTH) {
                racing = false;
                break;
            }
        }

        t = incrementTime(t);

        if (t % 10 == 0) {
            on10Sec();
        }
        onTime();
    }

    for (size_t i = 0; i < contestants.size(); ++i) {
        std::cout << contestants[i].getName() << ": " << distances[i] << std::endl;
    }

    for (size_t i = 0; i < contestants.size(); ++i) {
        if (distances[i] >= RUNWAY_LENGTH) {
            std::cout << "冠軍得主是: " << contestants[i].getName() << std::endl;
            break;
        }
    }
}

int RunRunGuineaPigCarCarRace::incrementTime(int time) {
    return time + 1;
}
