#include <stdio.h>
double myPow(double x, int n){
  int step = -1;
  if (n < 0) {
    x = 1/x;
    step = 1;
  }
  double y = 1;
  while (n != 0)
    if (n%2 == 0) {
      x *= x;
      n /= 2;
    } else {
      y *= x;
      n += step;
    }
  return y;
}

int main() {
  printf("%f", myPow(5,-2));
}
