struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
  if (l1 == NULL) return l2;

  struct ListNode* head = l1;
  struct ListNode* prev = NULL;

  while (l2 != NULL)
    if (l1->val <= l2->val) {
      prev = l1;
      if (l1->next != NULL)
        l1 = l1->next;
      else {
        l1->next = l2;
        break;
      }
    }
    else {
      if (prev == NULL) {
        head = l2;
        l2 = l2->next;
        head->next = l1;
        prev = head;
      } else {
        prev->next = l2;
        l2 = l2->next;
        prev = prev->next;
        prev->next = l1;
      } 
    }
  return head;
}
