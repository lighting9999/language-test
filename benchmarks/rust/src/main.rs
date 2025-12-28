fn main() {
    let outer: usize = 10_000;
    let inner: usize = 10_000;
    let mut sum: usize = 0;
    let start = std::time::Instant::now();
    for _ in 0..outer {
        for _ in 0..inner {
            sum = sum.wrapping_add(1);
        }
    }
    let dur = start.elapsed();
    println!("{{\"lang\":\"rust\",\"time\":{:.6},\"sum\":{}}}", dur.as_secs_f64(), sum);
}
