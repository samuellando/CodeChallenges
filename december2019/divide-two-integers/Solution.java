class Solution {
    public static int divide(int dividend, int divisor) {
        long q = 0;
        long divid = dividend;
        long divis = divisor;
        int sng;
        if (divisor >= 0 && dividend >= 0 || divisor < 0 && dividend < 0)
            sng = 1;
        else
            sng = -1;
        
        if (divid < 0) {
            long d = divid;
            for (long i = 0; i > d+d; i--)
                divid++;
        }
        if (divis < 0) {
            long d = divisor;
            for (long i = 0; i > d+d; i--)
                divis++;
        }
        
        for (long i = divis; i <= divid; i += divis)
            q++;
        if (sng == -1) {
            long d = q;
            for (long i = 0; i < d+d; i++)
                q--;
        }

        if (q > Integer.MAX_VALUE || q < Integer.MIN_VALUE){ //Handle overflow.
            return Integer.MAX_VALUE;
        }
        return (int)q;
    }

    public static void main(String[] args) {
        divide(Integer.MIN_VALUE,-1);
    }
}