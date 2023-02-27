struct Pos {
    x: i32,
    y: i32
}

impl Solution {
    pub fn execute_instructions(n: i32, start_pos: Vec<i32>, s: String) -> Vec<i32> {
        let mut pos: Pos;

        let mut ans: Vec<i32> = Vec::new();

        for i in 0..s.len() {
            pos = Pos { x: start_pos[1], y: start_pos[0] };
            ans.push(0);
            for c in s[i..].chars() {
                match c {
                    'R' => pos.x += 1,
                    'L' => pos.x -= 1,
                    'U' => pos.y -= 1,
                    'D' => pos.y += 1,
                    _ => panic!("Unexpected direction")
                }
                if pos.x >= 0 && pos.x < n && pos.y >= 0 && pos.y < n {
                    ans[i] += 1;
                } else {
                    break;
                }
            }
        }
        return ans;
    }
}
