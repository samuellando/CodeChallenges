impl Solution {
    pub fn is_power_of_two(n: i32) -> bool {
        let mut n = n;

        if n < 0 {
            return false;
        }

        while n != 0 {
            if n & 1 == 1 {
                if n >> 1 != 0 {
                    return false;
                } else {
                    return true;
                }
            } else {
                n = n >> 1;
            }
        }
        return false;
    }
}
