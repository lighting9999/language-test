.PHONY: all build run

all: build

build:
	clang -O2 -o c_bench benchmarks/c/test.c || true
	clang++ -O2 -o cpp_bench benchmarks/cpp/test.cpp || true
	cd benchmarks/rust && cargo build --release || true
	javac -d benchmarks/java/out benchmarks/java/src/Main.java || true

run:
	./run_bench.sh artifacts
