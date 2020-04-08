package main

type ListNode struct {
  Val int
  Next *ListNode
}

func middleNode(head *ListNode) *ListNode {
  // Find the length of the list.
  var l int
  lp := head
  for l = 0; lp.Next != nil; l++ {
    lp = lp.Next
  }
  // Now go to the middle.
  lp = head
  for i := 0; i <= l/2 ; i++ {
    lp = lp.Next
  }
  return lp
}
