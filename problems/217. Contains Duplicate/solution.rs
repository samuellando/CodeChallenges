use std::collections::HashMap;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut m = HashMap::new();

        for n in nums {
            match m.contains_key(&n) {
                true => return true,
                false => m.insert(n, 0),
            };
        }
        return false;
    }
}
