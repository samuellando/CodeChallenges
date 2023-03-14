impl Solution {
    pub fn min_operations(n: i32) -> i32 {
        if n % 2 != 0 {
            return ((n * n) - 1) / 4
        } else {
            return (n/2) * (n/2)
        }
    }
}
