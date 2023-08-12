class QuickSort {

    public QuickSort() {}

    public int[] Sort(int[] A, int lb, int rb) {
        if (lb >= rb) {
            return A;
        }
    
        int pivot = A[rb];
        int l = lb;
        int r = rb - 1;
    
        while (true) {
            while (A[l] < pivot) {
                l += 1;
            }
            while (A[r] >= pivot && r > lb) {
                r -= 1;
            }
            if (l < r) {
                int temp = A[l];
                A[l] = A[r];
                A[r] = temp;
                for (int j = 0; j < A.length; j++) {
                    if (j == A.length - 1) {
                        System.out.println(A[j]);
                    } else {
                        System.out.print(A[j]);
                        System.out.print(" ");
                    }
                }
            } else {
                break;
            }
        }
    
        if (A[rb] != A[l]) {
            int temp = A[rb];
            A[rb] = A[l];
            A[l] = temp;
            for (int j = 0; j < A.length; j++) {
                if (j == A.length - 1) {
                    System.out.println(A[j]);
                } else {
                    System.out.print(A[j]);
                    System.out.print(" ");
                }
            }
        }

        Sort(A, lb, l - 1);
        Sort(A, l + 1, rb);
        return A;
    }
}