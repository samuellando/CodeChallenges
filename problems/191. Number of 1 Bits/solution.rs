impl Solution {
    pub fn hammingWeight (n: u32) -> i32 {
        let mut c = 0;
        let mut n = n;
        while n > 0 {
            if n & 1 == 1 {
                c += 1;
            }
            n = n >> 1;
        }
        return c;
    }
}
