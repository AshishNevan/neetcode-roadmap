use std::collections::HashMap;

fn main() {
    println!("{:?}", two_sum(vec![3, 3], 6));
}

pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut hm: HashMap<i32, usize> = HashMap::new();
    for (index, &num) in nums.iter().enumerate() {
        hm.entry(num).or_insert(index);
    }
    for i in 0..nums.len() {
        if let Some(&j) = hm.get(&(target - nums[i])) {
            if i != j {
                return vec![j as i32, i as i32];
            } else {
                continue;
            }
        }
    }
    vec![-1, -1]
}
