#!/usr/bin/node
function factorial (x) {
  if (x < 0) {
    return (-1);
  };
  if (x === 0 || isNaN(x)) {
    return (1);
  };
  return (x * factorial(x - 1));
};

const result = factorial(Number(process.argv[2]));
console.log(result);
