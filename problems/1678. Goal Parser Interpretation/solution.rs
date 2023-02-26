impl Solution {
    pub fn interpret(command: String) -> String {
        let mut command = command;
        let mut r = String::from("");

        while command.len() > 0 {
            if command.starts_with("G") {
                r += "G";
                command = match command.strip_prefix("G") {
                    Some(e) => e.to_string(),
                    None => panic!("No")
                };
            } else if command.starts_with("()") {
                r += "o";
                command = match command.strip_prefix("()") {
                    Some(e) => e.to_string(),
                    None => panic!("No")
                };
            } else if command.starts_with("(al)") {
                r += "al";
                command = match command.strip_prefix("(al)") {
                    Some(e) => e.to_string(),
                    None => panic!("No")
                };
            } else {
                panic!("NO");
            }
        }

        return r;
    }
}
