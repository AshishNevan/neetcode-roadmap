use std::collections::HashMap;

fn main() {
    println!(
        "{}",
        valid_anagram("anagram".to_string(), "nagaram".to_string())
    )
}

pub fn valid_anagram(s: String, t: String) -> bool {
    if s.len() == t.len() {
        let mut hm_s: HashMap<char, u32> = HashMap::new();
        let mut hm_t: HashMap<char, u32> = HashMap::new();

        for x in s.chars() {
            hm_s.entry(x).and_modify(|f| *f += 1).or_insert(1);
        }
        for y in t.chars() {
            hm_t.entry(y).and_modify(|g| *g += 1).or_insert(1);
        }
        hm_s.eq(&hm_t)
    } else {
        false
    }
}
