package Q1;

public class Matrix {
    private int n,m ;
    private int mat[][] ;

    Matrix(int n, int m, int v) {
        /* 
         * Complete this constructor
         * Initialize a matrix of size n x m with all elements equal to v
         */
        this.m = m;
        this.n = n;
        mat = new int [n][m];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                mat[i][j] = v;
            }
        }

    }

    Matrix(int n, int m) {
        /* 
         * Complete this constructor 
         * Initialize a matrix of size n x m with all elements equal to 0
         */
        this.m = m;
        this.n = n;
        mat = new int [n][m];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                mat[i][j] = 0;
            }
        }
    }

    static Matrix add(Matrix A, Matrix B) {
        /*
         * Complete this method
         * Add two matrices and return the result
         * and return a zero matrix of size 1 x 1
         */
        if(A.m != B.m || A.n != B.n){
            Matrix zeroMat = new Matrix(1,1);
            return zeroMat;
        }
        else{
            Matrix addMat = new Matrix(A.n,A.m);
            for(int i = 0; i < A.n; i++){
                for(int j = 0; j < A.m; j++){
                    addMat.setelem(i, j, A.getelem(i, j) + B.getelem(i, j));
                }
            }
            return addMat;
        }
    
    }

    static Matrix matmul(Matrix A, Matrix B) {
        /*
         * Complete this method
         * Multiply two matrices and return the result
         * and return a zero matrix of size 1 x 1
         */  
        if(A.m != B.n){
            Matrix zeroMat = new Matrix(1,1);
            return zeroMat;
        }
        else{
            Matrix multMat = new Matrix(A.n, B.m);
            for(int i = 0; i < multMat.n; i++){
                for(int j = 0; j < multMat.m; j++){
                    int val = 0;
                    for(int k = 0; k < A.m; k++){
                        val += A.getelem(i,k)*B.getelem(k,j);
                    }
                    multMat.setelem(i, j, val);
                }
            }
            return multMat;
        }
    }

    void scalarmul(int k) {
        /*
         * Complete this method
         * Multiply all elements of the matrix by k
         */
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                mat[i][j] = mat[i][j]*k;
            }
        }
    }

    int getrows() {
        /*
         * Complete this method
         * Return the number of rows in the matrix
         */
        return n;
    }

    int getcols() {
        /*
         * Complete this method
         * Return the number of columns in the matrix
         */
        return m;
    }

    int getelem(int i,int j) {
        /*
         * Complete this method
         * Return the element at row i and column j
         * If i or j is out of bounds, return -1
         */
        return mat[i][j];
    }

    void setelem(int i,int j, int v) {
        /*
         * Complete this method
         * Set the element at row i and column j to v
         * If i or j is out of bounds, don't change anything
         */
        mat[i][j] = v;
    }

    void printmatrix() {
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                if(j!=0) System.out.print(" ");
                System.out.print(mat[i][j]);
            }
            System.out.print("\n") ;
        }
    }
}

