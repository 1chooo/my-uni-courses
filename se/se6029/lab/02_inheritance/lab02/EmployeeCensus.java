package lab02;

import java.util.ArrayList;

public class EmployeeCensus extends ArrayList<Employee> {
   public void addEmployee(Employee employee) {
       add(employee);
   }

   public void removeEmployee(Employee employee) {
       remove(employee);
   }
}

class Employee {
   // not important
}
