#!/usr/bin/node
const arg1 = process.argv[2]
if (isNaN(arg1) || arg1 === undefined) {
  console.log('Missing number of occurrences')
} else {
  let x = Number(arg1)
  while (x > 0) {
    console.log('C is fun')
    x--
  }
}
