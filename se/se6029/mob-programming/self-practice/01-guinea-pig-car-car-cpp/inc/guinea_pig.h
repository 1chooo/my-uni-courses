// guinea_pig.h

#ifndef GUINEA_PIG_H
#define GUINEA_PIG_H

#include <string>

class GuineaPig {
  protected:
    std::string name;
    int foodCount;

  public:
    GuineaPig();
    GuineaPig(std::string name);
    void noise();
    void eat(std::string food);
    void pupu();
    std::string getName();
};

#endif // GUINEA_PIG_H
