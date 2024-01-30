fn main() {
    println!("{:?}", product_except_self(vec![-1, 1, 0, -3, 3]));
}

pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
    let mut prefix: Vec<i32> = vec![0; nums.len()];
    let mut suffix: Vec<i32> = vec![0; nums.len()];
    prefix[0] = 1;
    suffix[nums.len() - 1] = 1;
    for i in 1..nums.len() {
        prefix[i] = nums[i - 1] * prefix[i - 1];
    }
    // prefix = [1,1,2,6]
    println!("prefix: {:?}", prefix);

    for i in (0..=nums.len() - 2).rev() {
        suffix[i] = nums[i + 1] * suffix[i + 1];
    }
    // suffix = [24,12,4,1]
    println!("suffix: {:?}", suffix);

    prefix
        .iter()
        .zip(suffix.iter())
        .map(|(x, y)| x * y)
        .collect()
    // vec![]
}
