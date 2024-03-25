public class Lab03 {
    public static void main(String[] args) {
        Child childObj = new Child(10); // 建立 Child 物件時傳遞參數到父類別建構子
    }
}

class Parent {
    Parent(int x) {
        System.out.println("Parent constructor called with parameter: " + x);
    }
}

class Child extends Parent {
    Child(int y) {
        super(y); // Call parent constructor with parameter
        System.out.println("Child constructor called with parameter: " + y);
    }
}
