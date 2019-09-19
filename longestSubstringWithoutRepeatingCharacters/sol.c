nclude <stdlib.h>
#define max(a,b) a>b?a:b
int lengthOfLongestSubstring(char * s){
  int size = 0;
  int restSize = 0;
  int* seen = calloc(sizeof(int), 128); // Accomadate for the ascci table.

  for (int i = 0; *(s + i) != '\0'; i++)
    if (*(seen + *(s + i))) {
      break;
    } else {
      *(seen + *(s + i)) = 1;
      size++;
    }
  free(seen);
  if (*s != '\0')
    restSize = lengthOfLongestSubstring(s + 1);
  return max(size, restSize);
}
