struct Zip<'a, A> {
    iters: [&'a mut dyn Iterator<Item = A>; 2],
    last: usize
}

impl<'a, A> Zip<'a, A> {
    fn new(a: &'a mut dyn Iterator<Item = A>, b: &'a mut dyn Iterator<Item = A>) -> Zip<'a, A> {
        let mut iters = [a, b];
        let n = iters.len() - 1;
        return Zip {iters: iters, last: n};
    }
}

impl<'a, A> Iterator for Zip<'a, A> {
    type Item = A;

    fn next(&mut self) -> Option<Self::Item> {
        self.last = (self.last + 1) % self.iters.len();
        let v =  self.iters[self.last].next();
        return v;
    }
}

impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> {
        let mut r = Vec::new();
        let n = n as usize;

        for i in Zip::new(&mut nums[..n].iter(), &mut nums[n..].iter()) {
            r.push(*i);
        }

        return r;
    }
}
