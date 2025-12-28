#!/usr/bin/env python3
"""
Aggregate per-language JSON outputs (or error text) into:
 - results/summary.json (machine-readable)
 - results/report.md (human-readable)
Usage:
  python3 tools/aggregate_results.py artifacts results
"""
import json
import os
import sys
from glob import glob
from datetime import datetime

def load_entry(path):
    try:
        text = open(path, 'r', encoding='utf-8').read().strip()
        # try JSON first
        try:
            data = json.loads(text)
            return {"ok": True, "data": data, "raw": text}
        except Exception:
            # not JSON — treat as error/timeout
            return {"ok": False, "data": None, "raw": text}
    except Exception as e:
        return {"ok": False, "data": None, "raw": str(e)}

def main():
    if len(sys.argv) < 3:
        print("Usage: aggregate_results.py <artifacts_dir> <out_dir>")
        sys.exit(2)
    artifacts = sys.argv[1]
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)

    files = glob(os.path.join(artifacts, "*.json"))
    results = []
    for f in sorted(files):
        name = os.path.basename(f)
        lang = name.split('.')[0]
        entry = load_entry(f)
        entry_record = {
            "file": name,
            "lang": lang,
            "ok": entry["ok"],
            "raw": entry["raw"]
        }
        if entry["ok"] and isinstance(entry["data"], dict):
            entry_record["time"] = entry["data"].get("time")
            entry_record["sum"] = entry["data"].get("sum")
        else:
            entry_record["time"] = None
            entry_record["sum"] = None
        results.append(entry_record)

    summary = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "results": results
    }

    summary_path = os.path.join(out, "summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    # Human readable report
    lines = []
    lines.append("# language-test 报告")
    lines.append("")
    lines.append(f"生成时间 (UTC): {summary['generated_at']}")
    lines.append("")
    lines.append("## 概览")
    lines.append("")
    for r in results:
        if r["ok"]:
            lines.append(f"- **{r['lang']}**: time = {r['time']}, sum = {r['sum']}")
        else:
            lines.append(f"- **{r['lang']}**: ERROR / TIMEOUT — 原始输出: ```\\n{r['raw']}\\n```")
    lines.append("")
    # Sort by successful time asc
    succ = [r for r in results if r["ok"] and r["time"] is not None]
    succ_sorted = sorted(succ, key=lambda x: x["time"])
    if succ_sorted:
        lines.append("## 性能排名（成功运行者）")
        for i, r in enumerate(succ_sorted, 1):
            lines.append(f"{i}. {r['lang']} — {r['time']} s")
    else:
        lines.append("## 性能排名：无成功结果")
    lines.append("")

    report_path = os.path.join(out, "report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\\n".join(lines))
    print(f"Wrote {summary_path} and {report_path}")

if __name__ == "__main__":
    main()
