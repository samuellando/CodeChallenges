import java.util.Stack;

class Solution {
  public String removeOuterParentheses(String S) {
    Stack<Integer> opens = new Stack<Integer>();
    for (int i = 0; i < S.length(); i++)
      if (S.charAt(i) == '(')
        opens.push(i);
      else
        if (opens.size() == 1) {
          S = S.substring(0, opens.peek())+S.substring(opens.pop()+1, i)+S.substring(i+1);
          i -= 2;
        } else
          opens.pop();
    return S;
  }
}
