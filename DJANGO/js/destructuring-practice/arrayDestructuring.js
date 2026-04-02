console.log("---- Array Destructuring ----");

var numbers = [10, 20, 30, 40];

var [a, b, c, d] = numbers;
console.log("Basic:", a, b, c, d);

var [first, , third] = numbers;
console.log("Skip:", first, third);

var [x, y, z = 100] = [1, 2];
console.log("Default:", x, y, z);

var num1 = 5;
var num2 = 15;
[num1, num2] = [num2, num1];
console.log("Swapped:", num1, num2);