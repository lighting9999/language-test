public class Main {
    public static void main(String[] args) {
        final int outer = 10000;
        final int inner = 10000;
        long sum = 0;
        long start = System.nanoTime();
        for (int i = 0; i < outer; i++) {
            for (int j = 0; j < inner; j++) {
                sum++;
            }
        }
        double elapsed = (System.nanoTime() - start) / 1e9;
        System.out.println(String.format("{\"lang\":\"java\",\"time\":%.6f,\"sum\":%d}", elapsed, sum));
    }
}
