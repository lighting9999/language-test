# language-test

跨语言基准：比较 C / C++ / Python / Rust / JavaScript / Java 在执行指定“嵌套循环”任务时的运行时性能。

说明
- 默认任务：两个嵌套循环，总计 100,000,000 次简单整数累加（outer=10000, inner=10000）。
- 测量：wall-clock time（秒）和 sum 校验。每种语言输出 JSON，workflow 会把所有输出作为 artifact 上传。
- C/C++ 使用 clang 编译，其他语言使用各自最新稳定版本。
- 若某语言在 Actions 限制内未完成，将记录为 timeout。
- 完成后 workflow 会生成 `results/report.md`（人类可读）和 `results/summary.json`（机器可读）并上传为 artifact。

本地运行（示例）
- 安装相应工具链后：
  - make build
  - make run
