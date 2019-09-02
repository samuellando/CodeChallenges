nArray(int* A, int ASize){
  short stage = 0; // 1 is climbing, 2 is decending
  for (int i = 1; i < ASize; i++)
    if (!stage && *(A + i - 1) < *(A + i))
      stage = 1;
    else if (!stage && *(A + i - 1) >= *(A + i))
      return false;
    else if (stage == 1 && *(A + i - 1) > *(A + i))
      stage = 2;
    else if (stage == 2 && *(A + i - 1) <= *(A + i))
      return false;
  return (stage == 2);
}
