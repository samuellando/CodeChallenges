package main

type TreeNode struct {
  Val int
  Left *TreeNode
  Right *TreeNode
}

type Node struct {
  TreeNode
  LeftH int
  RightH int
}

func diameterOfBinaryTree(root *TreeNode) int {
  // Calculate height of the left and right subtrees for each node.
  nodes := make([]*Node, 0)
  _, _, nodesN := calcHeights(root, &nodes, 0)
  nodes = *nodesN

  max := 0
  for i := 0; i < len(nodes); i++ {
    if nodes[i] != nil && nodes[i].LeftH + nodes[i].RightH > max {
      max = nodes[i].LeftH + nodes[i].RightH
    }
  }
  return max
}

func calcHeights(node *TreeNode, a *[]*Node, i int) (int, int, *[]*Node) {
  if node == nil {
    return 0, 0, a
  }
  nodeN := &Node{*node, 0, 0}
  aN := append(*a, nodeN)
  a = &aN
  var leftH0 int
  var leftH1 int
  var rightH0 int
  var rightH1 int
  leftH0, leftH1, a = calcHeights(node.Left, a, i+1)
  rightH0, rightH1, a = calcHeights(node.Right, a, i+2)

  if leftH0 > leftH1 {
    nodeN.LeftH = leftH0
  } else {
    nodeN.LeftH = leftH1
  }
  if rightH0 > rightH1 {
    nodeN.RightH = rightH0
  } else {
    nodeN.RightH = rightH1
  }
  return nodeN.LeftH + 1, nodeN.RightH + 1, a
}
