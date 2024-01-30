use std::collections::HashSet;

fn main() {
    println!(
        "{}",
        longest_consecutive(vec![0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) //  [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
                                                                //  [F, T, T, T, T, T, T, T, F, T]
    );
}

pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
    let hs: HashSet<_> = nums.iter().collect();
    let mut longest = 0;
    for &num in &hs {
        if !hs.contains(&(num - 1)) {
            let mut length = 1;
            while hs.contains(&(num + length)) {
                length += 1;
            }
            longest = longest.max(length);
        }
    }
    longest as i32
}
