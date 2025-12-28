#!/usr/bin/env bash
set -euo pipefail

OUT_DIR="${1:-artifacts}"
mkdir -p "$OUT_DIR"

# C (clang)
clang -O2 -o c_bench benchmarks/c/test.c || true
timeout 6h ./c_bench > "$OUT_DIR/c.json" || echo "C:timeout or failed" > "$OUT_DIR/c.json" || true

# C++ (clang++)
clang++ -O2 -o cpp_bench benchmarks/cpp/test.cpp || true
timeout 6h ./cpp_bench > "$OUT_DIR/cpp.json" || echo "CPP:timeout or failed" > "$OUT_DIR/cpp.json" || true

# Python (latest)
python3 benchmarks/python/test.py > "$OUT_DIR/python.json" || echo "PY:timeout or failed" > "$OUT_DIR/python.json" || true

# Rust (release)
pushd benchmarks/rust >/dev/null
cargo build --release || true
timeout 6h ./target/release/rust > "../../$OUT_DIR/rust.json" || echo "RUST:timeout or failed" > "../../$OUT_DIR/rust.json" || true
popd >/dev/null

# Node
node benchmarks/js/test.js > "$OUT_DIR/js.json" || echo "JS:timeout or failed" > "$OUT_DIR/js.json" || true

# Java
pushd benchmarks/java >/dev/null
javac -g:none -O src/Main.java -d out || true
timeout 6h java -cp out Main > "../$OUT_DIR/java.json" || echo "JAVA:timeout or failed" > "../$OUT_DIR/java.json" || true
popd >/dev/null

echo "Artifacts written to $OUT_DIR"
