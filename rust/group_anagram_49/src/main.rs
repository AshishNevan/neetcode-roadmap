use std::collections::HashMap;

fn main() {
    println!(
        "{:?}",
        group_anagrams(vec![
            "eat".to_string(),
            "tea".to_string(),
            "tan".to_string(),
            "ate".to_string(),
            "nat".to_string(),
            "bat".to_string()
        ])
    );
}

pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
    let mut hm: HashMap<Vec<u8>, Vec<String>> = HashMap::new();
    for str in strs {
        let mut ascii = [0; 26];
        for b in str.bytes() {
            ascii[(b - b'a') as usize] += 1;
        }
        hm.entry(ascii.to_vec()).or_default().push(str);
    }
    hm.values().cloned().collect()
}
