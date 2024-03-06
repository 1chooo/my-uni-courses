#ifndef EMPLOYEE_H
#define EMPLOYEE_H

class Employee {
  public:
    Employee(char *name, int id);
    // 為避免 dangling pointer，我們需要在 Employee 建立 copy constructor
    Employee(Employee &rhs); // right hand side
    ~Employee();
    char *getName();
    int getId();
    // Other Accessor methods
  private:
    int _id;
    char *_name;
};

#endif /* EMPLOYEE_H */
