// Lab02.java

class Lab02 {
    public static void main(String[] args) {

        // Base class
        Base base = new Base();
        base.baseMethod();

        FirstSubClass firstSubClass = new FirstSubClass();
        SecondSubClass secondSubClass = new SecondSubClass();
        
        firstSubClass.FirstSubClassMethod();
        secondSubClass.SecondSubClassMethod();
    }
}

class Base {
    Base() {}
    Base(int w) {}
    Base(int w, String f) {}
    
    void baseMethod() {
        System.out.println("Base method");
    }
}

class FirstSubClass extends Base {
    FirstSubClass() {}

    FirstSubClass(int w) {
        super(w);
    }

    FirstSubClass(int w, String f) {
        super(w, f);
    }

    void FirstSubClassMethod() {
        super.baseMethod();
    }
}

class SecondSubClass extends Base {
    SecondSubClass() {}

    SecondSubClass(int w) {
        super(w);
    }

    SecondSubClass(int w, String f) {
        super(w, f);
    }

    void SecondSubClassMethod() {
        // super.super.baseMethod();   // Wrong
        super.baseMethod();         // Correct
    }
}
