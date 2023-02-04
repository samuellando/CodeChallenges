use std::collections::HashMap;

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut m = HashMap::new();

        for num in &nums {
            let count = m.entry(num).or_insert(0);
            *count += 1;
        }

        for (k, v) in &m {
            if v > &(nums.len() / 2) {
                return **(k);
            }
        }
        return -1;
    }
}
