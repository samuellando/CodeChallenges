package main

import (
  "fmt"
)

func maxProfit(prices []int) int {
  profit := 0
  t := -1 // Index of the buy transaction.
  status := 0 // 0 is decreaseing, 1 is increaseing.
  for i := 1; i < len(prices); i++ {
    if prices[i] >= prices[i-1] && status == 0 {
      // Buy on i-1
      t = i-1
      status = 1
    }
    if prices[i] <= prices[i-1] && status == 1 {
      // Sell on i-1
      if t != -1 {
        profit += prices[i-1] - prices[t]
        t = -1
      }
      status = 0
    }
  }
  // Sell the stock at the end.
  if t != -1 {
    profit += prices[len(prices)-1] - prices[t]
  }
  return profit

}

func main() {
  in := []int{200}
  fmt.Println(maxProfit(in))
}
