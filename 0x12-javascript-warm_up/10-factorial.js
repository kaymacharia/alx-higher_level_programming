#!/usr/bin/node
function calculateFactorial(n) {
  if (isNaN(n)) {
    return 1; // Factorial of NaN is 1
  } else if (n === 0 || n === 1) {
    return 1; // Factorial of 0 and 1 is 1
  } else {
    return n * calculateFactorial(n - 1);
  }
}
const inputArgument = parseInt(process.argv[2]);
const result = calculateFactorial(inputArgument);
console.log(`Factorial of ${inputArgument} is: ${result}`);
