package Prime;

public class Prime {
    public boolean primeCheck1(int n) {
        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                return false;
            } 
        }
        return true;
    }

    public boolean primeCheck2(int n) {
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            } 
        }
        return true;
    }

    public static void main(String[] Args) {
    
    }
}
