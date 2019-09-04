#define isLetter(c) ((c>=65&&c<=90)||(c>=97&&c<=122))

char * reverseOnlyLetters(char * S){
  // First determine the length of the string.
  int length;
  for (length = 0; *(S + length) != '\0'; length++) continue;
  // Burn the candle at both ends and skip over non letters.
  int f = 0;
  int b = length - 1;
  while (f < b) {
    if (!isLetter(*(S + f))) {
      f++;
      continue;
    } else if (!isLetter(*(S + b))) {
      b--;
      continue;
    } else {
      *(S + f) += *(S + b);
      *(S + b) = *(S + f) - *(S + b);
      *(S + f) = *(S + f) - *(S + b);
      f++;
      b--;
    }
  }
  return S;
}
