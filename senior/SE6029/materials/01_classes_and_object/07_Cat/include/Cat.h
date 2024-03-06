#ifndef CAT_H
#define CAT_H

#include <string>

class Cat {
  public:
    Cat(std::string name = "tom", std::string color = "black_and_white");
    ~Cat();
    void setName(std::string name);
    std::string getName();
    void setColor(std::string color);
    std::string getColor();
    void speak();

  private:
    std::string _name;
    std::string _color;
};

#endif /* CAT_H */
