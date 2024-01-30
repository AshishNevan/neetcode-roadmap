use std::collections::HashSet;

pub fn main() {
    println!("{}", contains_duplicate(vec![1, 2, 3, 1]))
}
pub fn contains_duplicate(nums: Vec<i32>) -> bool {
    let mut hs: HashSet<i32> = HashSet::new();
    !nums.iter().all(|f| hs.insert(*f))
}
