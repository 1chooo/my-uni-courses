// in Dog.h

#ifndef _DOG
#define _DOG
class Dog {
  public:
    void setAge(int age);
    int getAge();
    void setWeight(int weight);
    int getWeight();
    void speak();

  private:
    int age;
    int weight;
};
#endif
