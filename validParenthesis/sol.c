#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

struct stack {
  char c;
  struct stack* prev;
};

int isEmpty(struct stack* s) {
  return s->prev == NULL;
}

struct stack* push(struct stack* s, char c) {
  struct stack s1;
  s1.c = c;
  s1.prev = s;
  struct stack* sp1 = malloc(sizeof(struct stack));
  *sp1 = s1;
  return sp1;
}

struct stack* pop(struct stack* s) {
  char c = s->c;
  struct stack* s1 = s;
  s = s1->prev;
  free(s1);
  return s;
}

int isValid(char * str){
  struct stack* s = malloc(sizeof(struct stack));
  char c;
  for (int i = 0; *(str + i) != '\0'; i++)
    if (*(str + i) == '(' || *(str + i) == '[' || *(str + i) == '{')
      s = push(s, *(str + i));
    else
      if (isEmpty(s)) {
        free(s);
        return 0;
      }
      else {
        c = s->c;
        s = pop(s);
        switch (*(str + i)) {
          case ')':
            if (c != '(') {
              free(s);
              return 0;
            }
            break;
          case ']':
            if (c != '[') {
              free(s);
              return 0;
            }
            break;
          case '}':
            if (c != '{') {
              free(s);
              return 0;
            }
            break;
        }
      }
  if (!isEmpty(s)) {
    free(s);
    return 0;
  }
  free(s);
  return 1;
}

int main() {
  char s[] = "({[]})";
  printf("%d\n", isValid(s));
  return 0;
}
