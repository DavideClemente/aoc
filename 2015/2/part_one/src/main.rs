use std::{fs::File, io::Read};

fn main() -> std::io::Result<()> {
    let mut file: File = File::open("../input.txt")?;
    let mut content: String = String::new();
    file.read_to_string(&mut content)?;
    let lines: std::str::Split<'_, char> = content.split('\n');
    for line in lines {
        let p: Vec<&str> = line.split('x').collect();

        let (side1, side2, side3) = match (
            p[0].parse::<i16>(),
            p[1].parse::<i16>(),
            p[2].parse::<i16>(),
        ) {
            (Ok(l), Ok(w), Ok(h)) => (l, w, h),
            _ => {
                panic!("Error");
            }
        };
        print!("{} {} {}", side1, side2, side3)
    }
    Ok(())
}
