const fs = require("fs");
const csv = require("csv-parser");

// 결과를 저장할 빈 배열
const results = [];

// CSV 파일 읽기
fs.createReadStream("rawData/2013~2022 산불 - 5hr 이상.csv")
  .pipe(csv())
  .on("data", (data) => results.push(data))
  .on("end", () => {
    // JSON 파일로 저장
    fs.writeFileSync("output.json", JSON.stringify(results, null, 2));
  });
