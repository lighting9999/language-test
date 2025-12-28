const outer = 10000;
const inner = 10000;
let sum = 0;
const t1 = process.hrtime.bigint();
for (let i = 0; i < outer; ++i) {
  for (let j = 0; j < inner; ++j) {
    sum++;
  }
}
const t2 = process.hrtime.bigint();
const elapsed = Number(t2 - t1) / 1e9;
console.log(JSON.stringify({lang: "js", time: elapsed, sum}));
