#include <limits.h>
int myAtoi(char * str){
  int sign = 1;
  long num = 0;
  int i;
  int ascciiOffset = 48;
  for (i = 0; *(str + i) == ' '; i++) continue;
  if (*(str + i) == '-') {
    sign = -1;
    i++;
  } else if (*(str + i) == '+')
    i++;
  while (*(str + i) <= ascciiOffset + 9 && *(str + i) >= ascciiOffset) {
    num = 10*num - (*(str + i++) - ascciiOffset);
    if (sign > 0 && num < -1*INT_MAX)
      return INT_MAX;
    else if (sign < 0 && num < INT_MIN)
      return INT_MIN;
  }
  return (int)(-1*sign*num);
}

