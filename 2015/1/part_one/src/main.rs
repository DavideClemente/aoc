use std::{fs::File, io::Read};

fn main() -> std::io::Result<()> {
    let mut file = File::open("input.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    let mut balance: i16 = 0;
    let mut index: i16 = 0;
    for c in contents.chars() {
        if c == '(' {
            balance += 1
        }
        if c == ')' {
            balance -= 1
        }
        index += 1;
        if balance == -1 {
            break;
        }
    }
    println!("{}", index);
    Ok(())
}
