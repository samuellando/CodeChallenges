package main

import (
  "fmt"
)

type MinStack struct {
  top *node
}

type node struct {
  val int
  min int
  prev *node
}


/** initialize your data structure here. */
func Constructor() MinStack {
  this := MinStack{nil}
  return this
}


func (this *MinStack) Push(x int)  {
  var n node
  if this.top != nil {
    var min int
    if x < this.top.min {
      min = x
    } else {
      min = this.top.min
    }
    n = node{x, min, this.top}
  } else {
    n = node{x, x, nil}
  }
  this.top = &n
}


func (this *MinStack) Pop()  {
  if this.top != nil {
    this.top = this.top.prev
  }
}


func (this *MinStack) Top() int {
  return this.top.val
}


func (this *MinStack) GetMin() int {
  return this.top.min
}

func main() {
  obj := Constructor();
  obj.Push(1);
  obj.Push(20);
  obj.Pop();
  param_3 := obj.Top();
  param_4 := obj.GetMin();
  fmt.Printf("%d  %d", param_3, param_4)
}
