int reverse(int x){
  if (x == -2147483648) return 0;
  short sign = x<0?-1:1;
  x *= sign;
  long y = 0;
  while (x > 0) {
    y *= 10;
    y += x % 10;
    x /= 10;
    if (y > 2147483647 || y < -2147483648) return 0;
  }
  return y*sign;
}
