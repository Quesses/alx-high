#!/usr/bin/node
let arg1 = process.argv[2];
if (isNaN(arg1) || arg1 === undefined) {
  console.log('MIssing size');
} else {
  const x = Number(arg1);
  let y = 0;
  while (y < x) {
    console.log('X'.repeat(x));
    y++;
  }
}
