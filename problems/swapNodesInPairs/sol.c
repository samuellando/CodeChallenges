struct ListNode* swapPairs(struct ListNode* head){
  if (head == NULL || head->next == NULL) return head;

  struct ListNode* one = head;
  struct ListNode* two;
  struct ListNode* prev;
  head = one->next;

  while (one != NULL && one->next != NULL) {
    two = one->next;
    if (prev != NULL)
      prev->next = two;
    one->next = two->next;
    two->next = one;
    prev = one;
    one = one->next;
  }
  return head;
}
