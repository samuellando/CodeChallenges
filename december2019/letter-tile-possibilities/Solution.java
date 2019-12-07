import java.util.LinkedList;
import java.util.HashMap;

class Solution {
  public static int numTilePossibilities(String tiles) {
    LinkedList<String> p = new LinkedList<String>();
    HashMap<String, String> h = new HashMap<String, String>();
    p = perm(tiles, p);
    for (String s : p)
      h.put(s, s);
    return h.size();
  }

  public static LinkedList<String> perm(String s, LinkedList<String> al) {
    al = new LinkedList<String>(al);
    if (s.length() == 1) {
      al.add(s);
      return al;
    } else {
      al = perm(s.substring(1), al);
      int size = al.size();
      al.add(s.charAt(0)+"");
      for (int i = 0; i < size; i++) {
        for (int j = 0; j <= al.get(i).length(); j++) {
          al.add(al.get(i).substring(0, j)+s.charAt(0)+al.get(i).substring(j));
        }
      }
      return al;
    }
  }

  public static void main(String[] args) {
    System.out.println(numTilePossibilities("AAABBC"));
  }
}
