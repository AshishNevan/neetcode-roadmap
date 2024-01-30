fn main() {
    println!("{}", is_palindrome("1".to_string()));
}

pub fn is_palindrome(s: String) -> bool {
    let lowercase = s.to_ascii_lowercase();
    let filtrate: Vec<char> = lowercase.chars().filter(|f| f.is_alphanumeric()).collect();
    let l_to_r = filtrate.iter();
    let r_to_l = l_to_r.clone().rev();
    l_to_r.eq(r_to_l)
}
