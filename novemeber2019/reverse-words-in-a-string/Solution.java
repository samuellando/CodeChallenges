import java.util.Stack;

class Solution {
    public static String reverseWords(String s) {
        Stack<String> st = new Stack<String>();
        char[] c = s.toCharArray();

       int start = -1;
       for (int i = 0; i < c.length; i++) {
           if (c[i] == ' ') {
                if (start >= 0) {
                    st.push(s.substring(start, i));
                    start = -1;
                }
            } else
                if (start < 0)
                    start = i;
        }
        if (start >= 0)
            st.push(s.substring(start, s.length()));

        s = "";
        for (String w : st) {
            s = w+" "+s;
        }
        if (s.length() < 1)
            return s;
        else
            return s.substring(0, s.length()-1);
    }
}