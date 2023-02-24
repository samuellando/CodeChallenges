use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut m: HashMap<char, u16> = HashMap::new();
        for l in s.chars() {
            match m.get(&l) {
                Some(i) => {m.insert(l, i + 1);},
                None => {m.insert(l, 1);}
            }
        }

        for l in t.chars() {
            match m.get(&l) {
                None | Some(0) => return false,
                Some(i) => {m.insert(l, i - 1);},
            }
        }

        return true;
    }
}
