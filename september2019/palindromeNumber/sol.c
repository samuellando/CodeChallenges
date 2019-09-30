int isPalindrome(int x){
  if (x < 0) return 0;

  int mag = 1;
  for (int i = x/10; i > 0; i /= 10)
    mag *= 10;

  while (mag > 1) {
    if (x % 10 != x / mag % 10)
      return 0;
    x /= 10;
    mag /= 100;
  }
  return 1;
}
