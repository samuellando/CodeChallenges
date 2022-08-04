int strStr(char * haystack, char * needle){
  if (needle[0] == '\0') return 0;
  for (long i = 0; haystack[i] != '\0'; i++)
    for (long j = 0; needle[j] == haystack[i+j]; j++)
      if (needle[j+1] == '\0') return i;
      else if (haystack[i + j] == '\0') break;
  return -1;
}

