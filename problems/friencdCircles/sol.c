/*
   void DFSUtil(int** M, int* visited, int root, int size) {
 *(visited + root) = 1;
 for (int i = root + 1; i < size; i++)
 if (*(M + (root * size) + i) && !*(visited + i))
 DFS(M, visited, i, size);
 }
 To eliminate practical time complexities, this is a iterative version of the
 above DFS algorithm.
 */
#define stackPush(root, stack, sp) stack[sp++]=root
#define stackPop(stack, sp) stack[--sp]
void DFSUtil(int** M, int* visited, int root, int size) {
  int stack[size];
  int sp = 0;
  stackPush(root, stack, sp);
  *(visited + root) = 1;
  while (sp > 0) {
    root = stackPop(stack, sp);
    for (int i = 0; i < size; i++)
      if (i != root && *(*(M + root) + i)&& !*(visited + i)) {
        *(visited + i) = 1;
        stackPush(i, stack, sp);
      }
  }
}

int findCircleNum(int** M, int MSize, int* MColSize) {
  // An implementation of depth first search.
  /*
   * Will be O(n^2) due to the use of a adjency matrix for the graph
   * reprisentation.
   */
  int visited[MSize];
  for (int i = 0; i < MSize; i++)
    visited[i] = 0;
  int circles = 0;
  for (int i = 0; i < MSize; i++)
    if (!visited[i]) {
      circles++;
      DFSUtil(M, visited, i, MSize);
    }
  return circles;
}
