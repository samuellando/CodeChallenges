impl Solution {
    pub fn all_paths_source_target(graph: Vec<Vec<i32>>) -> Vec<Vec<i32>> {

        let mut paths: Vec<Vec<i32>> = Vec::new();

        let mut stack: Vec<usize> = Vec::from([0].to_vec());
        let mut path_stack: Vec<Vec<i32>> = Vec::from([[0].to_vec()].to_vec());

        while !stack.is_empty() {
            let i = match stack.pop() {
                Some(e) => e,
                None => panic!("HOW")
            };

            let mut path = match path_stack.pop() {
                Some(e) => e.clone(),
                None => panic!("HOW")
            };

            for adj in &graph[i] {
                let mut p = path.clone();
                p.push(*adj);
                if *adj as usize == graph.len() - 1 {
                    paths.push(p);
                } else {
                    stack.push(*adj as usize);
                    path_stack.push(p)
                }
            }
        }

        paths
    }
}
