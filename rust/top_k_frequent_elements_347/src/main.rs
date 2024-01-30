use std::collections::HashMap;

fn main() {
    println!(
        "{:?}",
        top_k_frequent(vec![3,0,1,0], 1)
    )
}

pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
    let freqs = nums.iter().copied().fold(HashMap::new(), |mut map, val|{
        map.entry(val).and_modify(|f| *f+=1).or_insert(1);
        map
    });
    let mut bucket_sort: Vec<i32>= [0].repeat(100).to_vec();
    // println!("{:?}", bucket_sort);
    for freq in freqs{
        bucket_sort.insert(freq.1 as usize, freq.0)
    }
    let mut res = Vec::with_capacity(k as usize);
    let mut count = 0;
    while count < k {
        match bucket_sort.pop() {
            None => {}
            Some(x) => {
                count += 1;
                res.push(x);
            }
        }
    }
    res
}
