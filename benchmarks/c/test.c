#include <stdio.h>
#include <time.h>

int main() {
    const long outer = 10000;
    const long inner = 10000;
    volatile long sum = 0;
    struct timespec a,b;
    clock_gettime(CLOCK_MONOTONIC, &a);
    for (long i = 0; i < outer; ++i) {
        for (long j = 0; j < inner; ++j) {
            sum++;
        }
    }
    clock_gettime(CLOCK_MONOTONIC, &b);
    double elapsed = (b.tv_sec - a.tv_sec) + (b.tv_nsec - a.tv_nsec)/1e9;
    printf("{\"lang\":\"c\",\"time\":%.6f,\"sum\":%ld}\n", elapsed, sum);
    return 0;
}
