int checkPerfectNumber(int num) {
  // Negative numbers, 0 and 1 are all non perfect.
  if (num < 2) return 0;
  // 1 is always a divisor of num.
  int sum = 1;
  // Check all divisors from 0 to sqrt(num).
  for (int i = 2; i*i <= num; i++)
    if (num % i == 0)
      if (i*i != num)
        sum += (i + num/i);
      else
        sum += i;
  return (sum == num);
}
