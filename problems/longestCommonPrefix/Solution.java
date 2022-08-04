class Solution {
  public String longestCommonPrefix(String[] strs) {
    if (strs.length == 0) return "";
    String prefix = strs[0];
    int j;
    for (int i = 1; i < strs.length; i++) {
      for (j = 0; j < strs[i].length() && j < prefix.length(); j++)
        if (strs[i].charAt(j) != prefix.charAt(j)) break;
      prefix = prefix.substring(0,j);
    }
    return prefix;
  }
}
