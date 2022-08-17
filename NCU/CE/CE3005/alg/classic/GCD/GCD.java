import java.util.Scanner;

public class GCD {
	public static void main(String[] Args) {
		int m, n;
		Scanner myObj = new Scanner(System.in);
		
		System.out.println("Please type two integer m and n: ");
		m = myObj.nextInt();
		n = myObj.nextInt();

		EuclidAlgorithm euclidAlgorithm = new EuclidAlgorithm(m, n);
		euclidAlgorithm.EuclidGCD(m, n);

		System.out.printf("The highest common factor of m and n is %d.\n", n);
		myObj.close();
	}
}

class EuclidAlgorithm {
	private int m;
	private int n;

	public EuclidAlgorithm(int m, int n) {
		this.m = m;
		this.n = n;
	}

	public int getM() {
		return m;
	}

	public void setM(int m) {
		this.m = m;
	}

	public int getN() {
		return n;
	}

	public void setN(int n) {
		this.n = n;
	}

	public int EuclidGCD(int m, int n) {
		int r = m % n;

		while (r != 0) {
			m = n;
			n = r;
			r = m % n;
		}

		return n;
	}
}