.PHONY: all build run

all: build

build:
	clang -O3 -o c_bench benchmarks/c/test.c
	clang++ -O3 -o cpp_bench benchmarks/cpp/test.cpp
	cd benchmarks/rust && cargo build --release
	javac -d benchmarks/java/out benchmarks/java/src/Main.java

run:
	./run_bench.sh artifacts
