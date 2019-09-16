/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){
  if (head == NULL) return NULL;
  struct ListNode* next;
  struct ListNode* prev = head;
  head = head->next;
  prev->next = NULL;
  while (head != NULL) {
    next = head->next;
    head->next = prev;
    prev = head;
    head = next;
  }
  return prev;
}
