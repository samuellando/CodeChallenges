impl Solution {
    pub fn is_palindrome(head: Option<Box<ListNode>>) -> bool {
        let mut stack: Vec<i32> = Vec::new();

        let mut  p = &head;

        loop {
            match p  {
                Some(e) => {
                    stack.push(e.val);
                    p = &e.next;
                },
                None => break
            }
        }

        p = &head;

        loop {
             match p  {
                Some(e) => {
                    if e.val != match stack.pop() {
                        None => return false,
                        Some(f) => {
                            p = &e.next;
                            f
                        }
                    } {
                        return false;
                    }
                },
                None => {
                    if stack.len() == 0 {
                        return true;
                    } else {
                        return false;
                    }
                }
             }
        }
    }
}
