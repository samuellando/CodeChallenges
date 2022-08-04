#include <stdio.h> 
#include <math.h> 

double f(double x) { 
  return x+1/x-100; 
} 

double bisectionMethod(double a, double b, int n) { 
  double mid = (a+b)/2;
  printf("n = %d : f(%.16f) = %.16f : f(%.16f) = %.16f : f(%.16f) = %.16f\n", n, a, f(a), b, f(b), mid, f(mid));
  if (n == 1) return mid;
  if (f(a)*f(mid) < 0) return bisectionMethod(a, mid, n-1);
  else return bisectionMethod(mid, b, n-1);
}

int main() {
  double a = 0.008;
  double b = 0.012;
  int n = 7;
  double error = (b-a)/pow(2, n);
  double sol = bisectionMethod(a,b,n);
  printf("f(%.16f) = %.16f\n", sol, f(sol));
  printf("error: %.16e\n", error);
  printf("%.16f - %.16f\n", sol-error, sol+error);
  return 0;
}
