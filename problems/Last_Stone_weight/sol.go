// This example demonstrates a priority queue built using the heap interface.
package main

import (
	"container/heap"
	"fmt"
)

type PriorityQueue []*Item

type Item struct {
	value int
}

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].value > pq[j].value
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

func (pq *PriorityQueue) Push(x interface{}) {
	item := x.(*Item)
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	*pq = old[0 : n-1]
	return item
}

func lastStoneWeight(stones []int) int {
	pq := make(PriorityQueue, len(stones))
	for i := 0; i < len(stones); i++ {
		pq[i] = &Item{stones[i]}
	}
	heap.Init(&pq)
	for pq.Len() > 1 {
		rem := heap.Pop(&pq).(*Item).value - heap.Pop(&pq).(*Item).value
		if rem > 0 {
			heap.Push(&pq, &Item{rem})
		}
	}
	if pq.Len() == 0 {
		return 0
	} else {
		return heap.Pop(&pq).(*Item).value
	}
}

func main() {
	fmt.Println(lastStoneWeight([]int{2,7,4,1,8,1}))
}