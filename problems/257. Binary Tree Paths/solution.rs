// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn binary_tree_paths(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<String> {
        let mut paths: Vec<String> = Vec::new();
        let mut sol: Vec<String> = Vec::new();

        let mut stack: Vec<Rc<RefCell<TreeNode>>> = Vec::new();
        
        stack.push(root.clone().unwrap());
        paths.push(format!("{}", root.clone().unwrap().borrow().val));

        while stack.len() > 0 {
            let pr = stack.pop().clone().unwrap();
            let p = pr.borrow();
            let path = paths.pop().unwrap();

            if p.right == None && p.left == None {
                // It's a leaf.
                sol.push(path.clone());
            } else {
                if p.right != None {
                    stack.push(p.right.clone().unwrap());
                    paths.push(format!("{path}->{}", p.right.clone().unwrap().borrow().val));
                }
                if p.left != None {
                    stack.push(p.left.clone().unwrap());
                    paths.push(format!("{path}->{}", p.left.clone().unwrap().borrow().val));
                }
            }
        }

        return sol;
    }
}
