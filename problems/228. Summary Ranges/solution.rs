impl Solution {
    pub fn push(r: &mut Vec<String>, s: usize, e: usize, nums: &Vec<i32>)  {
        if s != e {
            r.push(format!("{}->{}", nums[s], nums[e]));
        } else {
            r.push(format!("{}", nums[s]));
        }
    }

    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        let mut r = Vec::new();

        if nums.len() == 0 {
            return r;
        }

        let mut s = 0;
        let mut e = 0;
        for (i, &n) in nums[1..].iter().enumerate() {
            if n  == nums[i] + 1 {
                e += 1;
            } else {
                Solution::push(&mut r, s, e, &nums);
                s = i+1;
                e = i+1;
            }
        }
        Solution::push(&mut r, s, e, &nums);
        
        return r;   
    }
}
