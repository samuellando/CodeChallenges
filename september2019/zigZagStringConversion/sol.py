class Solution(object):
  def convert(self, s, numRows):
    """
      :type s: str
       :type numRows: int
       :rtype: str
       """
       if numRows < 2:
       return s
       rows = []
       row = 0
       zig = 1
       for r in range(numRows):
         rows.append("")
         for l in s:
         rows[row] += l
         if row == 0:
         zig = 1
         elif row == numRows-1:
         zig = -1
         row += zig
         out = ""
         for row in rows:
         out += row
         return out
