int isLower(char c) {
  return ('a' <= c && c <= 'z');
}

int isUpper(char c) {
  return ('A' <= c && c <= 'Z');
}

int detectCapitalUse(char * word){
  // Linearly scan the string.
  for (int i = 1; *(word + i) != '\0'; i++)
    // If the first char is lower case, all others must all be lower case.
    if (isLower(*word) && isUpper(*(word + i)))
      return 0;
    // If the first char is upper case, 
    else if (isUpper(*word))
      // and the secound is lower case, all other must also be lower case.
      if (isLower(*(word + 1))) { 
        if (isUpper(*(word + i)))
          return 0;
      // and the secound is upper case, all others must be upper case.
      } else if (isLower(*(word + i))) //UPPEr
        return 0;
  return 1;
}
