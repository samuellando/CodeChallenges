impl Solution {
    pub fn rearrange_array(mut nums: Vec<i32>) -> Vec<i32> {
        let mut neg: Vec<i32> = Vec::new();

        nums.retain(|e| {
            if *e < 0 {
                neg.push(*e);
                false
            } else {
                true
            }
        });

        for (i, n) in neg.into_iter().enumerate() {
            nums.insert(i * 2 + 1, n);
        }

        nums
    }
}
