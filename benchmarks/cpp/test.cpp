#include <iostream>
#include <chrono>

int main() {
    const long outer = 10000;
    const long inner = 10000;
    volatile long sum = 0;
    auto t1 = std::chrono::steady_clock::now();
    for (long i = 0; i < outer; ++i) {
        for (long j = 0; j < inner; ++j) {
            sum++;
        }
    }
    auto t2 = std::chrono::steady_clock::now();
    std::chrono::duration<double> d = t2 - t1;
    std::cout << "{\"lang\":\"cpp\",\"time\":" << d.count() << ",\"sum\":" << sum << "}\n";
    return 0;
}
